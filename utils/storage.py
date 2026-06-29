from google.cloud import storage
import streamlit as st

BUCKET = "bucket-copa-ana-flavia"

@st.cache_resource
def get_bucket():
    client = storage.Client.from_service_account_json("credenciais.json")
    return client.bucket(BUCKET)


def baixar_imagem(nome_arquivo):
    bucket = get_bucket()

    blob = bucket.blob(f"imagens_jogadores/{nome_arquivo}")

    return blob.download_as_bytes()