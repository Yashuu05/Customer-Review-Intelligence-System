# test the NLP model saved in model/ folder to classify the customer reviews
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib
import re 
import os 
import sys 
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from src.logger import logging as log
import numpy as np
from gensim.models import Word2Vec
import pandas as pd
import random

MODEL_NAME = "lightgbm"
MODEL_PATH = os.path.join(project_root, "model", f"{MODEL_NAME}_nlp.joblib")
word2vec_path = os.path.join(project_root, "model", f"{MODEL_NAME}_word2vec.model")

def classify_review(model, df) -> None:
    nltk.download("stopwords", quiet=True)
    nltk.download("wordnet", quiet=True)
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    try:
        def preprocess_text(text):
            if not isinstance(text, str):
                text = ""
            text = text.lower()
            cleaned_text = re.sub(r'[^a-zA-Z]',' ', text)
            token = cleaned_text.split()
            processed_tokens = []
            for word in token:
                if word not in stop_words:
                    processed_tokens.append(lemmatizer.lemmatize(word))
            return processed_tokens
        
        # preprocess the reviews
        log.info("preprocessing the reviews")
        processed_series = df["review"].apply(preprocess_text)

        log.info(f"loading word2vec model from {word2vec_path}")
        word2vec_model = Word2Vec.load(word2vec_path)

        def document_vector(tokens):
            vectors = []
            for word in tokens:
                if word in word2vec_model.wv:
                    vectors.append(word2vec_model.wv[word])
            if len(vectors) == 0:
                return np.zeros(100)
            return np.mean(vectors, axis=0)
        
        # word embedding
        log.info("converting reviews into vectors.")
        review_vectors = np.array([document_vector(tokens) for tokens in processed_series])

        # predict the output using trained model
        log.info("predicting the output")
        predictions = model.predict(review_vectors)
        
        sentiments = []
        for pred in predictions:
            if pred == 0:
                sentiments.append("negative")
            elif pred == 1:
                sentiments.append("neutral")
            else:
                sentiments.append("positive")
                
        # save result into a csv file 
        pd.DataFrame({
            "review": df["review"],
            "predict": predictions,    
            "sentiment": sentiments               
        }).to_csv(os.path.join(project_root, "results", "test_results.csv"), index=False)    
        log.info("saved results to the 'results' folder")   

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__": 

    random.ra

    log.info("Testing initiated")
    print("loading saved lightgbm model...")
    lgbm = joblib.load(MODEL_PATH)
    if lgbm is not None:
        log.info(f"{MODEL_NAME} model load from {MODEL_PATH}")
        print(f"{MODEL_NAME} loaded succesfully")
        classify_review(lgbm, df)
    else:
        log.error(f"Error while loading model from path {MODEL_PATH}")
        print("Error: model failed to load.")