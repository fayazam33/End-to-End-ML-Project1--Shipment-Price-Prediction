import os
from os import environ
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR=os.path.join(os.getcwd(),"artifacts",TIMESTAMP)

MODEL_CONFIG_FILE = "config/model.yaml"
SCHEMA_FILE_PATH = "config/schema.yaml"

DB_URL=environ["MONGO_DB_URL"]

TEST_SIZE=0.2
DB_NAME="ShipmentDB"
COLLECTION_NAME="ShipmentCollection"

DATA_INGESTION_ARTIFACTS_DIR="DataIngestionAritfacts"
DATA_INGESTION_TRAIN_DIR="Train"
DATA_INGESTION_TEST_DIR="Test"
DATA_INGESTION_TRAIN_FILE_NAME="train.csv"
DATA_INGESTION_TEST_FILE_NAME="test.csv"

#data validation related constants
DATA_VALIDATION_ARTIFACT_DIR="DataValidationArtifacts"
DATA_DRIFT_FILE_NAME="DataDriftReport.yaml"

#data transformation 
DATA_TRANSFORMATION_ARTIFACTS_DIR="DataTransformationArtifacts"
TRANSFORMED_TRAIN_DATA_DIR="TransformedTrain"
TRANSFORMED_TEST_DATA_DIR="TransformedTest"
TRANSFORMED_TRAIN_DATA_FILE_NAME="transformed_train_data.npz" #npz is the numpy compressed file format
TRANSFORMED_TEST_DATA_FILE_NAME="transformed_test_data.npz"
PREPROCESSOR_OBJECT_FILE_NAME="shipping_preprocessor.pkl"#ভবিষ্যতে নতুন data একইভাবে transform করার জন্য

MODEL_TRAINER_ARTIFACTS_DIR="ModelTrainerArtifacts"
MODEL_FILE_NAME="shipping_price_model.pkl"
MODEL_SAVE_FORMAT=".pkl"

BUCKET_NAME="shipment-model-fayaz"
S3_MODEL_NAME= "shipping_price_model.pkl"
TARGET_COLUMN = "Cost"
