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
# get database credentials
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

log.info("connecting database.")

if not username and not password:
    log.error("Database credentials not found.")
    print("credentials not found")

def create_table():

    # connect to database nlp_db
    conn = connect_to_db(username=username, password=password)
    # create cursor
    mycursor = conn.cursor()

    try: 
        table_queries = [
            """
            CREATE TABLE IF NOT EXISTS personal_info (
                id INT AUTO_INCREMENT PRIMARY KEY,
                role VARCHAR(50) NOT NULL,
                gender VARCHAR(50),
                age INT CHECK(age >= 18),
                date DATE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS geo_info (
                id INT,
                FOREIGN KEY (id) REFERENCES personal_info(id),
                state VARCHAR(50) NOT NULL,
                city VARCHAR(50)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS reviews (
                id INT,
                FOREIGN KEY (id) REFERENCES personal_info(id),
                feedback TEXT NOT NULL,
                output VARCHAR(50) NOT NULL,
                probability DECIMAL(10,2) NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS items(
            id INT,
            FOREIGN KEY (id) REFERENCES personal_info(id),
            rating INT,
            product VARCHAR(50)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS admin (
                admin_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE,
                password VARCHAR(50) UNIQUE,
                register_date DATE
            )
            """
        ]
        # execute the commands sequentially
        for query in table_queries:
            mycursor.execute(query)
        conn.commit()
        log.info("tables 'personal_info', 'geo_info', 'reviews', 'admin' created successfully.")
        print("Tables created successfully!")

    except Exception as e:
        log.error(f"error while connection to MySQL: {e}")
        print(f"Error: {e}")

    finally:
        # close cursor
        if 'mycursor' in locals() and mycursor is not None:
            mycursor.close()
        if 'conn' in locals() and conn is not None and conn.is_connected():
            conn.close()
            log.info("MYSQL connection closed.")
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_table()