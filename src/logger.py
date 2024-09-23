import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")  # Path to the logs directory
os.makedirs(logs_path, exist_ok=True)  # Create the directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # Full path to the log file
logging.basicConfig(filename=LOG_FILE_PATH,  # Use the full file path here
                    format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

