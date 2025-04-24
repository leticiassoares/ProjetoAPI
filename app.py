import requests
import streamlit as st

def buscar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    if response.status_code == 200: 
        letra = response.json()['lyrics'] 
        return letra
    else: ""


st.image("https://i.imgur.com/SmktDIH.png")
st.title("Letras de músicas!")

banda = st.text_input("Digite o nome da banda/cantor: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("Pesquisar")

if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Encontramos a letra da música")
        st.text(letra)
    else:
        st.error("Infelizmente, não encontrei a letra dessa música")