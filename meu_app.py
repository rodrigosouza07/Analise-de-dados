import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu site streamlit")


with st.container():
    st.title("Dashboard sobre Fifa")
    st.subheader("Minha primeira aplicação com Streamlit")
    st.write("Informações sobre joagdores do Fifa")

with st.container():
    st.write("------");
    dados = pd.read_csv("fifa.csv")
    
