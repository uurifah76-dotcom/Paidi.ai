import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Paidi.ai | AI Video Studio",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Inisialisasi Session State (Termasuk Konfigurasi Pengaturan)
if "active_menu" not in st.session_state: 
    st.session_state.active_menu = "Beranda"
if "active_tab" not in st.session_state: 
    st.session_state.active_tab = "Buat Klip"
if "credits" not in st.session_state: 
    st.session_state.credits = 5  # Contoh sisa kredit default

# State untuk konfigurasi pengaturan
if "cfg_durasi" not in st.session_state: st.session_state.cfg_durasi = "Standar (30-60 detik)"
if "cfg_rasio" not in st.session_state: st.session_state.cfg_rasio = "9:16 (TikTok/Reels)"
if "cfg_resolusi" not in st.session_state: st.session_state.cfg_resolusi = "1080p Full HD"

# Tangkap navigasi dari query parameter bawah jika ada
query_params = st.query_params
if "menu" in query_params:
    st.session_state.active_menu = query_params["menu"]

# 3. CSS Kustom Sesuai Tampilan Dark Mode
st.markdown("""
    <style>
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }
    
    .block-container { 
        padding-top: 1rem !important; 
        padding-bottom: 110px !important; 
        max-width: 600px !important;
        background-color: #0b0f19;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif !important; }
    .stApp { background-color: #0b0f19; color: #ffffff; }

    /* Card Styling */
    .card-box {
        background: #111827;
        border: 1px solid #1f2937;
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 16px;
    }

    /* Fixed Bottom Navigation Bar */
    .custom-bottom-nav {
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        width: 100% !important;
        background: #0b0f19 !important;
        border-top: 1px solid #1f2937 !important;
        display: flex !important;
        justify-content: space-around !important;
        align-items: center !important;
        padding: 10px 0 15px 0 !important;
        z-index: 999999 !important;
    }
    .nav-item {
        text-align: center;
        color: #9ca3af;
        text-decoration: none;
        font-size: 11px;
        font-weight: 600;
        flex: 1;
    }
    .nav-item.active {
        color: #38bdf8;
    }
    .nav-item div:first-child {
        font-size: 20px;
        margin-bottom: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# 4. Header Logo & Studio Title
st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="color: #ffffff; font-size: 2rem; font-weight: 800; margin-bottom: 0;">Paidi<span style="color: #38bdf8;">.ai</span></h1>
        <p style="color: #38bdf8; font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-top: 5px;">Video Studio</p>
    </div>
""", unsafe_allow_html=True)

