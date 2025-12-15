import streamlit as st
from textblob import TextBlob
# TextBlob adalah Class dari library textblob, yang punya banyak method bawaan, termasuk .sentiment.

st.title("🧠 Mood Checker dari Kalimatmu")
st.write("Coba tulis satu kalimat dan lihat AI menebak mood kamu! 🤖")

# Input dari user
kalimat = st.text_input("➡️ Masukkan kalimatmu di sini:")

if st.button("Cek Mood"):
    if kalimat:
        # Buat object TextBlob dari kalimat user
        blob = TextBlob(kalimat)
        hasil = blob.sentiment
        #sentiment adalah method (fungsi bawaan dari class TextBlob) yang mengembalikan dua atribut penting:
        # .polarity: nilai -1 sampai 1 (semakin positif → mood positif)
        # .subjectivity: nilai 0 sampai 1 (semakin tinggi → semakin subjektif/emosional)

        # Tampilkan hasil analisis
        st.subheader("🔍 Hasil Analisis Mood:")
        st.write(f"**Polarity** (positif/negatif): `{hasil.polarity}`")
        st.write(f"**Subjectivity** (emosi pribadi): `{hasil.subjectivity}`")

        # Interpretasi mood
        if hasil.polarity > 0:
            st.success("✅ Mood kamu POSITIF! Semangat terus ya!")
        elif hasil.polarity < 0:
            st.error("❌ Mood kamu NEGATIF... coba istirahat sebentar yuk.")
        else:
            st.info("😐 Mood kamu NETRAL. Boleh jadi kamu lagi mikir keras!")

        # Bonus ekspresi emosional
        rating = int(hasil.subjectivity * 10)
        st.write(f"📊 Tingkat emosional ekspresi: `{rating}/10`")
    else:
        st.warning("Masukkan kalimat dulu yuk!")