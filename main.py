import streamlit as st
from io import BytesIO
import base64

file_ = open("logo.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(f"<img style='display: block; margin-left: auto; margin-right: auto; width:40%;' src='data:image/png;base64,{data_url}' alt='ComGptPatNavSSE' width='500'>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>CAIXA DE SUGESTÕES DO MAKÃO</h1>", unsafe_allow_html=True)

st.write('Use esta ferramenta para fazer sugestões de melhoria para o convívio e o cumprimento da missão do Grupamento.')