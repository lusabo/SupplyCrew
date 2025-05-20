import streamlit as st
from datetime import date

st.set_page_config(page_title="Nova Solicitação de Compra", layout="centered")

st.title("📝 Nova Solicitação de Compra")
st.markdown("Preencha os dados abaixo para iniciar um novo processo de cotação.")

# --- Dados do Item ---
st.subheader("🔍 Detalhes do Item")

item = st.text_input("Nome do Item", placeholder="Ex: Roda de liga leve 100mm")
descricao = st.text_area("Descrição Técnica", placeholder="Especifique dimensões, material, padrão técnico etc.")
quantidade = st.number_input("Quantidade", min_value=1, step=1)
data_limite = st.date_input("Data Limite para Entrega", min_value=date.today())

# --- Critérios Técnicos (opcional) ---
st.subheader("⚙️ Critérios Técnicos (opcional)")
criterios = {}
col1, col2 = st.columns(2)
with col1:
    criterios['peso_preco'] = st.slider("Peso - Preço", 0, 100, 50)
with col2:
    criterios['peso_prazo'] = st.slider("Peso - Prazo", 0, 100, 30)

criterios['peso_qualidade'] = 100 - criterios['peso_preco'] - criterios['peso_prazo']

if criterios['peso_qualidade'] < 0:
    st.warning("A soma dos pesos não pode exceder 100%. Ajuste os valores.")
    criterios['peso_qualidade'] = 0

# --- Fornecedores ---
st.subheader("📦 Fornecedores Alvo")
num_forn = st.number_input("Quantidade de Fornecedores para Cotação", min_value=1, max_value=10, value=3)
emails_forn = []
for i in range(num_forn):
    email = st.text_input(f"Email do Fornecedor {i+1}", key=f"forn_email_{i}")
    if email:
        emails_forn.append(email)

# --- Envio ---
st.subheader("🚀 Enviar Solicitação")

if st.button("Enviar Solicitação"):
    if not item or not descricao or not emails_forn:
        st.error("Todos os campos obrigatórios devem ser preenchidos.")
    else:
        st.success("Solicitação enviada com sucesso! 🎉")
        st.markdown("### ✅ Resumo da Solicitação")
        st.json({
            "item": item,
            "descricao": descricao,
            "quantidade": quantidade,
            "data_limite": str(data_limite),
            "criterios": criterios,
            "fornecedores": emails_forn
        })
