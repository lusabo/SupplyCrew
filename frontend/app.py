import streamlit as st

st.set_page_config(page_title="SupplyCrew", layout="wide")

from pages import list_request

# Sidebar com link apenas para listagem
tabs = {"Solicitações de Compra": list_request.render}

st.sidebar.title("SupplyCrew")
selected_page = st.sidebar.radio("Ir para:", list(tabs.keys()))

# Página inicial com mensagem de boas-vindas, sem conteúdo adicional
if selected_page:
    tabs[selected_page]()
