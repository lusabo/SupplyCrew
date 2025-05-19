import streamlit as st
import requests

st.title("SupplyCrew Dashboard")
response = requests.get("http://backend:8000/ping")
st.write("Backend responde:", response.json())

