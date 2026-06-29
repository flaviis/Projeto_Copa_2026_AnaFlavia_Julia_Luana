import streamlit as st
from card_jogador.card_jogador import mostrar_jogador

from utils.carregar_dados import carregar_dados
from utils.filtros import aplicar_filtros
from utils.KPIs import mostrar_kpis

from utils.graficos import (
    grafico_posicoes,
    grafico_top_gols,
    grafico_top_assistencias,
    grafico_idades,
    grafico_clubes,
    grafico_atributos,
)

# CONFIGURAÇÃO DA PÁGINA

st.set_page_config(
    page_title="Dashboard Copa do Mundo",
    page_icon="🏆",
    layout="wide"
)


# TÍTULO

st.title("🏆 Dashboard Copa do Mundo")
st.markdown("### Análise Estatística dos Jogadores das Seleções")


# =====================================================
# CARREGAR DADOS
# =====================================================

df = carregar_dados()


# =====================================================
# FILTROS
# =====================================================

df_filtrado = aplicar_filtros(df)


# =====================================================
# KPIs
# =====================================================

mostrar_kpis(df_filtrado)

st.divider()


# =====================================================
# PRIMEIRA LINHA
# =====================================================

col1, col2 = st.columns(2)

with col1:
    grafico_posicoes(df_filtrado)

with col2:
    grafico_top_gols(df_filtrado)


# =====================================================
# SEGUNDA LINHA
# =====================================================

col3, col4 = st.columns(2)

with col3:
    grafico_top_assistencias(df_filtrado)

with col4:
    grafico_idades(df_filtrado)


# =====================================================
# TERCEIRA LINHA
# =====================================================

col5, col6 = st.columns(2)

with col5:
    grafico_clubes(df_filtrado)

with col6:
    grafico_atributos(df_filtrado)


st.divider()


# =====================================================
# CARD DO JOGADOR
# =====================================================

st.subheader("👤 Perfil do Jogador")

mostrar_jogador(df_filtrado)


# =====================================================
# RODAPÉ
# =====================================================

st.markdown("---")
st.caption("Projeto Final - Banco de Dados II | IFNMG - Campus Almenara")