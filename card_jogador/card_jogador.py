import streamlit as st
import pandas as pd
from utils.storage import baixar_imagem


def mostrar_jogador(df):

    if df.empty:
        st.warning("Nenhum jogador encontrado para os filtros selecionados.")
        return

    jogador = st.selectbox(
        "Selecione um jogador",
        sorted(df["nome"].unique())
    )

    dados = df[df["nome"] == jogador].iloc[0]

    foto = None
   
    # BAIXAR FOTO DO BUCKET

    if pd.notna(dados["foto_url"]):

        try:
            foto = baixar_imagem(dados["foto_url"])

        except Exception as e:
            st.warning(f"Erro ao carregar imagem: {e}")
  
    # LAYOUT

    col1, col2 = st.columns([1, 2])

    with col1:

        if foto:
            st.image(foto, use_container_width=True)
        else:
            st.info("Imagem indisponível.")

    with col2:

        st.subheader(dados["nome"])

        st.write(f"🌎 **Seleção:** {dados['pais']}")
        st.write(f"🏟 **Clube:** {dados['clube']}")
        st.write(f"📌 **Posição:** {dados['posicao']}")
        st.write(f"🎂 **Idade:** {dados['idade']} anos")

        st.divider()

        k1, k2, k3 = st.columns(3)

        with k1:
            st.metric(
                "⚽ Gols",
                int(dados["gols_clube"])
            )

        with k2:
            st.metric(
                "🎯 Assistências",
                int(dados["assistencias_clube"])
            )

        with k3:
            st.metric(
                "🏃 Partidas",
                int(dados["partidas_clube"])
            )

        st.divider()

        st.markdown("### 📊 Atributos")

        atributos = [
            ("⚡ Ritmo", "ritmo"),
            ("🎯 Finalização", "finalizacao"),
            ("🎨 Passe", "passe"),
            ("🪄 Drible", "drible"),
            ("🛡 Defesa", "defesa"),
            ("💪 Físico", "fisico"),
        ]

        for titulo, coluna in atributos:

            if coluna not in dados.index:
                continue

            valor = float(dados[coluna])

            st.write(f"**{titulo}**")

            st.progress(
                min(valor / 100, 1),
                text=f"{valor:.0f}"
            )