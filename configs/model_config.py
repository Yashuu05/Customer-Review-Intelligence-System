from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

nlp_models = {
    "logistic regression": LogisticRegression(),
    "random forest": RandomForestClassifier(),
    "lightgbm": LGBMClassifier(),
    "xgboost": XGBClassifier()
}