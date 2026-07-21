import streamlit as st
import pandas as pd
import joblib
import os

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ODI High Scorer Predictor",
    page_icon="🏏",
    layout="centered"
)

# ============================================================
# LOAD MODEL AND COLUMNS
# ============================================================

BASE_DIR = os.path.dirname(__file__)

try:
    model = joblib.load(
        os.path.join(BASE_DIR, "odb_high_scorer_model.pkl")
    )

    feature_columns = joblib.load(
        os.path.join(BASE_DIR, "odb_columns.pkl")
    )

except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(135deg, #071a2f, #102d4a);
    }

    .header {
        background: linear-gradient(135deg, #0b5ed7, #00a6fb);
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
    }

    .header h1 {
        color: white !important;
        margin: 0;
    }

    .header p {
        color: white !important;
    }

    .section-title {
        color: white !important;
        font-size: 28px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    label {
        color: white !important;
    }

    input {
        color: black !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="header">
        <h1>🏏 ODI High Scorer Predictor</h1>
        <p>Predict whether a player belongs to the high-scoring category.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# PLAYER STATISTICS
# ============================================================

st.markdown(
    """
    <div class="section-title">
        📊 Player Statistics
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    mat = st.number_input(
        "Matches",
        min_value=0,
        value=200,
        step=1
    )

    inns = st.number_input(
        "Innings",
        min_value=0,
        value=180,
        step=1
    )

    no = st.number_input(
        "Not Outs",
        min_value=0,
        value=20,
        step=1
    )

    hs = st.number_input(
        "Highest Score",
        min_value=0.0,
        value=150.0,
        step=1.0
    )

    ave = st.number_input(
        "Batting Average",
        min_value=0.0,
        value=40.0,
        step=0.1
    )

    bf = st.number_input(
        "Balls Faced",
        min_value=0,
        value=10000,
        step=100
    )

with col2:

    sr = st.number_input(
        "Strike Rate",
        min_value=0.0,
        value=85.0,
        step=0.1
    )

    hundreds = st.number_input(
        "Centuries (100s)",
        min_value=0,
        value=10,
        step=1
    )

    fifties = st.number_input(
        "Fifties (50s)",
        min_value=0,
        value=40,
        step=1
    )

    ducks = st.number_input(
        "Ducks (0s)",
        min_value=0,
        value=5,
        step=1
    )

    fours = st.number_input(
        "Fours (4s)",
        min_value=0.0,
        value=500.0,
        step=1.0
    )

    sixes = st.number_input(
        "Sixes (6s)",
        min_value=0.0,
        value=50.0,
        step=1.0
    )

# ============================================================
# PREDICT BUTTON
# ============================================================

st.markdown("---")

if st.button(
    "🔍 Predict Player Category",
    use_container_width=True
):

    try:

        # Create input DataFrame using the same features
        # that were used during model training.

        input_data = pd.DataFrame(
            [[
                mat,
                inns,
                no,
                hs,
                ave,
                bf,
                sr,
                hundreds,
                fifties,
                ducks,
                fours,
                sixes
            ]],
            columns=feature_columns
        )

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Display result
        if prediction == 1:

            st.success(
                "🏆 High Scorer: "
                "This player belongs to the high-scoring category!"
            )

        else:

            st.info(
                "📊 Regular Scorer: "
                "This player is below the high-scoring category."
            )

    except Exception as e:

        st.error(
            f"⚠️ Prediction failed: {e}"
        )
