import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Cargamos el modelo de regresión optimizado
@st.cache_resource
def load_model():
    return joblib.load('modelo_precio_coches_regresion.joblib')

modelo = load_model()

# 2. Configuración de la interfaz web
st.set_page_config(page_title="Tasador Inteligente de Coches", page_icon="🚗", layout="centered") #añadimos sel icono de coche

st.title("🚗 Tasador Inteligente de Vehículos (Gradient Boosting)")
st.write("Introduce las especificaciones mecánicas del coche para calcular su valor estimado de mercado en tiempo real.")
st.markdown("---")

# 3. Diccionarios de mapeo generados por el LabelEncoder de Colab
marcas_disponibles = ['Acura', 'Audi', 'BMW', 'Buick', 'Cadillac', 'Chevrolet', 'Chrylser', 'Chrysler', 'Dodge', 'Eagle', 'Ford', 'Geo', 'Honda', 'Hyundai', 'Infiniti', 'Jeep', 'Lexus', 'Lincoln', 'Mazda', 'Mercedes-Benz', 'Mercury', 'Mitsubishi', 'Nissan', 'Oldsmobile', 'Plymouth', 'Pontiac', 'Saab', 'Saturn', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo']
categorias_disponibles = ['Compact', 'Large', 'Midsize', 'Small', 'Sporty', 'Van']
airbags_disponibles = ['Driver & Passenger', 'Driver only', 'None']

# Mapeos numéricos directos para que la IA los entienda
map_marcas = {marca: i for i, marca in enumerate(marcas_disponibles)}
map_categorias = {cat: i for i, cat in enumerate(categorias_disponibles)}
map_airbags = {air: i for i, air in enumerate(airbags_disponibles)}

# 4. Formulario de entrada de datos
col1, col2 = st.columns(2)

with col1:
    marca_sel = st.selectbox("Marca del Vehículo", marcas_disponibles, index=1) # Por defecto Audi
    categoria_sel = st.selectbox("Categoría de Carrocería", categorias_disponibles, index=2) # Por defecto Midsize
    airbag_sel = st.selectbox("Equipamiento de Seguridad (Airbags)", airbags_disponibles)
    cilindros = st.slider("Número de Cilindros", min_value=0, max_value=8, value=4, step=1)
    capacidad_pasajeros = st.slider("Capacidad de Pasajeros", min_value=2, max_value=8, value=5)

with col2:
    caballos = st.number_input("Caballos de Potencia (HP)", min_value=50, max_value=500, value=140, step=10)
    motor_litros = st.number_input("Cilindrada del Motor (Litros)", min_value=0.0, max_value=6.0, value=2.0, step=0.1)
    rpm_max = st.slider("RPM Máximas del Motor", min_value=3000, max_value=7000, value=5500, step=100)
    consumo_ciudad = st.number_input("Eficiencia / Rendimiento Urbano", min_value=0.0, max_value=50.0, value=22.0, step=1.0, help="En vehículos eléctricos/híbridos, introduce la equivalencia de eficiencia o pon 0 si es 100% eléctrico.")

st.markdown("---")

# 5. Cálculo de la predicción económica
if st.button("Calcular Tasación Estimada", use_container_width=True):
    
    # Construimos el DataFrame transformando los textos a los números del LabelEncoder
    datos_usuario = pd.DataFrame([{
        'Marca': map_marcas[marca_sel],
        'Categoría': map_categorias[categoria_sel],
        'Airbags': map_airbags[airbag_sel],
        'Cilindros': cilindros,
        'Motor_Litros': motor_litros,
        'Caballos_Potencia': caballos,
        'RPM_Maximas': rpm_max,
        'Consumo_Ciudad': consumo_ciudad,
        'Capacidad_Pasajeros': capacidad_pasajeros
    }])
    
    # Ejecutamos la regresión
    precio_predicho = modelo.predict(datos_usuario)[0]
    
    # Control de seguridad por si la combinación de datos da un número negativo
    if precio_predicho < 500:
        precio_predicho = 500.0
        
    # Mostramos el resultado con formato de dinero elegante
    st.metric(label="Precio de Mercado Estimado", value=f"{precio_predicho:,.2f} €")
    st.info(f"Nota: El modelo estima este valor basándose en las especificaciones del motor y equipamiento, con un margen de variación promedio de ± {5058.69:,.2f} €.")