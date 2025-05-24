import streamlit as st
import requests

API_BASE_URL = "http://backend:8000"

def render():
    st.title("Solicitações de Compra")
    st.markdown("### Listagem de Solicitações")

    # Listar todas as solicitações
    try:
        response = requests.get(f"{API_BASE_URL}/purchase-requests")
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
        return

    if not data:
        st.warning("Nenhuma solicitação cadastrada.")
    else:
        for request in data:
            with st.expander(f"Solicitação #{request['id']}"):
                st.write(f"Categoria ID: {request['category_id']}")
                st.write(f"Material ID: {request['material_id']}")
                st.write(f"Quantidade: {request['quantity']}")
                st.write(f"Prazo para proposta: {request['proposal_deadline']}")
                st.write(f"Data limite de entrega: {request['delivery_due_date']}")

    st.markdown("---")
    st.markdown("### Nova Solicitação")
    with st.form("new_request_form"):
        category_id = st.number_input("Categoria ID", min_value=1)
        material_id = st.number_input("Material ID", min_value=1)
        specification = st.text_area("Especificação")
        quantity = st.number_input("Quantidade", min_value=1)
        proposal_deadline = st.date_input("Prazo para proposta")
        delivery_due_date = st.date_input("Data de entrega")

        submitted = st.form_submit_button("Enviar")

        if submitted:
            payload = {
                "category_id": category_id,
                "material_id": material_id,
                "specification": specification,
                "quantity": quantity,
                "proposal_deadline": proposal_deadline.strftime("%d/%m/%Y"),
                "delivery_due_date": delivery_due_date.strftime("%d/%m/%Y"),
            }
            try:
                r = requests.post(f"{API_BASE_URL}/purchase-requests", json=payload)
                r.raise_for_status()
                st.success("Solicitação registrada com sucesso!")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Erro ao registrar: {e}")
