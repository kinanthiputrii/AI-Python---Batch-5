# 💬 Kinanthi AI Chatbot 💬
**Tugas Fun Project #2 - Python AI Batch 5**

Halo! Ini bot buatanku, **Kinanthi**. Selain menjawab pertanyaan, tampilannya udah kubuat cukup menarik jadi nggak bosenin waktu dipake ngobrol. Otaknya pake **Gemini 1.5 Flash** yang ditarik lewat OpenRouter, jadi lumayan pinter lah ya!

---

## Fitur-Fitur Kece
* **Pinter & Gercep**: Pake model Gemini terbaru, responsnya nyambung dan nggak kaku.
* **Tampilan Estetik**: Tema dark mode dengan skema warna oranye-krem biar enak di mata.
* **Riwayat Chat**: Ada daftar chat di sidebar kiri buat inget-inget obrolan sebelumnya.
* **Gampang Dibaca**: Tulisan AI warna hitam di bubble krem biar kontrasnya pas.
* **Anti-Nyangkut**: Ada tombol "Hapus Semua Chat" buat reset obrolan kalo udah kepanjangan.

---

## Persiapan Sebelum Jalan
Sebelum running, pastiin kamu punya:
1. **Python** sudah terinstall (versi 3.9 ke atas lebih aman).
2. **API Key OpenRouter** (bisa dapet gratis di openrouter.ai).
3. **Folder Assets**: Pastiin ada folder bernama `assets` yang isinya gambar `BG-riwayat.jpg` buat background sidebarnya.

---

Langkah-Langkah Menjalankan
Ikutin langkah ini ya biar nggak error:

1. **Siapkan Folder Project** Taruh file `.py` kamu dan folder `assets` dalam satu folder yang sama.
   
2. **Buka Terminal / Command Prompt** Arahkan ke folder tempat kamu simpen file tadi.

3. **Install Library yang Dibutuhkan** Ketik perintah ini dan tunggu sampe beres:
   ```bash
   pip install streamlit requests
4. Jalankan Aplikasi Ketik perintah di bawah (ganti nama_file.py jadi nama file kamu, misal main.py):
    streamlit run nama_file.py
5. Mulai Ngobrol! Browser kamu bakal otomatis kebuka ke alamat localhost:8501. Kalo udah muncul, langsung aja tes sapa si bot-nya!