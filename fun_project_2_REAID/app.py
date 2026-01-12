import streamlit as st
import requests
import json
import base64

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Kinanthi AI Chatbot", page_icon="💬", layout="wide")

# --- FUNGSI UNTUK MEMBACA GAMBAR LOKAL ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

# --- 2. CUSTOM CSS (Full Fix: Judul Tengah & Teks AI Hitam) ---
bin_str = get_base64_of_bin_file('assets/BG-riwayat.jpg') 
st.markdown(f"""
    <style>
        .stApp, [data-testid="stHeader"], [data-testid="stBottom"], .stMain {{
            background-color: #182220 !important;
        }}
        [data-testid="stSidebar"] {{
            background-image: url("data:image/jpg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
        }}
        [data-testid="stSidebarContent"] {{ background-color: rgba(0, 0, 0, 0.4) !important; }}
        
        /* Bubble Chat User */
        [data-testid="stChatMessage"]:has([aria-label="Chat message from user"]) {{
            background-color: #b66d38 !important;
            color: white !important;
            border-radius: 15px;
        }}
        /* Bubble Chat AI (Teks Hitam) */
        [data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) {{
            background-color: #e6d1a3 !important; 
            border-radius: 15px;
        }}
        [data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) p,
        [data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) span {{
            color: #000000 !important;
        }}
        
        /* Judul Tengah */
        .centered-title {{
            text-align: center;
            font-weight: bold;
            font-size: 42px;
            color: white !important;
            display: block;
            width: 100%;
        }}
        h1, h2, h3, p, span, label {{ color: white !important; }}
    </style>
""", unsafe_allow_html=True)

# --- 3. KONFIGURASI API (KEY TERBARU + MODEL TERSTABIL) ---
OPENROUTER_API_KEY = "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"
# Pakai Gemini 2.0 Flash karena ini yang paling stabil di OpenRouter Free sekarang
MODEL = "google/gemini-2.0-flash-exp:free"

# --- 4. INISIALISASI ---
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.markdown("##  Daftar Riwayat")
    if st.session_state.messages:
        for i, msg in enumerate(st.session_state.messages):
            if msg["role"] == "user":
                st.markdown(f'<div style="background: rgba(255,255,255,0.1); padding: 10px; border-radius: 5px; margin-bottom: 5px; border-left: 3px solid #b66d38;">{msg["content"][:20]}...</div>', unsafe_allow_html=True)
    st.write("---")
    if st.button("🗑️ Hapus Semua Chat"):
        st.session_state.messages = []
        st.rerun()

# --- 5. TAMPILAN UTAMA ---
st.markdown("<h1 class='centered-title'>💬 Kinanthi AI Chatbot 💬</h1>", unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Tulis pesan di sini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Berpikir..."):
            try:
                response = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
                    data=json.dumps({"model": MODEL, "messages": st.session_state.messages})
                )
                if response.status_code == 200:
                    answer = response.json()['choices'][0]['message']['content']
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    st.rerun()
                else:
                    st.error(f"Error {response.status_code}: Server sedang padat. Coba lagi sebentar lagi.")
            except Exception as e:
                st.error(f"Koneksi error: {e}")

st.write("---")
st.caption("Fun Project #2 - Kinanthi Eka Putri - Python AI Batch 5")