# Connect to S3
# Download your .pkl
# Load the model
# Return the model

import os
import boto3
import dill

from dotenv import load_dotenv

load_dotenv()


S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_MODEL_NAME = os.getenv("S3_MODEL_NAME")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION")

LOCAL_MODEL_PATH = "shipping_price_model.pkl"


def load_model_from_s3():

    print("Downloading model from S3...")

    s3 = boto3.client(
        "s3",
        region_name=AWS_REGION
    )

    # Download model
    s3.download_file(
        S3_BUCKET_NAME,
        S3_MODEL_NAME,
        LOCAL_MODEL_PATH
    )

    print("Model downloaded successfully.")

    # Load pickle model
    with open(LOCAL_MODEL_PATH, "rb") as file:
        model = dill.load(file)

    print("Model loaded successfully.")

    return model