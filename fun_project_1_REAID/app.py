import streamlit as st
import base64
import os

# --- 1. FUNGSI UNTUK PROSES BACKGROUND ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# Path menuju gambar batik di dalam folder assets
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'assets', 'batik.jpg')
img_data = get_base64(file_path)

# --- 2. SETUP CSS (TEMA & BACKGROUND) ---
if img_data:
    bg_style = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,31,63,0.97), rgba(0,31,63,0.97)), 
                    url("data:image/jpg;base64,{img_data}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
else:
    bg_style = "<style>.stApp { background-color: #001F3F; }</style>"

st.markdown(bg_style, unsafe_allow_html=True)

# CSS Tambahan untuk Teks dan UI
st.markdown("""
    <style>
    html, body, [class*="css"], .stMarkdown, label {
        color: #FFFFFF !important;
        font-size: 20px !important;
    }
    .judul-putih {
        color: #FFFFFF !important;
        font-size: 45px !important;
        font-weight: bold;
        border-left: 10px solid #0074D9;
        padding-left: 15px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #FFFFFF;
        color: #001F3F;
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        height: 50px;
        border: none;
    }
    div[data-testid="stRadio"] {
        background-color: #003366;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INISIALISASI SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'nama' not in st.session_state:
    st.session_state.nama = ""

# --- 4. LOGIKA HALAMAN ---

# HALAMAN 1: INPUT NAMA
if st.session_state.page == 1:
    st.markdown('<p class="judul-putih">Profesi IT apa sih yang cocok buat kamu?</p>', unsafe_allow_html=True)
    st.write("Cari tahu yuk!!")
    st.write("") 
    nama_input = st.text_input("Siapa nama kamu?", value=st.session_state.nama)
    st.write("")
    if st.button("Mulai Kuis →"):
        if nama_input:
            st.session_state.nama = nama_input
            st.session_state.page = 2
            st.rerun()
        else:
            st.warning("Mohon masukkan namamu terlebih dahulu.")

# HALAMAN 2: PERTANYAAN
elif st.session_state.page == 2:
    st.markdown(f'<p class="judul-putih">Halo, {st.session_state.nama}</p>', unsafe_allow_html=True)
    q1 = st.radio("Apa hobi kamu di waktu luang?", 
                  ["Ngulik aplikasi baru", "Menggambar atau edit foto", "Membaca angka atau data"])
    st.write("") 
    q2 = st.radio("Bagian mana dari web yang paling kamu suka?", 
                  ["Logika dan fungsinya", "Tampilan dan estetikanya", "Akurasi data yang ditampilkan"])
    st.write("")
    if st.button("Lihat Hasil Akhir"):
        st.session_state.q1 = q1
        st.session_state.q2 = q2
        st.session_state.page = 3
        st.rerun()

# HALAMAN 3: HASIL
elif st.session_state.page == 3:
    st.markdown('<p class="judul-putih">Hasil Analisis Profesi</p>', unsafe_allow_html=True)
    skor_prog, skor_dsgn, skor_ds = 0, 0, 0
    if st.session_state.q1 == "Ngulik aplikasi baru": skor_prog += 1
    elif st.session_state.q1 == "Menggambar atau edit foto": skor_dsgn += 1
    else: skor_ds += 1
    if st.session_state.q2 == "Logika dan fungsinya": skor_prog += 1
    elif st.session_state.q2 == "Tampilan dan estetikanya": skor_dsgn += 1
    else: skor_ds += 1

    st.write("---")
    if skor_prog >= skor_dsgn and skor_prog >= skor_ds:
        st.success(f"Berdasarkan jawabanmu, {st.session_state.nama} sangat cocok menjadi Programmer!")
    elif skor_dsgn > skor_ds:
        st.success(f"Berdasarkan jawabanmu, {st.session_state.nama} sangat cocok menjadi Designer!")
    else:
        st.success(f"Berdasarkan jawabanmu, {st.session_state.nama} sangat cocok menjadi Data Scientist!")
    st.balloons()
    st.write("")
    if st.button("Coba Lagi ↺"):
        st.session_state.page = 1
        st.rerun()

# --- 5. FOOTER (Ditambahkan di luar logika halaman agar selalu muncul) ---
st.write("---") # Garis pembatas tipis
st.caption("Fun Project #1 - Kinanthi Eka Putri - Python AI Batch 5")