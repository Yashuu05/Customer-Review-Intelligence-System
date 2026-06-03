import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.logger import logging

if __name__ == "__main__":
    logging.info("This is a log message from an external module.")
    try:
        a = 1 / 0
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    
    print("Testing complete. Check the logs folder.")