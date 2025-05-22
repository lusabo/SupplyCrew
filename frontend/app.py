import streamlit as st
import datetime
import requests

BACKEND_URL = "http://backend:8000"  # use http://localhost:8000 fora do Docker

st.set_page_config(page_title="Cadastro de Pedidos", page_icon="📦")
st.title("📦 Cadastro de Pedido de Compra")

st.markdown("Preencha os campos abaixo para um ou mais itens de compra. Você pode adicionar quantos quiser antes de enviar.")

# Cache com TTL curto para evitar chamadas repetidas
@st.cache_data(ttl=60)
def get_categories():
    try:
        res = requests.get(f"{BACKEND_URL}/categories/")
        res.raise_for_status()
        return {c["id"]: c["description"] for c in res.json()}
    except Exception as e:
        st.error(f"Erro ao carregar categorias: {e}")
        return {}

@st.cache_data(ttl=60)
def get_materials():
    try:
        res = requests.get(f"{BACKEND_URL}/materials/")
        res.raise_for_status()
        return {m["id"]: m["description"] for m in res.json()}
    except Exception as e:
        st.error(f"Erro ao carregar materiais: {e}")
        return {}

CATEGORIES = get_categories()
MATERIALS = get_materials()

# Inicializa a lista de pedidos na sessão
if "purchase_requests" not in st.session_state:
    st.session_state.purchase_requests = []

# Formulário de um único item
with st.form(key="add_item_form"):
    st.subheader("📝 Novo Item de Compra")

    col1, col2 = st.columns(2)
    with col1:
        category_id = st.selectbox("Categoria", options=list(CATEGORIES.keys()), format_func=lambda x: CATEGORIES[x])
    with col2:
        material_id = st.selectbox("Material", options=list(MATERIALS.keys()), format_func=lambda x: MATERIALS[x])

    specification = st.text_area("Especificação técnica", placeholder="Descreva o item com detalhes...")
    quantity = st.number_input("Quantidade", min_value=1, step=1, value=1)

    today = datetime.date.today()
    default_proposal_deadline = today + datetime.timedelta(days=2)

    col3, col4 = st.columns(2)
    with col3:
        proposal_deadline = st.date_input("Data limite para receber propostas", value=default_proposal_deadline, min_value=today)
        st.caption(f"📅 Selecionado: {proposal_deadline.strftime('%d/%m/%Y')}")
    with col4:
        delivery_due_date = st.date_input("Data limite para entrega", min_value=today)
        st.caption(f"📦 Entrega até: {delivery_due_date.strftime('%d/%m/%Y')}")

    submitted = st.form_submit_button("➕ Adicionar item")
    if submitted:
        st.session_state.purchase_requests.append({
            "category_id": category_id,
            "category": CATEGORIES[category_id],
            "material_id": material_id,
            "material": MATERIALS[material_id],
            "specification": specification,
            "quantity": quantity,
            "proposal_deadline": proposal_deadline.strftime("%d/%m/%Y"),
            "delivery_due_date": delivery_due_date.strftime("%d/%m/%Y")
        })
        st.success("Item adicionado com sucesso!")

# Exibe os pedidos atuais
if st.session_state.purchase_requests:
    st.subheader("📋 Itens adicionados")
    for i, item in enumerate(st.session_state.purchase_requests):
        st.markdown(f"**Item {i+1}:** {item['quantity']}x {item['material']} ({item['category']})")
        st.markdown(f"- Especificação: {item['specification']}")
        st.markdown(f"- Propostas até: `{item['proposal_deadline']}` | Entrega até: `{item['delivery_due_date']}`")
        st.divider()

    if st.button("🚀 Enviar todos os pedidos"):
        try:
            payload = {
                "requests": [
                    {
                        "category_id": item["category_id"],
                        "material_id": item["material_id"],
                        "specification": item["specification"],
                        "quantity": item["quantity"],
                        "proposal_deadline": item["proposal_deadline"],
                        "delivery_due_date": item["delivery_due_date"]
                    }
                    for item in st.session_state.purchase_requests
                ]
            }
            response = requests.post(f"{BACKEND_URL}/purchase-requests/", json=payload)

            if response.status_code == 200:
                st.success(f"{len(st.session_state.purchase_requests)} pedido(s) enviados com sucesso!")
                st.session_state.purchase_requests = []
            else:
                st.error(f"❌ Erro ao enviar pedidos: {response.text}")

        except Exception as e:
            st.error(f"❌ Erro de conexão com o backend: {e}")
else:
    st.info("Adicione ao menos um item antes de enviar.")
