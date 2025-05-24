import streamlit as st
from pages import purchase_requests  # módulo com a funcionalidade

st.set_page_config(page_title="SupplyCrew", layout="wide")

# Sidebar com navegação
st.sidebar.title("SupplyCrew")
page = st.sidebar.radio("Navegação", ["Início", "Solicitações de Compra"])

# Página inicial
if page == "Início":
    st.title("Bem-vindo ao SupplyCrew 🎯")
    st.markdown("Este é o painel inicial da plataforma de gestão de compras.")
    st.info("Use o menu à esquerda para acessar as funcionalidades disponíveis.")

# Página de manutenção de solicitações
elif page == "Solicitações de Compra":
    purchase_requests.render()
