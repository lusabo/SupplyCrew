import streamlit as st
import requests
from datetime import date

API_BASE_URL = "http://backend:8000"

st.title("📝 Nova Solicitação de Compra")

# Buscar categorias
try:
    categories_resp = requests.get(f"{API_BASE_URL}/categories")
    categories_resp.raise_for_status()
    categories = categories_resp.json()
    category_options = {cat["description"]: cat["id"] for cat in categories}
except Exception as e:
    st.error(f"Erro ao carregar categorias: {e}")
    st.stop()

# Buscar materiais
try:
    materials_resp = requests.get(f"{API_BASE_URL}/materials")
    materials_resp.raise_for_status()
    materials = materials_resp.json()
    material_options = {mat["description"]: mat["id"] for mat in materials}
except Exception as e:
    st.error(f"Erro ao carregar materiais: {e}")
    st.stop()

with st.form("new_request_form"):
    selected_category = st.selectbox("Categoria", list(category_options.keys()))
    selected_material = st.selectbox("Material", list(material_options.keys()))
    specification = st.text_area("Especificação")
    quantity = st.number_input("Quantidade", min_value=1)
    proposal_deadline = st.date_input("Prazo para proposta", value=date.today())
    delivery_due_date = st.date_input("Data de entrega", value=date.today())

    submitted = st.form_submit_button("Enviar")

if submitted:
    payload = {
        "category_id": category_options[selected_category],
        "material_id": material_options[selected_material],
        "specification": specification,
        "quantity": quantity,
        "proposal_deadline": proposal_deadline.strftime("%Y-%m-%d"),
        "delivery_due_date": delivery_due_date.strftime("%Y-%m-%d"),
    }
    try:
        r = requests.post(f"{API_BASE_URL}/purchase-requests", json=payload)
        r.raise_for_status()
        st.success("✅ Solicitação registrada com sucesso!")

        st.markdown("Redirecionando em 2 segundos...")
        st.markdown("""
            <script>
                setTimeout(function(){
                    window.location.href = "/";
                }, 2000);
            </script>
        """, unsafe_allow_html=True)

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Erro ao registrar: {e}")
