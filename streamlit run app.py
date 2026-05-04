import streamlit as st

def convertir_temperatura(valor, de_unidad, a_unidad):
    """
    Función para convertir la temperatura entre Celsius, Fahrenheit y Kelvin.
    """
    # Si las unidades son iguales, retornamos el mismo valor
    if de_unidad == a_unidad:
        return valor
    
    # Primero convertimos el valor de entrada a Celsius como punto intermedio
    if de_unidad == "Fahrenheit":
        celsius = (valor - 32) * 5.0 / 9.0
    elif de_unidad == "Kelvin":
        celsius = valor - 273.15
    else:
        celsius = valor
        
    # Luego convertimos de Celsius a la unidad de destino
    if a_unidad == "Fahrenheit":
        return (celsius * 9.0 / 5.0) + 32
    elif a_unidad == "Kelvin":
        return celsius + 273.15
    else:
        return celsius

# Configuración básica de la página para darle un mejor aspecto
st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️", layout="centered")

# Título y descripción
st.title("🌡️ Conversor de Temperatura")
st.markdown("Una herramienta sencilla y rápida para convertir entre **Celsius, Fahrenheit y Kelvin**.")

# Usamos columnas para darle un diseño más estructurado a la interfaz
col1, col2 = st.columns(2)

with col1:
    st.subheader("Entrada")
    # Campo para ingresar el valor numérico
    valor_entrada = st.number_input("Ingresa el valor:", value=0.0, step=1.0)
    # Selector de la unidad de origen
    unidad_origen = st.selectbox("Convertir de:", ["Celsius", "Fahrenheit", "Kelvin"])

with col2:
    st.subheader("Salida")
    # Selector de la unidad de destino
    unidad_destino = st.selectbox("Convertir a:", ["Celsius", "Fahrenheit", "Kelvin"])
    
    # Realizamos el cálculo en tiempo real
    resultado = convertir_temperatura(valor_entrada, unidad_origen, unidad_destino)
    
    # Mostramos el resultado destacado
    st.markdown("### Resultado:")
    st.success(f"{valor_entrada:.2f} {unidad_origen} equivale a **{resultado:.2f} {unidad_destino}**")

# Un pequeño pie de página
st.divider()
st.caption("Aplicación creada con Streamlit 🎈")
