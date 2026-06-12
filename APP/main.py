from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os 
import sys
from dotenv import load_dotenv
import joblib
import mysql.connector
from gensim.models import Word2Vec
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
import numpy as np
import re
import datetime
from zoneinfo import ZoneInfo

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from database.connect_db import connect_to_db

load_dotenv()
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
NLP_MODEL = "lightgbm"
MODEL_PATH = os.path.join(project_root, "model", f"{NLP_MODEL}_nlp.joblib")
WORD2VEC_PATH = os.path.join(project_root, "model", f"{NLP_MODEL}_word2vec.model")

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_flash_messages'

# Try loading NLP models at startup to avoid slow request processing
try:
    print("loading resources... ")
    print("loading NLP model")
    nlp = joblib.load(filename=MODEL_PATH)
    print("laoding word2vec model")
    word2vec_model = Word2Vec.load(WORD2VEC_PATH)
    print("checking stopwords")
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("downloading stopwords")
        nltk.download("stopwords", quiet=True)
        
    print("checking wordnet")
    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download("wordnet", quiet=True)
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    models_loaded = True
    print("download completed")
except Exception as e:
    print(f"Warning: Could not load NLP models. Error: {e}")
    models_loaded = False

@app.route('/submit', methods=['POST'])
def submit():
    if not models_loaded:
        return jsonify({"error": "NLP models are not loaded on the server."}), 500

    def predict_sentiment(review: str):
        processed_tokens = []
        vectors = []
        sentiment = ""
        # preprocess the review
        review = review.lower()
        review = re.sub(r'[^a-zA-Z]',' ', review)
        review_tokens = review.split()
        
        for word in review_tokens:
            if word not in stop_words:
                processed_tokens.append(lemmatizer.lemmatize(word))
        for word in processed_tokens:
            if word in word2vec_model.wv:
                vectors.append(word2vec_model.wv[word])
        if len(vectors) == 0:
            vector = np.zeros(100)
        else:
            vector = np.mean(vectors, axis=0)
            
        # prediction expects a 2D array
        prediction = nlp.predict([vector])
        try:
            probability = float(prediction[0])
            print(f"probability : {probability}")
        except (TypeError, IndexError, ValueError):
            probability = 0.99
            
        pred_val = prediction[0]
        if pred_val == 0:
            sentiment = "negative"
        elif pred_val == 1:
            sentiment = "neutral"
        else:
            sentiment = "positive"
        return sentiment, probability

    # Retrieve information submitted through the HTML form fields
    age = request.form.get('age')
    gender = request.form.get('gender')
    role = request.form.get('role')
    item = request.form.get('product')
    state = request.form.get('state')
    city = request.form.get('city')
    rating = request.form.get('rating')
    review = request.form.get('feedback', '')
    
    sentiment, probability = predict_sentiment(review=review)

    try:
        # Establish connection to MySQL
        if not username or not password:
            return jsonify({"error": "Database credentials not configured."}), 500

        conn = connect_to_db(username=username, password=password)
        mycursor = conn.cursor()
        
        current_time = datetime.datetime.now(ZoneInfo("Asia/Kolkata"))
        
        # Use parameterized queries (%s placeholders) to prevent SQL Injection
        sql_queries = [
            ("INSERT INTO personal_info (role, gender, age, product, date) VALUES (%s, %s, %s, %s)", (role, gender, age, current_time)),
            ("INSERT INTO geo_info (city, state) VALUES (%s, %s)", (city, state)),
            ("INSERT INTO reviews (feedback, output, probability) VALUES (%s, %s, %s)", (review, sentiment, probability)),
            ("INSERT INTO items (rating, product) VALUES (%s, %s)", (rating, item))
        ]
        
        # execute the queries
        for query, params in sql_queries:
            mycursor.execute(query, params)
        conn.commit()
        
        # Close connection assets
        mycursor.close()
        conn.close()
        
        return jsonify({"message": "Data successfully saved to the MySQL database!"}), 200
        
    except mysql.connector.Error as err:
        return jsonify({"error": f"Database Error: {err}"}), 500
    except Exception as err:
        return jsonify({"error": f"Unexpected Error: {err}"}), 500
    
@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('signup'))
        
        # Mock Authentication
        if email == 'yash@gmail.com' and password == 'yash123':
            return redirect(url_for('admin'))
        else:
            flash('For testing, please use yash@gmail.com / yash123', 'error')
            return redirect(url_for('signup'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Mock Authentication
        if email == 'yash@gmail.com' and password == 'yash123':
            return redirect(url_for('admin'))
        else:
            flash('Invalid email or password. Use yash@gmail.com / yash123', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

feedback_is_live = False

@app.route('/feedback')
def feedback():
    if not feedback_is_live:
        return render_template('feedback_closed.html')
    return render_template('feedback_form.html')

@app.route('/admin')
def admin():
    return render_template('admin_dashboard.html', feedback_is_live=feedback_is_live)

@app.route('/admin/launch_feedback', methods=['POST'])
def launch_feedback():
    global feedback_is_live
    feedback_is_live = True
    flash('Feedback form is now live.', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/close_feedback', methods=['POST'])
def close_feedback():
    global feedback_is_live
    feedback_is_live = False
    flash('Feedback form is now closed.', 'success')
    return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)