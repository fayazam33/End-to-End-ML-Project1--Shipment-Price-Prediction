import os
import sys
import tempfile

import boto3
import dill
import pandas as pd
import streamlit as st
from dotenv import load_dotenv


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


from shipment.components.model_trainer import CostModel



load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET_NAME = os.getenv(
    "S3_BUCKET_NAME",
    "shipment-model-fayaz"
)
S3_MODEL_KEY = os.getenv(
    "S3_MODEL_KEY",
    "shipping_price_model.pkl"
)


st.set_page_config(
    page_title="Shipment Cost Predictor",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>
    /* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0f172a 0%,
        #172554 100%
    );
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: white;
}

/* Sidebar success message */
[data-testid="stSidebar"] .stAlert {
    background-color: rgba(255, 255, 255, 0.10);
    border: 1px solid rgba(255, 255, 255, 0.15);
}

/* Sidebar info message */
[data-testid="stSidebar"] .stAlert {
    border-radius: 12px;
}

/* Divider */
[data-testid="stSidebar"] hr {
    border-color: rgba(255, 255, 255, 0.2);
}

    .main {
        background-color:#cff6ff;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

   .hero {
    padding: 3rem;
    border-radius: 24px;
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e3a8a 55%,
        #2563eb 100%
    );
    color: white;
    margin-bottom: 2rem;
    box-shadow: 0 15px 40px rgba(30, 58, 138, 0.25);
    position: relative;
    overflow: hidden;
}
.hero::after {
    content: "";
    position: absolute;
    width: 250px;
    height: 250px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
    right: -80px;
    top: -100px;
}

.hero h1 {
    font-size: 2.8rem;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 0.7rem;
}

.hero p {
    font-size: 1.15rem;
    color: #dbeafe;
    line-height: 1.6;
    max-width: 700px;
}

.hero-badge {
    display: inline-block;
    padding: 7px 14px;
    margin-bottom: 15px;
    border-radius: 50px;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.2);
    font-size: 0.85rem;
    font-weight: 600;
}

    .prediction-box {
    padding: 2.5rem;
    border-radius: 24px;
    background:  #92EEFF;
    border: 1px solid #bfdbfe;
    box-shadow: 0 15px 40px rgba(37, 99, 235, 0.12);
    text-align: center;
    margin-top: 2rem;
}

    .prediction-value {
        font-size: 3rem;
        font-weight: 700;
        color:#249D8F;
    }
    .prediction-description {
    color: #64748b;
    font-size: 0.95rem;
}

    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

   .info-card {
    padding: 1.5rem;
    border-radius: 18px;
    background: #E3F2FD;
    border: 1px solid #e2e8f0;
    box-shadow: 0 5px 20px rgba(15, 23, 42, 0.05);
    margin-bottom: 1rem;
}

.stFormSubmitButton > button {
    background: #f01f37;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 700;
    transition: all 0.2s ease;
    box-shadow: 0 6px 15px rgba(240, 31, 55, 0.25);
}

.stFormSubmitButton > button:hover {
    background: #1dd890;
    color: Black;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(240, 31, 55, 0.35);
}
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# S3 client
# ---------------------------------------------------------

@st.cache_resource
def get_s3_client():

    return boto3.client(
        "s3",
        region_name=AWS_REGION
    )


# ---------------------------------------------------------
# Download model from S3
# ---------------------------------------------------------

@st.cache_resource
def load_model_from_s3():

    s3 = get_s3_client()

    temp_dir = tempfile.gettempdir()

    model_path = os.path.join(
        temp_dir,
        "shipping_price_model.pkl"
    )

    # Download model from S3
    s3.download_file(
        S3_BUCKET_NAME,
        S3_MODEL_KEY,
        model_path
    )

    # Load pickle
    with open(model_path, "rb") as file:

        model = dill.load(file)

    return model


# ---------------------------------------------------------
# Load model
# ---------------------------------------------------------

try:

    with st.spinner("Loading ML model from AWS S3..."):

        model = load_model_from_s3()

    model_status = True

except Exception as e:

    model_status = False

    st.error(
        "Unable to load the model from AWS S3."
    )

    st.exception(e)


# ---------------------------------------------------------
# Hero section
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero">

        
    <h1>🚚 Shipment Cost Predictor</h1>
        <p>
        Predict the estimated shipment cost using
        a machine learning model 
        </p>

    </div>
    
    
    
    
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.header("⚙️ Model Information")

    st.success("Model loaded from AWS and We Are Ready to Predict")

    st.divider()

    st.info(
        """
        Enter the sculpture and shipment
        information and click **Predict Cost**.
        """
    )


