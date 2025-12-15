import streamlit as st

st.title("🛒 Kalkulator Diskon Belanja")

total_belanja = st.number_input("Masukkan total belanja (Rp):", min_value=0)

if total_belanja < 100_000:
    diskon = 0
elif total_belanja < 200_000:
    diskon = 0.05
elif total_belanja < 300_000:
    diskon = 0.08
else:
    diskon = 0.10

potongan = total_belanja * diskon
total_bayar = total_belanja - potongan

if st.button("Hitung Diskon"):
    st.write(f"Diskon: {int(diskon * 100)}%")
    st.write(f"Potongan Harga: Rp{potongan:,.0f}")
    st.write(f"Total Bayar: Rp{total_bayar:,.0f}")