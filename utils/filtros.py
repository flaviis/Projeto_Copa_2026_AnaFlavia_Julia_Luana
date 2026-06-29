import streamlit as st

def aplicar_filtros(df):

    st.sidebar.title("Filtros")

    pais = st.sidebar.selectbox(
        "Seleção",
        ["Todas"] + sorted(df["pais"].unique())
    )

    posicao = st.sidebar.multiselect(
        "Posição",
        sorted(df["posicao"].unique())
    )

    df_filtrado = df.copy()

    if pais != "Todas":
        df_filtrado = df_filtrado[df_filtrado["pais"] == pais]

    if posicao:
        df_filtrado = df_filtrado[df_filtrado["posicao"].isin(posicao)]

    return df_filtrado