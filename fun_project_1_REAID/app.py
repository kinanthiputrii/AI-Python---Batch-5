import streamlit as st
import base64
import os
import time

# --- 1. FUNGSI UNTUK PROSES BACKGROUND ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'assets', 'batik.jpg')
img_data = get_base64(file_path)

# --- 2. SETUP CSS (TAMPILAN) ---
if img_data:
    bg_style = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,31,63,0.97), rgba(0,31,63,0.97)), 
                    url("data:image/jpg;base64,{img_data}");
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    """
else:
    bg_style = "<style>.stApp { background-color: #001F3F; }</style>"

st.markdown(bg_style, unsafe_allow_html=True)

st.markdown("""
    <style>
    html, body, [class*="css"], .stMarkdown, label { color: #FFFFFF !important; font-size: 18px !important; }
    .judul-putih { color: #FFFFFF !important; font-size: 40px !important; font-weight: bold; border-left: 10px solid #0074D9; padding-left: 15px; margin-bottom: 20px; }
    .stButton>button { background-color: #FFFFFF; color: #001F3F; width: 100%; border-radius: 8px; font-weight: bold; height: 50px; border: none; }
    div[data-testid="stRadio"] { background-color: #003366; padding: 20px; border-radius: 10px; margin-bottom: 10px; }
    /* Style untuk kotak informasi di halaman detail */
    .card-detail { 
        background-color: rgba(255, 255, 255, 0.1); 
        padding: 25px; 
        border-radius: 15px; 
        border: 1px solid #0074D9;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (BAGIAN YANG TIDAK DIHAPUS) ---
with st.sidebar:
    st.title("Menu Navigasi")
    st.info("Kuis ini menggunakan algoritma skoring sederhana untuk menentukan kecocokan karir IT kamu.")
    st.write("---")
    
    # Bagian yang kamu minta tetap ada:
    st.subheader("Tentang Project")
    st.write("Aplikasi ini dibuat untuk tugas Fun Project #1 Batch 5.")
    
    st.write("---")
    if st.button("Reset Kuis 🔄"):
        st.session_state.page = 1
        st.rerun()

# --- 4. INISIALISASI SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = 1
if 'nama' not in st.session_state: st.session_state.nama = ""
if 'hasil_final' not in st.session_state: st.session_state.hasil_final = ""

# --- 5. LOGIKA HALAMAN ---

# HALAMAN 1: INPUT NAMA
if st.session_state.page == 1:
    st.progress(0)
    st.markdown('<p class="judul-putih">Profesi IT apa sih yang cocok buat kamu?</p>', unsafe_allow_html=True)
    st.write("Yuk cari masa depanmu di dunia teknologi!!")
    
    nama_input = st.text_input("Siapa nama kamu?", value=st.session_state.nama, placeholder="Ketik namamu di sini...")
    
    with st.expander("Kenapa harus coba kui ini?"):
        st.write("Industri IT punya banyak cabang. Langkah awal yang bagus jika mengetahui minat dasarmu untuk menjadi ahli!")

    if st.button("Mulai →"):
        if nama_input:
            st.session_state.nama = nama_input
            st.session_state.page = 2
            st.rerun()
        else:
            st.error("Silakan masukkan nama terlebih dahulu.")

# HALAMAN 2: PERTANYAAN KUIS
elif st.session_state.page == 2:
    st.progress(40)
    st.markdown(f'<p class="judul-putih">Pertanyaan untuk {st.session_state.nama}</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        q1 = st.radio("Apa hobi kamu?", ["Ngulik aplikasi", "Menggambar/Desain", "Analisis data"])
    with col2:
        q2 = st.radio("Fokus utama kamu?", ["Logika & Coding", "Visual & Estetika", "Informasi & Tren"])

    if st.button("Lihat Hasil Akhir"):
        with st.spinner('Menganalisis minat kamu...'):
            time.sleep(1.2)
            # Logika penentuan hasil
            if q1 == "Ngulik aplikasi" or q2 == "Logika & Coding":
                st.session_state.hasil_final = "Programmer"
            elif q1 == "Menggambar/Desain" or q2 == "Visual & Estetika":
                st.session_state.hasil_final = "UI/UX Designer"
            else:
                st.session_state.hasil_final = "Data Scientist"
            
            st.session_state.page = 3
            st.rerun()

# HALAMAN 3: RINGKASAN HASIL
elif st.session_state.page == 3:
    st.progress(75)
    st.markdown('<p class="judul-putih">Hasil Analisis Karier</p>', unsafe_allow_html=True)
    st.balloons()
    
    st.success(f"Selamat **{st.session_state.nama}**! Kamu sangat cocok menjadi seorang **{st.session_state.hasil_final}**!")
    
    st.write("---")
    st.write("Ingin tahu lebih dalam tentang profesi ini?")
    if st.button("Baca detail profesimu yuk!! "):
        st.session_state.page = 4
        st.rerun()

# HALAMAN 4: DETAIL PROFESI
elif st.session_state.page == 4:
    st.progress(100)
    st.markdown(f'<p class="judul-putih">Mengenal {st.session_state.hasil_final}</p>', unsafe_allow_html=True)
    
    if st.session_state.hasil_final == "Programmer":
        st.markdown("""
        <div class="card-detail">
            <h3>💻 Programmer</h3>
            <p>Seorang Programmer membangun sistem dan aplikasi menggunakan bahasa pemrograman.</p>
            <ul>
                <li><b>Skill:</b> Python, JavaScript, Java, C++.</li>
                <li><b>Tanggung Jawab:</b> Membuat fitur, memperbaiki bug, dan mengembangkan software.</li>
                <li><b>Kenapa Seru?</b> Kamu bisa menciptakan sesuatu yang bermanfaat bagi ribuan orang dari nol.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    elif st.session_state.hasil_final == "UI/UX Designer":
        st.markdown("""
        <div class="card-detail">
            <h3>🎨 UI/UX Designer</h3>
            <p>UI/UX Designer memastikan aplikasi mudah digunakan dan memiliki tampilan yang indah.</p>
            <ul>
                <li><b>Skill:</b> Figma, Design Thinking, Riset Pengguna.</li>
                <li><b>Tanggung Jawab:</b> Membuat alur aplikasi (wireframe) dan desain visual (mockup).</li>
                <li><b>Kenapa Seru?</b> Kamu menggabungkan seni dengan teknologi untuk memanjakan mata pengguna.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    else: # Data Scientist
        st.markdown("""
        <div class="card-detail">
            <h3>📊 Data Scientist</h3>
            <p>Ahli data yang mencari pola penting dari ribuan data untuk kemajuan bisnis.</p>
            <ul>
                <li><b>Skill:</b> Statistik, Machine Learning, SQL, Python.</li>
                <li><b>Tanggung Jawab:</b> Mengolah data mentah menjadi wawasan (insight) berharga.</li>
                <li><b>Kenapa Seru?</b> Kamu menjadi "peramal" modern dengan kekuatan data dan matematika.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    if st.button("Coba Kuis Lagi ↺"):
        st.session_state.page = 1
        st.rerun()

# --- 6. FOOTER ---
st.write("---")
st.caption("Fun Project #1 - Kinanthi Eka Putri - Python AI Batch 5")