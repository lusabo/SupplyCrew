import streamlit as st
import datetime

# Simulações de categorias e materiais (substitua por dados reais do backend)
CATEGORIES = {
    1: 'Chapas',
    2: 'Tubos',
    3: 'Laminados (cantoneiras e vigas)',
    4: 'Instrumentos (válvulas)',
    5: 'Conexões'
}

MATERIALS = {
    1: 'Inox 316',
    2: 'Inox 304',
    3: 'Latão',
    4: 'Alumínio',
    5: 'Duplex',
    6: 'Aço Carbono'
}

st.set_page_config(page_title="Cadastro de Pedidos", page_icon="📦")
st.title("📦 Cadastro de Pedido de Compra")

st.markdown("Preencha os campos abaixo para um ou mais itens de compra. Você pode adicionar quantos quiser antes de enviar.")

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
    with col4:
        delivery_due_date = st.date_input("Data limite para entrega", min_value=today)

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

    # Botão de envio final
    if st.button("🚀 Enviar todos os pedidos"):
        # Aqui você chamaria a API do backend com os dados acumulados
        st.success(f"{len(st.session_state.purchase_requests)} pedido(s) enviados com sucesso!")
        st.session_state.purchase_requests = []
else:
    st.info("Adicione ao menos um item antes de enviar.")
