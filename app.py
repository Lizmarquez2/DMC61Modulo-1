import streamlit as st

st.title("Especialización Pyhton for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Liz Marquez")

valor_inicial = st.number_input("Ingrese el valor inicial")
valor_final = st.number_input("Ingrese el valor final")

lista_numeros = list(range(int(valor_inicial), int(valor_final)))
st.write(lista_numeros) 

modulos = st.sidebar.selectbox ("Seleccione un módulo",["Módulo Listas","Módulo Arreglos","Módulo Funciones"])

if modulos == "Módulos Listas":
  st.write("Bienvenido al módulo Listas")
elif modulos =="Módulos Arreglos":
  st.write("Bienvenido al módulo Arreglos")
else:
  st.write("Bienvenido al módulo Funciones")
