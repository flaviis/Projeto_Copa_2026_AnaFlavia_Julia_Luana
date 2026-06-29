from google.cloud import storage
from google.oauth2 import service_account
import streamlit as st

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

client = storage.Client(
    credentials=credentials,
    project=credentials.project_id,
)