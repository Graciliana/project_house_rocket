import pandas as pd
import streamlit as st

# função carregar o dataset
@st.cache_resource
def loads_dataset() -> pd.DataFrame:
    return pd.read_csv(
        "dataset/kc_house_data.csv"
    )
