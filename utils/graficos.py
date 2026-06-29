import streamlit as st
import plotly.express as px
import pandas as pd


# 1 - Jogadores por posição

def grafico_posicoes(df):

    dados = (
        df.groupby("posicao")
        .size()
        .reset_index(name="Quantidade")
    )

    fig = px.bar(
        dados,
        x="posicao",
        y="Quantidade",
        title="Jogadores por Posição"
    )

    st.plotly_chart(fig, use_container_width=True)


# 2 - Top 10 Artilheiros

def grafico_top_gols(df):

    top = (
        df.sort_values("gols_clube", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top,
        x="gols_clube",
        y="nome",
        orientation="h",
        title="Top 10 Artilheiros"
    )

    st.plotly_chart(fig, use_container_width=True)

# 3 - Top Assistências

def grafico_top_assistencias(df):

    top = (
        df.sort_values("assistencias_clube", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top,
        x="assistencias_clube",
        y="nome",
        orientation="h",
        title="Top 10 Assistências"
    )

    st.plotly_chart(fig, use_container_width=True)

# 4 - Histograma de Idade

def grafico_idades(df):

    fig = px.histogram(
        df,
        x="idade",
        nbins=10,
        title="Distribuição das Idades"
    )

    st.plotly_chart(fig, use_container_width=True)


# 5 - Clubes com mais jogadores

def grafico_clubes(df):

    clubes = (
        df.groupby("clube")
        .size()
        .reset_index(name="Quantidade")
        .sort_values("Quantidade", ascending=False)
        .head(10)
    )

    fig = px.bar(
        clubes,
        x="clube",
        y="Quantidade",
        title="Clubes com Mais Jogadores"
    )

    st.plotly_chart(fig, use_container_width=True)


# 6 - Média dos atributos

def grafico_atributos(df):

    atributos = [
        "ritmo",
        "finalizacao",
        "passe",
        "drible",
        "defesa",
        "fisico"
    ]

    existentes = [c for c in atributos if c in df.columns]

    if not existentes:
        st.warning("Nenhuma coluna de atributos encontrada.")
        return

    medias = (
        df[existentes]
        .mean()
        .reset_index()
    )

    medias.columns = ["Atributo", "Média"]

    fig = px.bar(
        medias,
        x="Atributo",
        y="Média",
        title="Média dos Atributos dos Jogadores"
    )

    st.plotly_chart(fig, use_container_width=True)