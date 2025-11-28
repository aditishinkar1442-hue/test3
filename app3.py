import streamlit as st
import pandas as pd

# ------------------ UI SETUP ------------------
st.set_page_config(
    page_title="USD/INR Option Chain",
    page_icon="💱",
    layout="wide",
)

st.markdown("""
    <h1 style='text-align:center; color:#2E86C1;'>💱 USD/INR Forex Option Chain</h1>
    <p style='text-align:center; font-size:18px;'>
        Realistic sample option chain for USD/INR with clean UI and smooth experience.
    </p>
""", unsafe_allow_html=True)

st.divider()

# ------------------ SAMPLE OPTION CHAIN DATA ------------------
# You can replace this with real API later

data = {
    "Strike Price": [82.00, 82.25, 82.50, 82.75, 83.00],
    "CALL OI": [120000, 150000, 180000, 160000, 110000],
    "CALL LTP": [0.4500, 0.3800, 0.2900, 0.2100, 0.1500],
    "CALL Change %": [+1.2, -0.5, +2.1, -1.8, +0.3],

    "PUT OI": [90000, 130000, 175000, 140000, 100000],
    "PUT LTP": [0.3000, 0.3500, 0.4200, 0.5100, 0.6300],
    "PUT Change %": [-0.7, +1.5, +2.0, +1.2, +3.5],
}

df = pd.DataFrame(data)

# ------------------ FILTER AREA ------------------
st.subheader("🔍 Filters")

col1, col2 = st.columns(2)

strike_filter = col1.selectbox(
    "Select Strike Price",
    options=["All"] + df["Strike Price"].astype(str).tolist(),
)

option_type = col2.selectbox(
    "Select Option Type",
    ["All", "CALL", "PUT"]
)

# ------------------ APPLY FILTERS ------------------
filtered_df = df.copy()

if strike_filter != "All":
    filtered_df = filtered_df[filtered_df["Strike Price"] == float(strike_filter)]

if option_type == "CALL":
    filtered_df = filtered_df[["Strike Price", "CALL OI", "CALL LTP", "CALL Change %"]]
elif option_type == "PUT":
    filtered_df = filtered_df[["Strike Price", "PUT OI", "PUT LTP", "PUT Change %"]]

# ------------------ DISPLAY TABLE ------------------
st.subheader("📊 Option Chain Data")

st.dataframe(filtered_df, use_container_width=True)

# ------------------ FOOTER ------------------
st.markdown("""
    <p style='text-align:center; margin-top:40px; color:gray;'>
        Forex USD/INR Option Chain • Built with Streamlit • Clean UI/UX
    </p>
""", unsafe_allow_html=True)
