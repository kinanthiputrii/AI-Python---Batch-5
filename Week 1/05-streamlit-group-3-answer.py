import streamlit as st

st.title("🌤️ Prediksi Mood Berdasarkan Cuaca")

cuaca = st.selectbox("Pilih cuaca hari ini:", ["Cerah", "Mendung", "Hujan", "Berangin"])

if cuaca == "Cerah":
    mood = "Kamu ceria dan semangat!"
elif cuaca == "Mendung":
    mood = "Mood kamu mellow dan butuh pelukan ☁️"
elif cuaca == "Hujan":
    mood = "Kamu pengen rebahan sambil nonton drakor."
else:
    mood = "Kamu agak nggak fokus hari ini. Minum teh, yuk!"

st.write(f"Mood kamu hari ini: {mood}")