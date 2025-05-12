# import
import streamlit as st

from app.utils.loads_dataset import loads_dataset
# layout page
# ============
st.set_page_config(
    page_title="Dashboard - House Rocket", page_icon="🏂", layout="wide"
)
# Inject custom CSS to change the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;  /* Replace with your desired color */
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Introduction page
# ===================
st.markdown(
    "<h1 style='text-align: center; color: #0F0FD1;'>Project House Rocket</h1>",
    unsafe_allow_html=True,
)

# carregar os dados
st.header("📂 Dataset")
df = loads_dataset()
# Exibir os primeiros dados
st.dataframe(df.head())