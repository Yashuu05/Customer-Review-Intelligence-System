from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

nlp_models = {
    "logistic_regression": LogisticRegression(solver="saga", class_weight="balanced"),
    "random_forest": RandomForestClassifier(),
    "lightgbm": LGBMClassifier(),
    "xgboost": XGBClassifier()
}