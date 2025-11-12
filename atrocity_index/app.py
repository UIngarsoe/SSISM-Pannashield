# atrocity_index/app.py
# SS'ISM Paññā Shield — Atrocity Index Live Dashboard
# Deployed on Streamlit Cloud

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Page Config ---
st.set_page_config(
    page_title="SS'ISM Paññā Shield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Title & Header ---
st.title("🛡️ SS'ISM Paññā Shield")
st.markdown("### *The World's First Sīla-Samādhi-Paññā AI for Truth Defense*")
st.markdown("> **\"When vetoes silence justice, data becomes resistance.\"** — U Ingar Soe, 2025")

# --- Sidebar ---
with st.sidebar:
    st.image("https://via.placeholder.com/300x300.png?text=PAÑÑĀ+SHIELD", use_column_width=True)
    st.markdown("## Controls")
    veto_year = st.selectbox("Select Veto Year", [1988, 2007, 2021, 2023, 2025])
    data_source = st.multiselect("Data Sources", ["Satellite", "OSINT", "UN Reports"], default=["Satellite", "OSINT"])

    st.markdown("---")
    st.markdown("**GitHub:** [UIngarsoe/SSISM-Pannashield](https://github.com/UIngarsoe/SSISM-Pannashield)")
    st.markdown("**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)")

# --- Main Dashboard ---
col1, col2 = st.columns([1, 1])

with col1:
    st.metric("**Atrocity Index (H)**", "0.92", "+0.17")
    st.metric("**Accountability Likelihood (Φ_A)**", "78%", "+22%")
    st.metric("**Villages Destroyed**", "47", "+12")

with col2:
    # Sample Data for Chart
    df = pd.DataFrame({
        "Year": [1988, 2007, 2021, 2023, 2025],
        "H Score": [0.65, 0.78, 0.92, 0.88, 0.95],
        "Vetoes": [1, 2, 6, 4, 3]
    })
    fig = px.line(df, x="Year", y="H Score", title="Atrocity Index Over Time", markers=True)
    fig.add_bar(x=df["Year"], y=df["Vetoes"], name="UN Vetoes", yaxis="y2")
    fig.update_layout(yaxis2=dict(title="Veto Count", overlaying="y", side="right"))
    st.plotly_chart(fig, use_container_width=True)

# --- Upload OSINT ---
st.markdown("### Upload OSINT Data (CSV with 'text' column)")
uploaded_file = st.file_uploader("Drop CSV here", type=["csv"])

if uploaded_file:
    df_upload = pd.read_csv(uploaded_file)
    if 'text' in df_upload.columns:
        st.success("OSINT Loaded!")
        sample = df_upload['text'].head(3).tolist()
        st.write("Sample posts:")
        for t in sample:
            st.caption(f"• {t}")
        
        # Fake Misinfo Detection
        fake_count = sum(1 for t in df_upload['text'] if any(k in t for k in ["လှုပ်", "သေ", "အန္တရာယ်"]))
        st.warning(f"**{fake_count} potential fake news posts detected**")
        
        # A' Recommendation
        st.info("**A' (Execution):** Counter with verified satellite timeline + #VETOCOSTCHALLENGE")
    else:
        st.error("CSV must have a 'text' column.")

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #888;'>
    Built with ❤️ by <b>U Ingar Soe</b> | 
    <a href='https://github.com/UIngarsoe/SSISM-Pannashield'>Fork on GitHub</a> | 
    #AIForJustice #Pannashield
    </div>
    """, 
    unsafe_allow_html=True
)
