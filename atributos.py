import streamlit as st
import pandas as pd
import requests



token = st.text_input("ingrese un token", "token")
publicacion= st.text_input("ingrese un item", 'MLA928704162')
#token = 'APP_USR-8281042440531010-072514-ac36d79d0b8550aad06531478c2a755c-10470150'
items = [publicacion]

for item in items:
    url = f" https://api.mercadolibre.com/catalog_quality/status?item_id={item}&v=3&access_token={token}"

   
    response = requests.request("GET", url)

rta = response.json()
missing = rta['adoption_status']['ft']['missing_attributes']

'''Atributos Faltantes:'''

if missing:
    st.write(missing)
else:
    st.write('Ninguno')    



