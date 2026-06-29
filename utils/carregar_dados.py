import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados():
    df = pd.read_csv("dados/jogadores_selecoes_.csv")
    return df