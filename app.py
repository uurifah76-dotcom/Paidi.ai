import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Paidi.ai | AI Video Studio",
    page_icon="🤖",
    layout="centered"
)

# 2. Inisialisasi Session State Kredit
if "credits" not in st.session_state:
    st.session_state.credits = 5

# 3. Header Utama Paidi.ai
st.title("Paidi.ai")
st.subheader("AI Video Studio")
st.markdown("Platform otomatisasi video panjang YouTube menjadi klip pendek viral untuk kreator.")
st.markdown(f"**Sisa Kredit Anda:** ⚡ {st.session_state.credits} Kredit")

st.divider()

# 4. Navigasi Utama Menggunakan Tab Native Streamlit
tab_beranda, tab_klip, tab_pengaturan, tab_pembayaran, tab_affiliate, tab_bantuan = st.tabs([
    "🏠 Beranda", 
    "🕒 Klip Saya", 
    "⚙️ Pengaturan", 
    "💳 Pembayaran", 
    "🤝 Affiliate", 
    "❓ Bantuan"
])

with tab_beranda:
    st.markdown("### Buat Klip AI Baru")
    
    # Form Input Link YouTube
    link = st.text_input("Tempel Tautan YouTube Anda", placeholder="https://youtube.com/watch?v=...")
    
    col1, col2 = st.columns(2)
    with col1:
        durasi = st.selectbox("Durasi Klip", ["Standar (30-60 detik)", "Pendek (15-30 detik)"])
    with col2:
        rasio = st.selectbox("Rasio Video", ["9:16 (TikTok/Reels)", "16:9 (Landscape)"])

    if st.button("✨ Eksekusi Analisis Klip", type="primary", use_container_width=True):
        if st.session_state.credits <= 0:
            st.warning("Kredit Anda habis! Silakan lakukan top up melalui menu Pembayaran.")
        elif link:
            with st.spinner("Paidi.ai sedang memproses video..."):
                st.success("Klip berhasil dibuat dan siap diunduh!")
        else:
            st.warning("Silakan masukkan tautan YouTube terlebih dahulu.")

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # Informasi Legalitas & Founder untuk Kepercayaan Audiens
    st.markdown("### 🏛️ Informasi Legalitas Perusahaan")
    st.markdown("""
    **PT Paidi Inovasi Teknologi Indonesia**  
    Terdaftar resmi dan dilindungi hukum Republik Indonesia.  
    NIB: 9123000xxxxx | Kantor Pusat: Jakarta, Indonesia.
    """)

    st.markdown("### 👑 Pimpinan & Pendiri")
    st.markdown("""
    **Founder & CEO:** Paidi S.Kom., M.T.  
    Berdedikasi menghadirkan solusi teknologi kecerdasan buatan (AI) terdepan bagi seluruh kreator konten di Indonesia.
    """)

with tab_klip:
    st.header("Daftar Klip Tersimpan")
    st.info("Belum ada klip yang dirender. Buat klip pertamamu melalui tab Beranda.")

with tab_pengaturan:
    st.header("Pengaturan Studio AI")
    st.selectbox("Kualitas Video Output", ["1080p Full HD", "720p HD", "4K Ultra"])
    st.selectbox("Bahasa Auto-Subtitle", ["Indonesia", "English"])
    st.success("Pengaturan tersimpan otomatis.")

with tab_pembayaran:
    st.header("Top Up Paket Kredit")
    st.markdown("""
    **Paket Kreator Pro**  
    Akses penuh fitur AI tanpa batas watermark — **Rp 29.000**
    """)
    if st.button("Beli Paket Sekarang", type="primary"):
        st.session_state.credits += 50
        st.success("Berhasil menambah 50 kredit!")
        st.rerun()

with tab_affiliate:
    st.header("Program Affiliate Paidi.ai")
    st.markdown("Dapatkan komisi **30%** dari setiap kreator yang bergabung melalui tautan undangan unik Anda.")

with tab_bantuan:
    st.header("Pusat Bantuan & Dukungan")
    st.markdown("Butuh bantuan teknis atau kendala top up? Hubungi tim support kami.")
    st.link_button("💬 Chat WhatsApp Dukungan CS", "https://wa.me/6283853413171", use_container_width=True)
