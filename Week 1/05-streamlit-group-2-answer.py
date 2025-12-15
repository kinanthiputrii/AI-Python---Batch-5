import streamlit as st
from datetime import datetime

st.title("📅 Tebak Umurmu")

tahun_lahir = st.number_input("Masukkan tahun lahir kamu:", min_value=1900, max_value=datetime.now().year)

if st.button("Hitung Umur"):
    umur = datetime.now().year - tahun_lahir
    st.write(f"Umur kamu sekarang: {umur} tahun")