# ---------------------------------------------------------
# Stop if model couldn't load
# ---------------------------------------------------------

if not model_status:

    st.stop()


# ---------------------------------------------------------
# Input section
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">📦 Shipment Information</div>',
    unsafe_allow_html=True
)


with st.form("prediction_form"):

    # -----------------------------------------------------
    # Sculpture information
    # -----------------------------------------------------

    st.subheader("🎨 Sculpture Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        artist_reputation = st.number_input(
            "Artist Reputation",
            min_value=0.0,
            max_value=1.0,
            value=0.50,
            step=0.01
        )

    with col2:

        height = st.number_input(
            "Height",
            min_value=0.0,
            value=20.0,
            step=1.0
        )

    with col3:

        width = st.number_input(
            "Width",
            min_value=0.0,
            value=10.0,
            step=1.0
        )


    col4, col5, col6 = st.columns(3)

    with col4:

        weight = st.number_input(
            "Weight",
            min_value=0.0,
            value=1000.0,
            step=10.0
        )

    with col5:

        material = st.selectbox(
            "Material",
            [
                "Brass",
                "Clay",
                "Aluminium",
                "Wood",
                "Stone",
                "Marble",
                "Bronze"
            ]
        )

    with col6:

        sculpture_price = st.number_input(
            "Price Of Sculpture",
            min_value=0.0,
            value=100.0,
            step=1.0
        )


    # -----------------------------------------------------
    # Shipping information
    # -----------------------------------------------------

    st.divider()

    st.subheader("🚚 Shipping Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        base_shipping_price = st.number_input(
            "Base Shipping Price",
            min_value=0.0,
            value=50.0,
            step=1.0
        )

    with col2:

        international = st.selectbox(
            "International",
            ["Yes", "No"]
        )

    with col3:

        express_shipment = st.selectbox(
            "Express Shipment",
            ["Yes", "No"]
        )


    col4, col5, col6 = st.columns(3)

    with col4:

        installation_included = st.selectbox(
            "Installation Included",
            ["Yes", "No"]
        )

    with col5:

        transport = st.selectbox(
            "Transport",
            [
                "Airways",
                "Roadways",
                "Waterways"
            ]
        )

    with col6:

        fragile = st.selectbox(
            "Fragile",
            ["Yes", "No"]
        )


    # -----------------------------------------------------
    # Customer information
    # -----------------------------------------------------

    st.divider()

    st.subheader("👤 Customer Information")

    col1, col2 = st.columns(2)

    with col1:

        customer_information = st.selectbox(
            "Customer Information",
            [
                "Working Class",
                "Wealthy"
            ]
        )

    with col2:

        remote_location = st.selectbox(
            "Remote Location",
            ["Yes", "No"]
        )


    # -----------------------------------------------------
    # Submit
    # -----------------------------------------------------

    st.divider()

    submitted = st.form_submit_button(
        "Predict the Shipment Cost",
        use_container_width=True
    )


# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

if submitted:

    try:

        # -------------------------------------------------
        # Create DataFrame
        # -------------------------------------------------

        input_data = pd.DataFrame(
            [
                {
                    "Artist Reputation": artist_reputation,
                    "Height": height,
                    "Width": width,
                    "Weight": weight,
                    "Material": material,
                    "Price Of Sculpture": sculpture_price,
                    "Base Shipping Price": base_shipping_price,
                    "International": international,
                    "Express Shipment": express_shipment,
                    "Installation Included": installation_included,
                    "Transport": transport,
                    "Fragile": fragile,
                    "Customer Information": customer_information,
                    "Remote Location": remote_location,
                }
            ]
        )


        # -------------------------------------------------
        # Make prediction
        # -------------------------------------------------

        prediction = model.predict(input_data)

        predicted_cost = float(prediction[0])


        # -------------------------------------------------
        # Display result
        # -------------------------------------------------

        st.markdown(
            f"""
            <div class="prediction-box">

            <h2>💰 Predicted Shipment Cost</h2>

            <div class="prediction-value">
                    ${predicted_cost:,.2f}
            </div>

           

            </div>
            """,
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # Show input data
        # -------------------------------------------------

        st.divider()

        st.subheader("📋 Submitted Information")

        display_data = input_data.T.reset_index()

        display_data.columns = [
            "Feature",
            "Value"
        ]

        st.dataframe(
            display_data,
            use_container_width=True,
            hide_index=True
        )

        st.markdown(
    """
    <div style="text-align:center; margin-top:40px; padding:20px; color:#64748b;">
        Created by <strong>Fayaz Ali Muktadir</strong>
    </div>
    """,
    unsafe_allow_html=True
            )
    except Exception as e:

        st.error(
            "Prediction failed."
        )

        st.exception(e)