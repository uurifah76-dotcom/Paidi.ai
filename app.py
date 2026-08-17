import streamlit as st
import base64

# 1. Konfigurasi Halaman (Light Mode ala SaaS Modern & KlipAja.id)
st.set_page_config(
    page_title="Paidi.ai | AI Video Studio",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Inisialisasi Session State
if "active_menu" not in st.session_state: st.session_state.active_menu = "Beranda"
if "active_tab" not in st.session_state: st.session_state.active_tab = "Buat Klip"
if "credits" not in st.session_state: st.session_state.credits = 0  # Sesuaikan dengan database Anda

# Cek parameter query string untuk navigasi bawah
query_params = st.query_params
if "menu" in query_params:
    st.session_state.active_menu = query_params["menu"]

# 3. CSS Kustom Full Meniru Konsep KlipAja.id
st.markdown("""
    <style>
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }
    
    .block-container { 
        padding-top: 1rem !important; 
        padding-bottom: 110px !important; 
        max-width: 600px !important;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif !important; }
    .stApp { background-color: #fcfcfc; color: #111827; }
    
    /* Top Header */
    .top-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0 15px 0;
        margin-bottom: 15px;
        border-bottom: 1px solid #f3f4f6;
    }
    .brand-logo {
        font-size: 1.4rem;
        font-weight: 800;
        color: #111827;
        text-decoration: none;
        display: flex;
        align-items: center;
        letter-spacing: -0.5px;
    }
    .brand-logo span { color: #f59e0b; } /* Warna kuning/emas khas KlipAja */
    
    .header-right {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .credit-badge {
        background: #fffbeb;
        color: #d97706;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid #fde68a;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .user-avatar {
        background: #111827;
        color: white;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.9rem;
    }

    /* Cards */
    .card-box {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 16px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    }
    
    .promo-card {
        background: #fffbeb;
        border: 1px solid #fde68a;
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 20px;
    }

    /* Fixed Bottom Navigation Bar */
    .custom-bottom-nav {
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        width: 100% !important;
        background: #ffffff !important;
        border-top: 1px solid #e5e7eb !important;
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
        color: #f59e0b;
    }
    .nav-item div:first-child {
        font-size: 20px;
        margin-bottom: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# 4. Header Atas Paidi.ai
st.markdown(f"""
    <div class="top-header">
        <a href="?menu=Beranda" target="_self" class="brand-logo">
            Paidi<span>.ai</span>
        </a>
        <div class="header-right">
            <div class="credit-badge">⚡ {st.session_state.credits}</div>
            <div class="user-avatar">P</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Tombol simulasi testing kredit
col_sim1, col_sim2 = st.columns(2)
with col_sim1:
    if st.button("Simulasi: Kredit Habis (0)"):
        st.session_state.credits = 0
        st.rerun()
with col_sim2:
    if st.button("Simulasi: Ada Kredit (3)"):
        st.session_state.credits = 3
        st.rerun()

# 5. Routing Halaman Berdasarkan Menu Utama
if st.session_state.active_menu == "Beranda":
    
    # Sub-tabs Horizontal Sejajar dari Kiri ke Kanan (Gaya KlipAja)
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

    if st.session_state.active_tab == "Buat Klip":
        
        # PROMOSI / NOTIFIKASI KREDIT HABIS Khas KlipAja
        if st.session_state.credits == 0:
            st.markdown("""
                <div class="promo-card">
                    <h3 style="margin-top:0; color:#b45309; font-size:1.15rem;">Kredit Paidi kamu habis! 🎉</h3>
                    <p style="color: #78350f; font-size: 0.88rem; line-height: 1.5; margin-bottom: 15px;">
                        Top up sekarang untuk melanjutkan pembuatan konten AI Anda. Proses instan dan siap diposting.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("⚡ Top up untuk bikin lagi", key="btn_topup_redirect", use_container_width=True):
                st.session_state.active_menu = "Pembayaran"
                st.rerun()
            st.markdown("<br>", unsafe_allow_html=True)

        # Form Input Link YouTube
        st.markdown("### Tempel Link YouTube", unsafe_allow_html=True)
        link = st.text_input("Tempel Tautan YouTube Anda", placeholder="https://youtube.com/watch?v=...", label_visibility="collapsed")
        
        if st.button("✨ Eksekusi Analisis", key="exec_main", use_container_width=True):
            if st.session_state.credits <= 0:
                st.warning("Kredit Anda habis! Silakan lakukan Top Up terlebih dahulu.")
            elif link:
                with st.spinner("Paidi.ai sedang memproses video..."):
                    st.success("Analisis selesai dan klip berhasil dibuat!")
            else:
                st.warning("Masukkan tautan YouTube terlebih dahulu.")

        st.markdown("<hr style='border: 0; border-top: 1px solid #f3f4f6; margin: 25px 0;'>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 0.85rem;'>atau mulai dari video populer</p>", unsafe_allow_html=True)
        
        # Contoh List Video Populer
        videos = [
            ("Bedah Isi Otak Dibalik Bisnis Trili...", "Sulianto Indria Putra"),
            ("Bapak Anak Suka Investasi", "Raditya Dika"),
            ("Live Trading 5 Miliar, Jadi Berapa...", "Sulianto Indria Putra")
        ]
        for title, channel in videos:
            st.markdown(f"""
                <div class="card-box" style="padding: 12px 16px; display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
                    <div style="background: #f3f4f6; width: 70px; height: 45px; border-radius: 8px; flex-shrink: 0;"></div>
                    <div>
                        <div style="font-weight: 600; font-size: 0.9rem; color: #111827;">{title}</div>
                        <div style="font-size: 0.75rem; color: #9ca3af;">{channel}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    elif st.session_state.active_tab == "Klip Saya":
        st.markdown("""
            <div class="card-box" style="text-align: center; padding: 40px 20px;">
                <h3>🎬 Daftar Klip Anda</h3>
                <p style="color: #9ca3af; font-size: 0.9rem;">Belum ada klip yang dirender. Mulai buat klip pertamamu!</p>
            </div>
        """, unsafe_allow_html=True)

    elif st.session_state.active_tab == "Pengaturan":
        st.markdown("### ⚙️ Pengaturan Studio & AI")
        st.selectbox("Durasi Klip", ["Pendek (15-30 detik)", "Standar (30-60 detik)"])
        st.selectbox("Rasio Video", ["9:16 (TikTok/Reels)", "1:1 (Square)", "16:9 (Landscape)"])
        st.selectbox("Resolusi", ["720p HD", "1080p Full HD"])
        st.success("Konfigurasi tersimpan otomatis.")

elif st.session_state.active_menu == "Pembayaran":
    st.markdown("<h2>Top Up Kredit</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6b7280; font-size: 0.9rem;'>Beli kredit untuk memproses video YouTube di Paidi.ai.</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="card-box">
            <div style="font-size: 0.85rem; color: #6b7280;">Saldo Kredit Anda</div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #f59e0b; margin: 5px 0;">{st.session_state.credits} kredit</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Pilih Paket", unsafe_allow_html=True)
    st.markdown("""
        <div class="card-box" style="border: 2px solid #f59e0b;">
            <h3 style="margin: 0; color: #111827;">Paket Kreator Pro</h3>
            <p style="color: #6b7280; font-size: 0.85rem; margin: 5px 0 15px 0;">Cocok untuk konten kreator aktif</p>
            <div style="font-size: 1.5rem; font-weight: 800; color: #111827; margin-bottom: 15px;">Rp 29.000</div>
            <ul style="padding-left: 20px; font-size: 0.85rem; color: #4b5563; line-height: 1.8; margin-bottom: 20px;">
                <li>50 Kredit AI Video</li>
                <li>Tanpa Watermark</li>
                <li>Subtitle Karaoke Otomatis</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Beli Paket Pro", key="buy_pro", use_container_width=True):
        st.session_state.credits += 50
        st.success("Berhasil Top Up 50 Kredit!")
        st.rerun()

elif st.session_state.active_menu == "Affiliate":
    st.markdown("<h2>Affiliate Paidi.ai</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6b7280; font-size: 0.9rem;'>Ajak kreator lain dan dapatkan komisi menarik.</p>", unsafe_allow_html=True)
    st.markdown("""
        <div class="card-box" style="text-align: center; padding: 30px;">
            <div style="font-size: 2rem; font-weight: 900; color: #111827;">20% - 30%</div>
            <p style="color: #6b7280; font-size: 0.85rem; margin-top: 10px;">
                Komisi dari setiap top-up pertama kreator yang Anda undang ke platform Paidi.ai.
            </p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_menu == "Bantuan":
    st.markdown("<h2>Pusat Bantuan</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6b7280; font-size: 0.9rem;'>Hubungi tim dukungan Paidi.ai.</p>", unsafe_allow_html=True)
    
    st.link_button("💬 Chat WhatsApp CS", "https://wa.me/6283853413171", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div class="card-box" style="text-align: center; padding: 25px;">
            <div style="font-size: 1rem; font-weight: 700; color: #111827; margin-bottom: 8px;">Butuh Panduan Lain?</div>
            <p style="color: #6b7280; font-size: 0.85rem;">Tim kami siap membantu kendala teknis atau pertanyaan Anda.</p>
        </div>
    """, unsafe_allow_html=True)

# 6. Render Navigasi Bawah Mengambang Ala KlipAja
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
