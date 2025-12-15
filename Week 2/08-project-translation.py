# Terjemahan Bahasa Real-Time dengan Streamlit + Hugging Face

import streamlit as st
from transformers import pipeline

# Inisialisasi pipeline untuk terjemahan
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-id-en")

# UI Streamlit
st.title("🗣️ Real-time Bahasa Translator")
st.write("Masukkan teks Bahasa Indonesia dan lihat terjemahannya ke Bahasa Inggris.")

text_input = st.text_area("Tulis kalimat Bahasa Indonesia di sini:")

if st.button("Terjemahkan"):
    if text_input.strip():
        with st.spinner("Menerjemahkan..."):
            result = translator(text_input, max_length=100)[0]["translation_text"]
            st.success("Hasil Terjemahan:")
            st.write(f"**{result}**")
    else:
        st.warning("Tolong masukkan teks terlebih dahulu.")