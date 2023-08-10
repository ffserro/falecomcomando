import streamlit as st

from datetime import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = 'smtp-mail.outlook.com'
port = 587
user = st.secrets['USUARIO']
password = st.secrets['SENHA']
server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(user, password)

from io import BytesIO
import base64

file_ = open("logo.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(f"<img style='display: block; margin-left: auto; margin-right: auto; width:40%;' src='data:image/png;base64,{data_url}' alt='ComGptPatNavSSE' width='500'>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>CAIXA DE SUGESTÕES DO MAKÃO</h1>", unsafe_allow_html=True)

st.write('Use esta ferramenta para fazer sugestões de melhoria para o convívio e o cumprimento da missão do Grupamento.')

nome_militar = st.text_input('Caso você deseje se identificar, digite o seu nome abaixo:')

sugestao = st.text_area('Deixe aqui a sua sugestão: ')

if st.button('Enviar'):
    if nome_militar:
        message = f'Sugestão de {nome_militar} em {datetime.now().strftime('%d/%m/%Y, às %H:%M:%S')}: \n\n{sugestao}'
    else:
        message = f'Sugestão anônima em {datetime.now().strftime('%d/%m/%Y, às %H:%M:%S')}: \n\n{sugestao}'

    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = 'serro@marinha.mil.br'
    email_msg['Subject'] = 'Fale com o comando - Sugestão'

    email_msg.attach(MIMEText(message, 'plain'))