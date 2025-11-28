import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta

# ------------------- APP CONFIG -------------------
st.set_page_config(
    page_title="USD/INR Option Chain",
    page_icon="💱",
    layout="wide",
)

# ------------------- HEADER -------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#3b82f6;'>💱 USD/INR Forex Option Chain</h1>
    <p style='text-align:center; font-size:18px;'>Live-style option chain interface for USD/INR Forex Market</p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ------------------- SIDEBAR -------------------
st.sidebar.header("⚙️ Settings")
spot_price = st.sidebar.number_input("USD/INR Spot Price", value=83.20, step=0.01)

expiry_date = st.sidebar.date_input(
    "Select Expiry",
    value=date.today() + timedelta(days=30)
)

st.sidebar.markdown("---")
st.sidebar.write("📌 *This is a simulated option chain for demonstration.*")

# ------------------- GENERATE DUMMY OPTION CHAIN -------------------
def generate_option_chain(spot):
    strikes = np.arange(spot - 3, spot + 3.5, 0.5).round(2)
    data = []

    for strike in strikes:
        call_price = max(0, spot - strike) + np.random.uniform(0.10, 0.40)
        put_price = max(0, strike - spot) + np.random.uniform(0.10, 0.40)

        data.append([
            round(call_price, 2),
            round(np.random.uniform(100, 900)),  # Call OI
            round(np.random.uniform(-200, 200)), # Call change OI
            strike,
            round(put_price, 2),
            round(np.random.uniform(100, 900)),  # Put OI
            round(np.random.uniform(-200, 200)), # Put change OI
        ])

    df = pd.DataFrame(data, columns=[
        "CALL LTP",
        "CALL OI",
        "CALL Chg OI",
        "STRIKE",
        "PUT LTP",
        "PUT OI",
        "PUT Chg OI"
    ])
    return df

chain_df = generate_option_chain(spot_price)

# ------------------- OPTION CHAIN TABLE -------------------
st.markdown(
    """
    <h3 style='color:#10b981;'>📊 USD/INR Option Chain Table</h3>
    """,
    unsafe_allow_html=True
)

st.dataframe(
    chain_df.style.back_
