"""
train several algorithms to find the best algorithm having high accuracy
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

def evaluate_model(y_test, y_pred) -> list:
    """
    calculates performance metrics of the Ml model such as :
    1. accuracy
    2. recall
    3. precision
    4. f1_score
    5. roc_auc_score

    Inputs: y_test: target test data  |   y_pred: predicted values by model
    Output: accuracy, recall, precision, f1_score, roc_auc_score 
    """

    acc = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

    return [acc, recall, precision, f1] 

def find_max_accuracy(result: dict) -> tuple:
    """
    finds the maximum accuracy along with the model name

    Input: dictionary of results
    Output: maximum accuracy, model name
    """
    max_accuracy = 0
    model_name = ""
    for key, val in result.items():
        model_accuracy = val[0]
        if model_accuracy > max_accuracy:
            max_accuracy = model_accuracy
            model_name = key

    return max_accuracy, model_name

def train_nlp(X_train, y_train, X_test, y_test) -> None:
    """
    train each model on the training dataset by using hyperparameters and evaluates each model to find
    best model having hihgest accuracy
    """
    # load hyperparameters
    param_grid = data_utils.load_hyperparameters(file_path=os.path.join(project_root, "configs", "hyperparameters.json"))
    # store the results
    result = {}
    # store best params
    best_params = {}
    # store trained model
    trained_models = {}

    for model_name, model in nlp_models.items():
        # strip 'model__' prefix since estimator is not a Pipeline
        if isinstance(param_grid[model_name], list):
            model_params = []
            for param_dict in param_grid[model_name]:
                model_params.append({k.replace('model__', ''): v for k, v in param_dict.items()})
        else:
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
        
        # store the model
        trained_models[model_name] = best_model

        # store best parameters
        best_params[model_name] = {"best_parameters" : model_grid.best_params_, "best_score" : model_grid.best_score_}
        
        print("\npredicting target values...")
        # predict the values
        y_pred = model_grid.predict(X_test)

        # evaluate model
        evaluation_lst = evaluate_model(y_test=y_test, y_pred=y_pred)

        # store the evaluation metrics
        result[model_name] = evaluation_lst 

    # find highest accuracy 
    print("\nfinding highest accuracy...")
    accuracy, best_model_name = find_max_accuracy(result=result)
    print(f"highest accuracy = {accuracy}\nmodel name = {best_model_name}")
    # save best model
    print(f"\nsaving {best_model_name}...")
    nlp_model = trained_models[best_model_name]
    joblib.dump(nlp_model, filename=os.path.join(project_root, "model", f"{best_model_name}_nlp.joblib"))

    print("\nsaving results...")
    # save results
    data_utils.save_json(data=result, file_path=os.path.join(project_root, "results", "result_metrics.json"))

    # save best parameters of each model
    data_utils.save_json(data=best_params, file_path=os.path.join(project_root, "results", "best_parameters.json"))


def word_embed_reviews(df):
    """
    This function converts raw text into word embedding using tokenization, stopwords, lemmatization, and 
    word2vec. The resulting single sentence has word embedding of 100 dimensions.
    
    - Input: raw dataset
    - Output: word embedding array
    """
    nltk.download("stopwords")
    nltk.download("wordnet")
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
    # save word2vec model
    word2vec_path = os.path.join(project_root, "model", "word2vec.model")
    print(f"saving word2vec model to {word2vec_path}")
    word2vec_model.save(word2vec_path)

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
        print("============ training initialized =================")
        log.info("initialized training for nlp")

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
            print("\n5. training models")
            train_nlp(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)
            log.info("training of model completed")

        else:
            print("\nError loading dataset.")

    except Exception as e:
        print(f"error: {e}")
        log.error(f"{e}")