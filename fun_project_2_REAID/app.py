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

# --- 2. CUSTOM CSS ---
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
        [data-testid="stSidebarContent"] {{
            background-color: rgba(0, 0, 0, 0.5) !important;
        }}

        /* Judul Tengah */
        .centered-title {{
            text-align: center;
            font-weight: bold;
            font-size: 42px;
            color: white !important;
            margin-bottom: 5px;
            display: block;
            width: 100%;
        }}

        /* Tulisan Tambahan (Caption di bawah judul) */
        .centered-caption {{
            text-align: center;
            font-size: 16px;
            color: #cccccc !important;
            margin-bottom: 30px;
            display: block;
            width: 100%;
        }}

        [data-testid="stChatMessage"]:has([aria-label="Chat message from user"]) {{
            background-color: #b66d38 !important;
            color: white !important;
            border-radius: 15px;
        }}

        [data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) {{
            background-color: #e6d1a3 !important; 
            border-radius: 15px;
        }}

        [data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) p,
        [data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) span,
        [data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) div {{
            color: #000000 !important;
        }}

        h1, h2, h3, p, span, label {{
            color: white !important;
        }}
    </style>
""", unsafe_allow_html=True)

# --- 3. KONFIGURASI API ---
API_KEY_KAMU = "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"
MODEL_AI = "meta-llama/llama-3-8b-instruct:free"

# --- 4. LOGIKA RIWAYAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.markdown("##  Daftar Riwayat")
    if st.session_state.messages:
        for i, msg in enumerate(st.session_state.messages):
            if msg["role"] == "user":
                st.markdown(f"**{i//2 + 1}.** {msg['content'][:25]}...")
    
    st.write("---")
    if st.button("🗑️ Hapus Semua Chat"):
        st.session_state.messages = []
        st.rerun()

# --- 5. TAMPILAN UTAMA ---
st.markdown("<h1 class='centered-title'>💬 Kinanthi AI Chatbot 💬</h1>", unsafe_allow_html=True)
st.markdown("<span class='centered-caption'>Mau tanya apa hari ini?</span>", unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Tulis sesuatu di sini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Kinanthi AI sedang mengetik..."):
            try:
                response = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {API_KEY_KAMU}",
                        "Content-Type": "application/json"
                    },
                    data=json.dumps({
                        "model": MODEL_AI,
                        "messages": st.session_state.messages
                    }),
                    timeout=20
                )

                if response.status_code == 200:
                    answer = response.json()['choices'][0]['message']['content']
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    st.rerun()
                elif response.status_code == 429:
                    st.warning("Aduh, servernya lagi penuh banget! Tunggu 10-15 detik terus coba kirim lagi ya.")
                else:
                    st.error(f"Ada gangguan teknis (Error {response.status_code})")
            
            except Exception as e:
                st.error("Koneksi bermasalah. Pastikan internetmu aktif ya!")

st.write("---")
st.caption("Fun Project #2 - Kinanthi Eka Putri - Python AI Batch 5")