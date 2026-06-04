import os
import sys 
from dotenv import load_dotenv
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from src.logger import logging as log
import json
file_path = os.path.join(project_root, "configs", "hyperparameters.json")

try: 
    with open(file_path, encoding="utf-8", mode="+r") as file:
        params = json.load(file)
    
    if params is None:
        print("hyperparameter file couldn't load")

    print("Random Forest hyperparameters: \n", params["random_forest"])
    log.info("successfully access RandomForest hyperaparameters.")

except Exception as e:
    log.error(f"{e}")
    print(f"error: {e}")