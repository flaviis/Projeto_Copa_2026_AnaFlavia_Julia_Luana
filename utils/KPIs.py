import streamlit as st
import pandas as pd


def mostrar_kpis(df):
    """
    Exibe os principais indicadores do dashboard.
    """

    total_jogadores = len(df)

    # Idade média
    if "idade" in df.columns:
        idade_media = round(pd.to_numeric(df["idade"], errors="coerce").mean(), 1)
    else:
        idade_media = 0

    # Total de gols
    if "gols" in df.columns:
        total_gols = int(pd.to_numeric(df["gols"], errors="coerce").fillna(0).sum())
    elif "gols_clube" in df.columns:
        total_gols = int(pd.to_numeric(df["gols_clube"], errors="coerce").fillna(0).sum())
    else:
        total_gols = 0

    # Total de assistências
    if "assistencias" in df.columns:
        total_assistencias = int(
            pd.to_numeric(df["assistencias"], errors="coerce").fillna(0).sum()
        )
    elif "assistencias_clube" in df.columns:
        total_assistencias = int(
            pd.to_numeric(df["assistencias_clube"], errors="coerce").fillna(0).sum()
        )
    else:
        total_assistencias = 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="👥 Jogadores",
            value=total_jogadores
        )

    with col2:
        st.metric(
            label="🎂 Idade Média",
            value=f"{idade_media:.1f}"
        )

    with col3:
        st.metric(
            label="⚽ Gols",
            value=total_gols
        )

    with col4:
        st.metric(
            label="🎯 Assistências",
            value=total_assistencias
        )