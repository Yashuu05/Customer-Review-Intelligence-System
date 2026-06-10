"""
calculate the accuracy of lightgbm classification 
"""

import pandas as pd
import os
import sys 
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
df = pd.read_csv(os.path.join(project_root, "results", "test_results.csv"))

correct_predicted = len(df[df["actual"] == df["predicted"]])
accuracy = (correct_predicted / df.shape[0]) * 100
print(f"accuracy of test results = {accuracy:.2f} %")