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
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score, precision_score, recall_score
from src.logger import logging as log
from configs.model_config import nlp_models
from utils import data_utils
import re
import nltk
from nltk.corpus import stopwords

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
    recall = recall_score(y_test, y_pred, average='weighted')
    precision = precision_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    roc = roc_auc_score(y_test, y_pred, average='weighted')

    return [acc, recall, precision, f1, roc] 

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
        # intergrate hyperparameter
        model_grid = GridSearchCV(
            estimator=model,
            params = param_grid[model_name],
            verbose = 2,
            n_jobs = -1,
            scoring = "accuracy",
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
        evaluation_lst = evaluate_model(model=best_model, y_test=y_test, y_pred=y_pred)

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


def preprocess_dataset(df):
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))

    print("\n", df.head(3))
    print("\nshape of data = ", df.shape)
    data = df[["Summary","Sentiment"]]
    print("\nusing dataset = \n", data.head(3))

    def clean_text(text):
        text = text.lower()
        cleaned_text = re.sub(r'[^a-zA-Z]',' ', text)
        token = cleaned_text.split()



if __name__ == "__main__":
    print("============ training initialized =================")
    log.info("initialized training for nlp")

    # step 1 
    print("1. loading dataset...")
    df = data_utils.load_data(df_path=os.path.join(project_root, "data", "dataset.csv"))
    if df is not None:
        # preprocess dataset
        pass
    else:
        print("\nError loading dataset.")