# =============================================================================
# Cricket ODI High Scorer Predictor
# =============================================================================

import streamlit as st
import pandas as pd
import joblib

model = joblib.load("odb_high_scorer_model.pkl")
feature_columns = joblib.load("odb_columns.pkl")

st.set_page_config(
    page_title="ODI High Scorer Predictor",
    page_icon="🏏",
    layout="centered"
)


# =============================================================================
# Custom CSS Styling
# =============================================================================

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
        margin: 0;
    }

    .result {
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        background: #123c28;
        color: white;
        margin-top: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

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
        margin: 0;
    }

    .result {
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        background: #123c28;
        color: white;
        margin-top: 20px;
    }

    /* Make section headings white */
    h2 {
        color: white !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.subheader("📊 Player Statistics")

col1, col2 = st.columns(2)


with col1:

    mat = st.number_input(
        "Matches",
        min_value=0,
        value=200
    )

    inns = st.number_input(
        "Innings",
        min_value=0,
        value=180
    )

    no = st.number_input(
        "Not Outs",
        min_value=0,
        value=20
    )

    hs = st.number_input(
        "Highest Score",
        min_value=0.0,
        value=150.0
    )

    ave = st.number_input(
        "Batting Average",
        min_value=0.0,
        value=40.0
    )

    bf = st.number_input(
        "Balls Faced",
        min_value=0,
        value=10000
    )


with col2:

    sr = st.number_input(
        "Strike Rate",
        min_value=0.0,
        value=85.0
    )

    hundreds = st.number_input(
        "Centuries (100s)",
        min_value=0,
        value=10
    )

    fifties = st.number_input(
        "Fifties (50s)",
        min_value=0,
        value=40
    )

    ducks = st.number_input(
        "Ducks (0s)",
        min_value=0,
        value=5
    )

    fours = st.number_input(
        "Fours (4s)",
        min_value=0.0,
        value=500.0
    )

    sixes = st.number_input(
        "Sixes (6s)",
        min_value=0.0,
        value=50.0
    )

st.markdown("---")

if st.button(
    "🔍 Predict Player Category",
    use_container_width=True
):

    try:

        # =============================================================================
        # prepare input data for prediction
        # =============================================================================

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


        # =============================================================================
        # prepare input data for prediction
        # =============================================================================

        prediction = model.predict(input_data)[0]


        # =============================================================================
        # display result
        # =============================================================================

        if prediction == 1:

            st.markdown(
                """
                <div class="result">
                    <h2>🏆 High Scorer</h2>
                    <p>This player belongs to the high-scoring category.</p>
                </div>
                """,
                unsafe_allow_html=True
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
