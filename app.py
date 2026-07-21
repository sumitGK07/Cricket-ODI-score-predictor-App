import streamlit as st
import pandas as pd
import joblib

# ============================================================

# PAGE CONFIGURATION

# ============================================================

st.set_page_config(
page_title="ODI High Scorer Predictor",
page_icon="🏏",
layout="centered"
)

# ============================================================

# LOAD MODEL AND PREPROCESSING FILES

# ============================================================

model = joblib.load("odb_high_scorer_model.pkl")
feature_columns = joblib.load("odb_columns.pkl")

# ============================================================

# CUSTOM CSS

# ============================================================

st.markdown(
""" <style>

/* Main application background */
.stApp {
    background: linear-gradient(135deg, #071a2f, #102d4a);
}

/* Main header */
.header {
    background: linear-gradient(135deg, #0b5ed7, #00a6fb);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
}

.header h1 {
    color: white !important;
    font-size: 48px;
    margin: 0;
}

.header p {
    color: white !important;
    font-size: 22px;
    margin-top: 20px;
}

/* Section headings */
.section-title {
    color: white !important;
    font-size: 32px;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 20px;
}

/* Input labels */
label {
    color: white !important;
}

/* Prediction result */
.result-box {
    background: #123c28;
    color: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
    font-size: 24px;
    font-weight: bold;
}

/* Button */
.stButton > button {
    width: 100%;
    background-color: #0b5ed7;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 12px;
}

.stButton > button:hover {
    background-color: #084298;
    color: white;
}

</style>
""",
unsafe_allow_html=True

)

# ============================================================

# HEADER

# ============================================================

st.markdown(
""" <div class="header"> <h1>🏏 ODI High Scorer Predictor</h1> <p>Predict whether a player belongs to the high-scoring category.</p> </div>
""",
unsafe_allow_html=True
)

# ============================================================

# PLAYER STATISTICS

# ============================================================

st.markdown(
""" <div class="section-title">
📊 Player Statistics </div>
""",
unsafe_allow_html=True
)

# Create two columns for input fields

col1, col2 = st.columns(2)

with col1:

matches = st.number_input(
    "Matches",
    min_value=0,
    value=200,
    step=1
)

innings = st.number_input(
    "Innings",
    min_value=0,
    value=180,
    step=1
)

not_outs = st.number_input(
    "Not Outs",
    min_value=0,
    value=20,
    step=1
)


with col2:


strike_rate = st.number_input(
    "Strike Rate",
    min_value=0.0,
    value=85.0,
    step=0.1
)

centuries = st.number_input(
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


# ============================================================

# PREDICTION BUTTON

# ============================================================

st.markdown("---")

if st.button("🔮 Predict High Scorer"):


try:

    # Create DataFrame from user input
    input_data = pd.DataFrame(
        {
            "matches": [matches],
            "innings": [innings],
            "not_outs": [not_outs],
            "strike_rate": [strike_rate],
            "centuries": [centuries],
            "fifties": [fifties]
        }
    )

    # Make sure input columns match the columns used during training
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 1:

        st.markdown(
            """
            <div class="result-box">
                🏆 This player belongs to the HIGH-SCORING category!
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="result-box">
                📊 This player does NOT belong to the high-scoring category.
            </div>
            """,
            unsafe_allow_html=True
        )

except Exception as e:

    st.error(f"⚠️ Prediction failed: {e}")
