import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://backend:8000"

def render():
    st.title("📋 Solicitações de Compra")

    if st.button("➕ Nova Solicitação"):
        st.switch_page("pages/form_request.py")

    # Funções auxiliares para obter mapeamentos
    def get_mapping(endpoint):
        try:
            response = requests.get(f"{API_BASE_URL}/{endpoint}")
            response.raise_for_status()
            data = response.json()
            return {item["id"]: item["description"] for item in data}
        except Exception as e:
            st.error(f"Erro ao carregar {endpoint}: {e}")
            return {}

    # Obter mapeamentos
    category_map = get_mapping("categories")
    material_map = get_mapping("materials")

    # Buscar solicitações
    try:
        response = requests.get(f"{API_BASE_URL}/purchase-requests")
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        st.error(f"Erro ao buscar solicitações: {e}")
        st.stop()

    # Substituir IDs por descrições
    for item in data:
        item["Categoria"] = category_map.get(item["category_id"], f"ID {item['category_id']}")
        item["Material"] = material_map.get(item["material_id"], f"ID {item['material_id']}")

    # Construir DataFrame
    df = pd.DataFrame(data)
    df = df[["id", "Categoria", "Material", "specification", "quantity", "proposal_deadline", "delivery_due_date"]]
    df.columns = ["ID", "Categoria", "Material", "Especificação", "Quantidade", "Prazo para Proposta", "Entrega"]

    # Exibir tabela
    if df.empty:
        st.warning("Nenhuma solicitação cadastrada.")
    else:
        st.dataframe(df, use_container_width=True)
