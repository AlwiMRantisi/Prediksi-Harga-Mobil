'''Alwi Muhamad R(237006052)'''

import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediksi Harga Mobil",
    layout="wide"
)

st.markdown("""
<div class="header-box">
    <h1>Aplikasi Prediksi Harga Mobil</h1>
    <p>Prediksi harga mobil berdasarkan spesifikasi kendaraan</p>
</div>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("model_harga_mobil.pkl")

# Layout 2 kolom
col1, col2 = st.columns(2)

with col1:
    st.subheader("Jenis dan Spesifikasi Mesin")

    vehicle_type = st.selectbox(
        "Vehicle Type",
        ["Passenger", "Car"]
    )

    engine_size = st.number_input("Engine Size", min_value=0.0, value=2.4)
    horsepower = st.number_input("Horsepower", min_value=0.0, value=150.0)
    fuel_capacity = st.number_input("Fuel Capacity", min_value=0.0, value=18.0)
    fuel_efficiency = st.number_input("Fuel Efficiency", min_value=0.0, value=25.0)

with col2:
    st.subheader("Dimensi Mobil")

    wheelbase = st.number_input("Wheelbase", min_value=0.0, value=110.0)
    width = st.number_input("Width", min_value=0.0, value=70.0)
    length = st.number_input("Length", min_value=0.0, value=190.0)
    curb_weight = st.number_input("Curb Weight", min_value=0.0, value=3.2)

st.markdown("---")

if st.button("Prediksi Harga Mobil", use_container_width=True):
    data_baru = pd.DataFrame({
        'Vehicle_type': [vehicle_type],
        'Engine_size': [engine_size],
        'Horsepower': [horsepower],
        'Wheelbase': [wheelbase],
        'Width': [width],
        'Length': [length],
        'Curb_weight': [curb_weight],
        'Fuel_capacity': [fuel_capacity],
        'Fuel_efficiency': [fuel_efficiency]
    })

    prediksi = model.predict(data_baru)

    st.success(f"Perkiraan Harga Mobil: ${prediksi[0]:,.2f} Ribu")

    st.write("Data yang digunakan untuk prediksi:")
    st.dataframe(data_baru)
