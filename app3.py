import streamlit as st
import pandas as pd
import numpy as np
from math import log, sqrt, exp
from scipy.stats import norm

st.set_page_config(page_title="Forex Options App", page_icon="💹", layout="wide")

# --------------------------- UI HEADER --------------------------- #
st.markdown(
    """
    <h1 style='text-align:center; color:#3A6EA5;'>💹 USD/INR Forex Options App</h1>
    <h3 style='text-align:center; color:gray;'>Option Chain + Option Calculator</h3>
    <br>
    """,
    unsafe_allow_html=True
)

# --------------------------- SAMPLE OPTION CHAIN --------------------------- #
st.subheader("📘 USD/INR Option Chain (Sample Live-Style Data)")

# Generate sample data
strikes = np.arange(82, 86.5, 0.5)
calls_ltp = np.random.uniform(0.10, 1.20, len(strikes))
puts_ltp = np.random.uniform(0.10, 1.20, len(strikes))

df_chain = pd.DataFrame({
    "Strike": strikes,
    "Call LTP": np.round(calls_ltp, 2),
    "Put LTP": np.round(puts_ltp, 2),
    "Call OI": np.random.randint(1000, 8000, len(strikes)),
    "Put OI": np.random.randint(1000, 8000, len(strikes)),
})

st.dataframe(df_chain, use_container_width=True)

st.markdown("---")

# --------------------------- OPTION CALCULATOR --------------------------- #
st.subheader("🧮 Forex Option Calculator (Black–Scholes Model)")

col1, col2, col3 = st.columns(3)

with col1:
    S = st.number_input("💵 Future Price (USD/INR)", min_value=1.0, value=83.0)

with col2:
    K = st.number_input("🎯 Strike Price", min_value=1.0, value=83.5)

with col3:
    T = st.number_input("⏳ Time to Expiry (Years)", min_v
