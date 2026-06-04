"""
train several algorithms to find the best algorithm having high accuracy
"""
import os
import sys 
from dotenv import load_dotenv
import mysql.connector
load_dotenv()
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if project_root not in sys.path:
    sys.path.insert(0, project_root)
from src.logger import logging as log
from database.connect_db import connect_to_db