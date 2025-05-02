import streamlit as st

import math
if page == "Beranda":
    st.markdown("""
        <style>
        .intro-box {
            background-color: #f0f8ff;
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #dce6f1;
        }
        .feature-box {
            background-color: #e6f7e6;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            border: 1px solid #cce0cc;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("📦 Selamat Datang di Kalkulator AQL")
    st.markdown("""
    <div class='intro-box'>
        <h4>🔍 Apa itu AQL?</h4>
        <p>
        <strong>AQL (Acceptable Quality Limit)</strong> adalah standar industri untuk menentukan batas maksimal jumlah cacat yang dapat diterima dalam suatu pengambilan sampel.
        Kalkulator ini membantu Anda mengambil keputusan apakah suatu <em>lot produksi</em> harus <strong>diterima</strong> atau <strong>ditolak</strong> berdasarkan jumlah cacat.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 Fitur Utama")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='feature-box'>
        ✅ Perhitungan cepat berdasarkan nilai AQL<br>
        ✅ Mudah digunakan oleh operator QC<br>
        ✅ Tidak perlu rumus rumit
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-box'>
        📊 Visual & intuitif<br>
        ⚙️ Cocok untuk berbagai ukuran lot<br>
        🏭 Siap digunakan di lingkungan manufaktur
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("👈 **Gunakan menu di samping kiri untuk memulai perhitungan AQL.**")

