import streamlit as st
import pandas as pd
import numpy as np
from math import log, sqrt, exp
from scipy.stats import norm

# ---------------------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------------------
st.set_page_config(page_title="Forex Options (USD/INR)", page_icon="💱", layout="wide")

st.title("💱 USD/INR Forex Options Suite")
st.write("Option Chain + Option Calculator for USD/INR Forex Market")

# ---------------------------------------------------------------------
# BLACK–SCHOLES OPTION FUNCTIONS
# ---------------------------------------------------------------------
def black_scholes_call(S, K, r, sigma, T):
    d1 = (log(S/K) + (r + 0.5*sigma*sigma)*T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    call = S * norm.cdf(d1) - K * exp(-r*T) * norm.cdf(d2)
    return call

def black_scholes_put(S, K, r, sigma, T):
    d1 = (log(S/K) + (r + 0.5*sigma*sigma)*T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    put = K * exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put

# ---------------------------------------------------------------------
# OPTION CHAIN GENERATOR
# ---------------------------------------------------------------------
def generate_option_chain(spot, r, sigma, T):
    strikes = np.arange(spot - 5, spot + 5.5, 0.5)
    calls = []
    puts = []

    for K in strikes:
        calls.append(black_scholes_call(spot, K, r, sigma, T))
        puts.append(black_scholes_put(spot, K, r, sigma, T))

    df = pd.DataFrame({
        "Strike": strikes,
        "Call Price": np.round(calls, 4),
        "Put Price": np.round(puts, 4)
    })
    return df

# ---------------------------------------------------------------------
# USER INPUTS
# ---------------------------------------------------------------------

st.subheader("📌 Input Parameters")

col1, col2, col3, col4 = st.columns(4)

spot = col1.number_input("💲 USD/INR Spot Price", min_value=60.0, max_value=90.0, value=83.00)
future_price = col2.number_input("📈 Future Price (USD/INR)", min_value=60.0, max_value=90.0, value=83.50)
sigma = col3.number_input("📉 Implied Volatility (%)", min_value=1.0, value=6.0) / 100
T = col4.number_input("⏳ Time to Expiry (Years)", min_value=0.01, max_value=1.0, value=0.08)

r = 0.06  # interest rate fixed

# ---------------------------------------------------------------------
# OPTION CHAIN DISPLAY
# ---------------------------------------------------------------------
st.subheader("📊 USD/INR Option Chain")

df_chain = generate_option_chain(spot, r, sigma, T)

st.dataframe(df_chain, use_container_width=True)

# ---------------------------------------------------------------------
# OPTION CALCULATOR
# ---------------------------------------------------------------------
st.subheader("🧮 Option Price Calculator")

col5, col6, col7 = st.columns(3)

calc_spot = col5.number_input("Spot Price", value=spot)
calc_strike = col6.number_input("Strike Price", value=83.0)
calc_vol = col7.number_input("Volatility (%)", value=6.0) / 100

call_price = black_scholes_call(calc_spot, calc_strike, r, calc_vol, T)
put_price = black_scholes_put(calc_spot, calc_strike, r, calc_vol, T)

st.success(f"Call Price: {call_price:.4f}")
st.info(f"Put Price: {put_price:.4f}")

