"""
train a single selected algorithm to find its performance
"""
import os
import sys 
from dotenv import load_dotenv
load_dotenv()
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score, precision_score, recall_score
from src.logger import logging as log
from configs.model_config import nlp_models
from utils import data_utils
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec
from sklearn.preprocessing import LabelEncoder

# ==========================================
# UPDATE THIS VARIABLE TO TRAIN DESIRED MODEL
# Available models: "logistic_regression", "random_forest", "lightgbm", "xgboost"
# ==========================================
TARGET_MODEL_NAME = "random_forest"

def evaluate_model(y_test, y_pred) -> list:
    """
    calculates performance metrics of the Ml model such as :
    1. accuracy
    2. recall
    3. precision
    4. f1_score

    Inputs: y_test: target test data  |   y_pred: predicted values by model
    Output: accuracy, recall, precision, f1_score
    """
    acc = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

    return [acc, recall, precision, f1] 

def train_single_model(X_train, y_train, X_test, y_test, model_name: str) -> None:
    """
    train the specified model on the training dataset by using hyperparameters and evaluates the model
    """
    if model_name not in nlp_models:
        print(f"Error: Model '{model_name}' not found in configs.model_config.nlp_models")
        return

    model = nlp_models[model_name]

    # load hyperparameters
    param_grid = data_utils.load_hyperparameters(file_path=os.path.join(project_root, "configs", "hyperparameters.json"))
    
    if model_name not in param_grid:
        print(f"Error: Hyperparameters for '{model_name}' not found in configs/hyperparameters.json")
        return

    # strip 'model__' prefix since estimator is not a Pipeline
    model_params = {k.replace('model__', ''): v for k, v in param_grid[model_name].items()}

    # intergrate hyperparameter
    model_grid = GridSearchCV(
        estimator=model,
        param_grid=model_params,
        verbose=2,
        n_jobs=-1,
        scoring="accuracy",
        cv=3
    )
    
    print(f"\ntraining {model_name}...")
    model_grid.fit(X_train, y_train)
    
    # best model
    best_model = model_grid.best_estimator_
    
    print("\npredicting target values...")
    # predict the values
    y_pred = model_grid.predict(X_test)

    # evaluate model
    evaluation_lst = evaluate_model(y_test=y_test, y_pred=y_pred)
    accuracy, recall, precision, f1 = evaluation_lst
    
    print(f"\nResults for {model_name}:")
    print(f"Accuracy: {accuracy}")
    print(f"Recall: {recall}")
    print(f"Precision: {precision}")
    print(f"F1 Score: {f1}")

    # save best model
    print(f"\nsaving {model_name}...")
    joblib.dump(best_model, filename=os.path.join(project_root, "model", f"{model_name}_nlp.joblib"))

    # save results
    print("\nsaving results...")
    result = {model_name: evaluation_lst}
    data_utils.save_json(data=result, file_path=os.path.join(project_root, "results", f"{model_name}_result_metrics.json"))

    # save best parameters of the model
    best_params = {model_name: {"best_parameters" : model_grid.best_params_, "best_score" : model_grid.best_score_}}
    data_utils.save_json(data=best_params, file_path=os.path.join(project_root, "results", f"{model_name}_best_parameters.json"))

def word_embed_reviews(df):
    """
    This function converts raw text into word embedding using tokenization, stopwords, lemmatization, and 
    word2vec. The resulting single sentence has word embedding of 100 dimensions.
    
    - Input: raw dataset
    - Output: word embedding array
    """
    nltk.download("stopwords", quiet=True)
    nltk.download("wordnet", quiet=True)
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    embedding_size = 100

    print("\n", df.head(3))
    print("\nshape of data = ", df.shape)
    data = df[["Summary","Sentiment"]].copy()
    print("\nusing dataset = \n", data.head(3))

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
    
    print("\npreprocessing the text")
    data["Summary"] = data["Summary"].apply(preprocess_text)
    
    # training word2vec model
    word2vec_model = Word2Vec(
        sentences=data["Summary"],
        vector_size=embedding_size,
        window=5,
        min_count=1,
        workers=4
    )

    # word embedding 
    def document_vector(tokens):
        vectors = []
        for word in tokens:
            if word in word2vec_model.wv:
                vectors.append(
                    word2vec_model.wv[word]
                )

        if len(vectors) == 0:
            return np.zeros(embedding_size)

        return np.mean(vectors, axis=0)
    
    print("Implementing Word Embedding")
    X = np.array([
        document_vector(tokens) for tokens in data["Summary"]
    ])
    print("\nshape of Word Embedding array: ", X.shape)
    return X 

def preprocess_target(df, target):
    """
    Encodes the target values using LabelEncoder.
    - Input: raw dataset (dataframe)  |  target (target feature name)
    - output: LabelEncode target series
    """
    print("\npreprocessing the target valuees...")
    y = df[target]
    encoder = LabelEncoder()
    encoded_array = encoder.fit_transform(y)
    encoded_series = pd.Series(encoded_array, name=target)
    print("\nencoded target = \n", encoded_series.head(8))
    print("\nshape of encoded target = ", encoded_series.shape)
    return encoded_series

#======================================================================================================    

if __name__ == "__main__":
    try:
        print(f"============ training initialized for {TARGET_MODEL_NAME} =================")
        log.info(f"initialized training for {TARGET_MODEL_NAME}")

        # step 1 
        print("1. loading dataset...")
        df = data_utils.load_data(df_path=os.path.join(project_root, "data", "dataset.csv"))
        if df is not None:
            log.info("dataset read successfully.")
        
            # step 2: preprocess dataset
            print("\n2. preprocessing the reviews...")
            X = word_embed_reviews(df=df)
            log.info("word embedding implemented.")
        
            # step 3 : preprocess target values
            print("\n3. Preprocessing target values...")
            y = preprocess_target(df=df, target="Sentiment")
        
            # step 4: split dataset
            print("\n4. splitting dataset...")
            X_train, X_test, y_train, y_test = data_utils.split_dataset(
                randomState=42,
                testSize=0.20,
                X=X,
                y=y
            )
            log.info("Split the dataset successfully")
            
            # step 5: train model
            print(f"\n5. training model {TARGET_MODEL_NAME}")
            train_single_model(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, model_name=TARGET_MODEL_NAME)
            log.info(f"training of {TARGET_MODEL_NAME} completed")

        else:
            print("\nError loading dataset.")

    except Exception as e:
        print(f"error: {e}")
        log.error(f"{e}")