# 5. Logika Navigasi Berdasarkan Menu Utama
if st.session_state.active_menu == "Beranda":
    
    # Tombol Tab Horizontal Sejajar dari Kiri ke Kanan
    st1, st2, st3 = st.columns(3)
    with st1:
        btn_type_1 = "primary" if st.session_state.active_tab == "Buat Klip" else "secondary"
        if st.button("✨ Buat Klip", key="tb_buat", use_container_width=True, type=btn_type_1): 
            st.session_state.active_tab = "Buat Klip"
            st.rerun()
    with st2:
        btn_type_2 = "primary" if st.session_state.active_tab == "Klip Saya" else "secondary"
        if st.button("🕒 Klip Saya", key="tb_klip", use_container_width=True, type=btn_type_2): 
            st.session_state.active_tab = "Klip Saya"
            st.rerun()
    with st3:
        btn_type_3 = "primary" if st.session_state.active_tab == "Pengaturan" else "secondary"
        if st.button("⚙️ Pengaturan", key="tb_set", use_container_width=True, type=btn_type_3): 
            st.session_state.active_tab = "Pengaturan"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Konten Berdasarkan Tab yang Aktif
    if st.session_state.active_tab == "Buat Klip":
        
        # Banner Promo / Kredit
        if st.session_state.credits <= 0:
            st.markdown("""
                <div style="background: linear-gradient(135deg, #0369a1, #0284c7); padding: 20px; border-radius: 16px; margin-bottom: 20px;">
                    <h3 style="color: white; margin-top:0; font-size: 1.1rem;">⚡ Kredit Paidi kamu habis!</h3>
                    <p style="color: #e0f2fe; font-size: 0.85rem;">Top up sekarang untuk melanjutkan pembuatan klip AI.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Top Up Sekarang", use_container_width=True):
                st.session_state.active_menu = "Pembayaran"
                st.rerun()
        else:
            st.markdown("""
                <div style="background: linear-gradient(135deg, #0284c7, #2563eb); padding: 18px; border-radius: 16px; margin-bottom: 20px;">
                    <h4 style="color: white; margin: 0; font-size: 0.95rem;">🚀 PROMO PELUNCURAN BETA</h4>
                    <p style="color: #e0f2fe; font-size: 0.8rem; margin: 5px 0 0 0;">Klaim Sesi Gratis + Diskon 50% untuk Paket Pro hari ini!</p>
                </div>
            """, unsafe_allow_html=True)

        # Form Input Link YouTube
        st.markdown("<p style='color: #9ca3af; font-size: 0.85rem; margin-bottom: 5px;'>Tempel Tautan YouTube Anda</p>", unsafe_allow_html=True)
        link = st.text_input("Link YouTube", placeholder="https://youtube.com/watch?v=...", label_visibility="collapsed")
        
        # Ringkasan konfigurasi aktif saat ini
        st.markdown(f"""
            <div style="font-size: 0.75rem; color: #9ca3af; margin: 10px 0 15px 0;">
                🛠️ Mode Aktif: <span style="color: #38bdf8;">{st.session_state.cfg_durasi}</span> | <span style="color: #38bdf8;">{st.session_state.cfg_rasio}</span>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("✨ Eksekusi Analisis Klip", use_container_width=True):
            if st.session_state.credits <= 0:
                st.warning("Kredit Anda habis! Silakan lakukan top up.")
            elif link:
                with st.spinner("Paidi.ai sedang memproses video..."):
                    st.success("Klip berhasil dibuat berdasarkan pengaturan Anda!")
            else:
                st.warning("Silakan masukkan tautan YouTube terlebih dahulu.")

        # ==========================================
        # BAGIAN INFORMASI PERUSAHAAN & FOUNDER
        # ==========================================
        st.markdown("<br><hr style='border: 0; border-top: 1px solid #1f2937; margin: 25px 0;'>", unsafe_allow_html=True)
        
        st.markdown("""
            <div class="card-box" style="text-align: left;">
                <h4 style="color: #ffffff; font-size: 1rem; margin-top: 0; margin-bottom: 8px;">🏛️ Informasi Legalitas Perusahaan</h4>
                <p style="color: #9ca3af; font-size: 0.8rem; line-height: 1.6; margin-bottom: 0;">
                    <b>PT Paidi Inovasi Teknologi Indonesia</b><br>
                    Terdaftar resmi dan dilindungi hukum Republik Indonesia.<br>
                    NIB: 9123000xxxxx | Kantor Pusat: Jakarta, Indonesia.
                </p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="card-box" style="text-align: left;">
                <h4 style="color: #ffffff; font-size: 1rem; margin-top: 0; margin-bottom: 8px;">👑 Pimpinan & Pendiri</h4>
                <p style="color: #9ca3af; font-size: 0.8rem; line-height: 1.6; margin-bottom: 0;">
                    <b>Founder & CEO:</b> Paidi S.Kom., M.T.<br>
                    Berdedikasi menghadirkan solusi teknologi kecerdasan buatan (AI) terdepan bagi seluruh kreator konten di Indonesia.
                </p>
            </div>
        """, unsafe_allow_html=True)

    elif st.session_state.active_tab == "Klip Saya":
        st.markdown("""
            <div class="card-box" style="text-align: center; padding: 30px;">
                <h3 style="color: #ffffff; font-size: 1.1rem;">Daftar Klip Tersimpan</h3>
                <p style="color: #9ca3af; font-size: 0.85rem;">Belum ada klip yang dirender. Buat klip pertamamu melalui tab "Buat Klip".</p>
            </div>
        """, unsafe_allow_html=True)

    elif st.session_state.active_tab == "Pengaturan":
        st.markdown("""<div class="card-box">""", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #ffffff; font-size: 1.1rem; margin-top:0;'>⚙️ Pengaturan Studio AI</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #9ca3af; font-size: 0.8rem;'>Konfigurasi di bawah ini akan otomatis diterapkan saat Anda memproses klip baru.</p>", unsafe_allow_html=True)
        
        # Input Pengaturan yang tersimpan ke Session State
        st.session_state.cfg_durasi = st.selectbox(
            "Durasi Klip", 
            ["Pendek (15-30 detik)", "Standar (30-60 detik)", "Panjang (60-90 detik)"],
            index=["Pendek (15-30 detik)", "Standar (30-60 detik)", "Panjang (60-90 detik)"].index(st.session_state.cfg_durasi)
        )
        
        st.session_state.cfg_rasio = st.selectbox(
            "Rasio Video", 
            ["9:16 (TikTok/Reels)", "1:1 (Square)", "16:9 (Landscape)"],
            index=["9:16 (TikTok/Reels)", "1:1 (Square)", "16:9 (Landscape)"].index(st.session_state.cfg_rasio)
        )
        
        st.session_state.cfg_resolusi = st.selectbox(
            "Resolusi Hasil", 
            ["720p HD", "1080p Full HD", "4K Ultra"],
            index=["720p HD", "1080p Full HD", "4K Ultra"].index(st.session_state.cfg_resolusi)
        )
        
        st.success("✨ Konfigurasi tersimpan otomatis.")
        st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.active_menu == "Pembayaran":
    st.markdown("<h2 style='color: white; font-size: 1.3rem;'>Top Up Paket Kredit</h2>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="card-box">
            <p style="color: #9ca3af; margin:0; font-size: 0.85rem;">Sisa Kredit Anda</p>
            <h2 style="color: #38bdf8; margin: 5px 0 0 0;">⚡ {st.session_state.credits} Kredit</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="card-box" style="border: 2px solid #0284c7;">
            <h3 style="color: white; margin-top: 0;">Paket Kreator Pro</h3>
            <p style="color: #9ca3af; font-size: 0.85rem;">Akses penuh fitur AI tanpa batas watermark.</p>
            <h2 style="color: #38bdf8; margin: 10px 0;">Rp 29.000</h2>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Beli Paket Sekarang", use_container_width=True):
        st.session_state.credits += 50
        st.success("Berhasil menambah 50 kredit!")
        st.rerun()

elif st.session_state.active_menu == "Affiliate":
    st.markdown("<h2 style='color: white; font-size: 1.3rem;'>Program Affiliate</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="card-box" style="text-align: center;">
            <h1 style="color: #38bdf8; margin: 0;">30%</h1>
            <p style="color: #9ca3af; font-size: 0.85rem; margin-top: 10px;">Komisi dari setiap kreator yang bergabung melalui tautan undangan Anda.</p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_menu == "Bantuan":
    st.markdown("<h2 style='color: white; font-size: 1.3rem;'>Pusat Bantuan</h2>", unsafe_allow_html=True)
    st.link_button("💬 Chat WhatsApp Dukungan CS", "https://wa.me/6283853413171", use_container_width=True)

# 6. Render Navigasi Bawah
active_b = "active" if st.session_state.active_menu == "Beranda" else ""
active_p = "active" if st.session_state.active_menu == "Pembayaran" else ""
active_a = "active" if st.session_state.active_menu == "Affiliate" else ""
active_h = "active" if st.session_state.active_menu == "Bantuan" else ""

st.markdown(f"""
    <div class="custom-bottom-nav">
        <a href="?menu=Beranda" target="_self" class="nav-item {active_b}">
            <div>🏠</div>
            <div>Beranda</div>
        </a>
        <a href="?menu=Pembayaran" target="_self" class="nav-item {active_p}">
            <div>💳</div>
            <div>Pembayaran</div>
        </a>
        <a href="?menu=Affiliate" target="_self" class="nav-item {active_a}">
            <div>🤝</div>
            <div>Affiliate</div>
        </a>
        <a href="?menu=Bantuan" target="_self" class="nav-item {active_h}">
            <div>❓</div>
            <div>Bantuan</div>
        </a>
    </div>
""", unsafe_allow_html=True)
