import streamlit as st

from datetime import datetime, timedelta

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = 'smtp-mail.outlook.com'
port = 587
user = st.secrets['USUARIO']
password = st.secrets['SENHA']
server = smtplib.SMTP(host, port)

from io import BytesIO
import base64

file_ = open("logo.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(f"<img style='display: block; margin-left: auto; margin-right: auto; width:40%;' src='data:image/png;base64,{data_url}' alt='ComGptPatNavSSE' width='500'>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>CAIXA DE SUGESTÕES DO MAKÃO</h1>", unsafe_allow_html=True)


if 'finalizado' not in st.session_state:
    st.write('Use esta ferramenta para fazer sugestões de melhoria para o convívio e o cumprimento da missão do Grupamento.')

    nome_militar = st.text_input('Caso você deseje se identificar, digite o seu nome abaixo:')

    sugestao = st.text_area('Deixe aqui a sua sugestão: ')

    if st.button('Enviar'):
        if nome_militar:
            message = f"Sugestão de {nome_militar} em {(datetime.now() + timedelta(hours=-3)).strftime('%d/%m/%Y, às %H:%M:%S')}: \n\n{sugestao}"
        else:
            message = f"Sugestão anônima em {(datetime.now() + timedelta(hours=-3)).strftime('%d/%m/%Y, às %H:%M:%S')}: \n\n{sugestao}"

        server.ehlo()
        server.starttls()
        server.login(user, password)

        for recipient in ['serro@marinha.mil.br', 'jose.alfredo@marinha.mil.br']:
            email_msg = MIMEMultipart()
            email_msg['From'] = user
            email_msg['To'] = recipient
            email_msg['Subject'] = 'Fale com o comando - Sugestão'

            email_msg.attach(MIMEText(message, 'plain'))

            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        
        server.quit()

        st.session_state['finalizado'] = 1

        st.rerun()
else:
    st.markdown('# Obrigado pela contribuição!')