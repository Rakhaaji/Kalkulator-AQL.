import streamlit as st

import streamlit as st
import math

st.set_page_config(page_title="AQL Checker", layout="centered")

# Sidebar navigation
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Beranda", "Kalkulator AQL"])

def hitung_acceptance(sample_size, aql_percent):
    aql = aql_percent / 100
    return math.floor(sample_size * aql + 0.5)

# ------------------------
# Halaman BERANDA
# ------------------------
if page == "Beranda":
    st.title("📦 Selamat Datang di Kalkulator AQL kelompok 3")
    st.write("""
    AQL (**Acceptable Quality Limit**) adalah batas maksimum jumlah produk cacat yang dianggap masih dapat diterima dalam suatu sampel inspeksi.
    
    Alat ini membantu Anda menghitung apakah suatu **lot** (jumlah barang dalam batch produksi) dapat diterima atau ditolak berdasarkan jumlah sampel, cacat yang ditemukan, dan nilai AQL.

    ### 👈 Gunakan menu di sebelah kiri untuk mengakses kalkulator.
    """)

# ------------------------
# Halaman KALKULATOR
# ------------------------
elif page == "Kalkulator AQL":
    st.title("🔢 Kalkulator AQL")

    # Input
    lot_size = st.number_input("Ukuran Lot", min_value=1, value=500)
    sample_size = st.number_input("Ukuran Sampel", min_value=1, value=50)
    aql = st.number_input("Nilai AQL (%)", min_value=0.01, value=1.0, format="%.2f")
    defects_found = st.number_input("Jumlah Cacat yang Ditemukan", min_value=0, value=0)

    if st.button("Hitung Hasil"):
        acceptance_number = hitung_acceptance(sample_size, aql)
        rejection_number = acceptance_number + 1

        st.markdown(f"**Acceptance Number (Ac):** `{acceptance_number}`")
        st.markdown(f"**Rejection Number (Re):** `{rejection_number}`")

        if defects_found <= acceptance_number:
            st.success("✅ LOT DITERIMA")
        else:
            st.error("❌ LOT DITOLAK")
