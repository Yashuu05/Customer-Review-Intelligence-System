import pandas as pd
from sklearn.model_selection import train_test_split
import os
import sys 
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def load_data(df_path):
    """
    read csv file
    input: csv file path
    output: csv file or dataset
    """
    try:
        df = pd.read_csv(df_path)
        print(f"{df_path} load successfully")
        return df
    except Exception as e:
        print(f"error: {e}")

def split_dataset(randomState: int, testSize: float, X, y) -> tuple:
    """
    split dataset into training and testing with given ratio

    Input: 
    random state, testSize, X, y

    Output: 
    X_train, X_test, y_train, y_test  
    """
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=randomState, test_size=testSize, shuffle=True)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"error: {e}")

def create_num_cat_list(df):
    """
    create the list of separate list of categorical and numerical features from the given datast

    Input: 
    df : dataset

    Output: 
    numerical_cols: columns with numerical features
    categorical_cols: columns with categorical features 
    """
    numerical_cols = []
    categorical_cols = []

    try:
        for cols in df.columns:
            if df[cols].dtypes == "object":
                categorical_cols.append(cols)
            else:
                numerical_cols.append(cols)

        print("numerical cols: \n", numerical_cols)
        print("\ncategorical cols: \n", categorical_cols)

        return numerical_cols, categorical_cols

    except Exception as e:
        print(f"error: {e}")

def load_hyperparameters(file_path=os.path.join(project_root, "configs", "hyperparameters.json")):
    """
    read configs/hyperparameters.json file to load hyperparameters specified for each ML algorithm.

    Input: file path
    Output: hyperparameter file
    """
    import json
    try:
        with open(file_path, mode="+r", encoding="utf-8") as file:
            params = json.load(file)
        if params is None:
            print("Hyperaparameter file couldn't load.")
            return None
        
        return params
    except Exception as e:
        print(f"error: {e}")