import os
from os import environ
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

MODEL_CONFIG_FILE = "config/model.yaml"
SCHEMA_FILE_PATH = "config/schema.yaml"

DB_URL=environ["MONGO_DB_URL"]

TEST_SIZE=0.2