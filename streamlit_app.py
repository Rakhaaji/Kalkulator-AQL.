import streamlit as st

import math

st.set_page_config(page_title="Kalkulator AQL", layout="centered")

st.title("📊 Kalkulator AQL (Acceptable Quality Limit)")

# Input
lot_size = st.number_input("Ukuran Lot", min_value=1, value=500)
sample_size = st.number_input("Ukuran Sampel", min_value=1, value=50)
aql = st.number_input("Nilai AQL (%)", min_value=0.01, value=1.0, format="%.2f")
defects_found = st.number_input("Jumlah Cacat yang Ditemukan", min_value=0, value=0)

# Fungsi untuk menghitung acceptance number (berdasarkan standar kasar)
def get_acceptance_number(sample_size, aql_percent):
    aql = aql_percent / 100
    # Approximate acceptance number using binomial approximation
    return math.floor(sample_size * aql + 0.5)

if st.button("Hitung Hasil"):
    acceptance_number = get_acceptance_number(sample_size, aql)
    
    st.write(f"🔢 **Acceptance Number (Ac):** {acceptance_number}")
    st.write(f"❌ **Rejection Number (Re):** {acceptance_number + 1}")
    
    if defects_found <= acceptance_number:
        st.success("✅ LOT DITERIMA")
    else:
        st.error("❌ LOT DITOLAK")
