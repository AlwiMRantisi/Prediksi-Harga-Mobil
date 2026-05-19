'''Alwi Muhamad R(237006052)'''

import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediksi Harga Mobil",
    layout="wide"
)

# Header
st.markdown("""
<div class="header-box">
    <h1>Aplikasi Prediksi Harga Mobil</h1>
    <p>Prediksi harga mobil berdasarkan spesifikasi kendaraan</p>
</div>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("model_harga_mobil.pkl")
columns = joblib.load("columns.pkl")



# Layout 2 kolom
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Spesifikasi Mesin")
    engine_size = st.number_input("Engine Size", min_value=0.0, value=2.0)
    horsepower = st.number_input("Horsepower", min_value=0.0, value=150.0)
    fuel_capacity = st.number_input("Fuel Capacity", min_value=0.0, value=15.0)
    fuel_efficiency = st.number_input("Fuel Efficiency", min_value=0.0, value=25.0)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Dimensi Mobil")
    wheelbase = st.number_input("Wheelbase", min_value=0.0, value=100.0)
    width = st.number_input("Width", min_value=0.0, value=70.0)
    length = st.number_input("Length", min_value=0.0, value=180.0)
    curb_weight = st.number_input("Curb Weight", min_value=0.0, value=3.0)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

sales = st.slider("Sales in thousands", min_value=0.0, max_value=600.0, value=50.0)

if st.button("Prediksi Harga Mobil", use_container_width=True):
    input_data = pd.DataFrame([{
        "Sales_in_thousands": sales,
        "Engine_size": engine_size,
        "Horsepower": horsepower,
        "Wheelbase": wheelbase,
        "Width": width,
        "Length": length,
        "Curb_weight": curb_weight,
        "Fuel_capacity": fuel_capacity,
        "Fuel_efficiency": fuel_efficiency
    }])

    input_data = input_data.reindex(columns=columns, fill_value=0)

    prediksi = model.predict(input_data)

    st.markdown(f"""
    <div class="result-box">
        Perkiraan Harga Mobil: ${prediksi[0]:,.2f} Ribu
    </div>
    """, unsafe_allow_html=True)