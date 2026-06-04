import os
import sys 
from dotenv import load_dotenv
import mysql.connector
load_dotenv()
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if project_root not in sys.path:
    sys.path.insert(0, project_root)
from src.logger import logging as log

# get database credentials
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

# intialize log
log.info("connecting database.")

if not username and not password:
    log.error("Database credentials not found.")
    print("credentials not found")

def connect_to_db(username: str, password: str) -> None:
    
    """
    connect to the local MySQL server to create a new database 'nlp_db'

    inputs:
    1. password: MySQL password set during installation
    2. username : MySQL username

    output: if connection is successful or not
    """
    try:
        # 1. Establish the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',        # Change to server IP if remote
            user=username,             
            password=password, 
            database='nlp_db' 
        )
    
        if connection.is_connected():
            log.info("Database connection successful.")
            print("Successfully connected to the database!")

    except Exception as e:
        log.error(f"{e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    connect_to_db(password=password, username=username)