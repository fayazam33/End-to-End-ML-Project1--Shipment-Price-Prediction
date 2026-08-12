# End-to-End-ML-Project1--Shipment-Price-Prediction

The project is built using the **HackerEarth Machine Learning:Exhibit A(rt)** dataset, available through Kaggle.

## Dataset

This project uses the following publicly available dataset:

**HackerEarth Machine Learning: Exhibit A(rt)**

🔗 Dataset:
https://www.kaggle.com/datasets/oossiiris/hackerearth-machine-learning-exhibit-art

How to run
Before you run this project make sure you have MongoDB Atlas account and you have the shipping dataset into it.

Step 1. Cloning the repository.

```
git clone https://github.com/fayazam33/End-to-End-ML-Project1--Shipment-Price-Prediction.git
```

Step 2. Create a conda environment.


```
conda create -n shipment python=3.11 -y
```
```
conda activate shipment
```


Step 3. Install the requirements

```
pip install -r requirements.txt
```


The dataset contains information related to sculptures and their
shipment characteristics. The features used in this project include
attributes such as:

- Artist Reputation
- Height
- Width
- Weight
- Material
- Price of Sculpture
- Base Shipping Price
- International Shipping
- Express Shipment
- Installation Included
- Transport
- Fragile
- Customer Information
- Remote Location

The dataset is used as the foundation for developing and evaluating
the shipment cost prediction model.

> **Dataset Attribution:** The original dataset is provided by its
> respective author on Kaggle. This repository contains my own
> implementation, preprocessing, model development, deployment, and
> application interface built using the dataset.

## 🎯 Project Objective

The objective of this project is to develop a machine learning
regression system capable of estimating the shipment cost of a
sculpture from its available characteristics and shipping information.

The trained model is integrated into an interactive Streamlit
application where users can enter shipment information and receive
an estimated shipment cost.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- CatBoost
- Matplotlib
- Seaborn
- MongoDB
- AWS S3
- Streamlit
- Dill

## 🔄 Project Workflow

Dataset

↓

Data Ingestion

↓

Data Validation

↓

Data Transformation

↓

Feature Engineering

↓

Model Training

↓

Model Evaluation

↓

AWS S3 Model Storage

↓

Streamlit Application

↓

Shipment Cost Prediction

## ☁️ Deployment

The trained machine learning model is stored in **AWS S3** and
loaded by the Streamlit application at runtime.

MongoDB is used as part of the project's data/metadata pipeline,
while Streamlit provides the interactive prediction interface.
```
END-TO-END-ML-PROJECT1--SHIPMENT-PRICE-PREDICTION/
│
├── api/                         # API-related files
│
├── artifacts/                   # Generated ML artifacts
│
├── catboost_info/               # CatBoost training information
│
├── config/                      # Project configuration files
│
├── data/                        # Dataset and data-related files
│
├── DataTransformationArtifacts/ # Data transformation outputs
│
├── log/                         # Application and pipeline logs
│
├── notebooks/                   # Jupyter notebooks for analysis and experimentation
│   ├── 1._EDA_Shipment-Pricing-Prediction.ipynb
│   └── 2._Feature_Engineering_Model_Shipment-Pricing-Prediction.ipynb
│
├── shipment/                    # Main ML pipeline package
│   ├── components/              # Data ingestion, transformation, model training, etc.
│   ├── constants/               # Project constants
│   ├── entity/                   # Configuration and artifact entities
│   └── ...
│
├── test/                        # Test files
│
├── .dockerignore                # Docker ignore configuration
├── .env                         # Environment variables (not committed to GitHub)
├── .gitignore                   # Git ignore configuration
│
├── app.py                       # Application entry point
├── demo.py                      # Demo/testing application
├── Dockerfile                   # Docker configuration
│
├── LICENSE                      # Project license
├── README.md                    # Project documentation
├── requirements.txt             # Production dependencies
├── requirements_dev.txt         # Development dependencies
├── setup.py                     # Python package configuration
│
├── shipping_price_model.pkl     # Trained shipment price prediction model
│
├── streamlit_app.py             # Streamlit web application
├── template.py                  # Project template/setup utility
│
└── shipment.egg-info/           # Python package metadata
```
## 🚀 Live Application

👉 My Streamlit application URL here:

https://shipment-cost-prediction-with-fayaz.streamlit.app/

## 👨‍💻 Author

## **Fayaz Ali Muktadir**

This project was developed as an end-to-end machine learning
implementation to practice data preprocessing, feature engineering,
model training, cloud-based model storage, and ML application
deployment.
