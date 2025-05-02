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

    st.markdown("""
        <style>
        .industrial-bg {
            background-color: #f5f7fa;
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #ccd3dc;
        }
        .feature-box {
            background-color: #e2e8f0;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 10px;
            border: 1px solid #cbd5e0;
            font-weight: 500;
        }
        .industrial-header {
            font-size: 24px;
            color: #1a202c;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/2819/2819592.png", width=80)  # Icon industri

    st.markdown("<div class='industrial-header'>🏭 Sistem Pemeriksaan Kualitas - AQL</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='industrial-bg'>
        <h4>🔍 Apa itu AQL?</h4>
        <p>
        <strong>AQL (Acceptable Quality Limit)</strong> adalah batas maksimum jumlah cacat yang diperbolehkan dalam suatu sampel acak
        sebelum seluruh lot produksi dianggap tidak memenuhi standar kualitas. Dalam industri manufaktur, AQL membantu tim QC memastikan
        produk sesuai spesifikasi tanpa memeriksa semua item.
        </p>
        <p>
        Kalkulator ini dirancang untuk tim inspeksi dan kontrol kualitas di lingkungan industri untuk mempercepat pengambilan keputusan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🔧 Fitur Sistem")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='feature-box'>
        ✔️ Hitung nilai Acceptance/Rejection<br>
        ✔️ Sesuaikan dengan berbagai ukuran lot<br>
        ✔️ Tidak perlu tabel AQL manual
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-box'>
        📦 Cocok untuk operator QC pabrik<br>
        ⏱️ Proses cepat dan real-time<br>
        💼 Siap digunakan di lingkungan industri
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.success("➡️ Gunakan menu di samping kiri untuk mulai menghitung AQL.")

    
    
# ------------------------
# Halaman KALKULATOR
# ------------------------
elif page == "Kalkulator AQL":
    st.title("⚖️ Kalkulator AQL")

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
