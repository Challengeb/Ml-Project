import logging
import os
import datetime
from logging import Logger, FileHandler, StreamHandler, Formatter
LOG_FILE=f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
log_file_path=os.path.join(logs_path,LOG_FILE)
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s',
                    handlers=[
                        FileHandler(log_file_path),
                        StreamHandler()
                    ])  