import streamlit as st
import base64

# Fungsi untuk konversi gambar lokal ke base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

img_base64 = get_base64_image("IMG-20260521-WA0022.jpg")
logo_base64 = get_base64_image("47836-removebg-preview.png")

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Paidi.ai | AI Video Studio",
    page_icon="47836-removebg-preview.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Inisialisasi Session State
if "active_menu" not in st.session_state:
    st.session_state.active_menu = "Beranda"

if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Buat Klip"

# Tangkap parameter query string manual untuk navigasi bawah agar sinkron
if "menu" in st.query_params:
    val_menu = st.query_params["menu"]
    # Handle jika query param berupa string atau list
    if isinstance(val_menu, list):
        st.session_state.active_menu = val_menu[0]
    else:
        st.session_state.active_menu = val_menu

# 3. CSS Kustom untuk Mengunci Navigasi Bawah Secara Mutlak (Fixed Bottom Navbar)
st.markdown(f"""
    <style>
    [data-testid="stHeader"] {{ display: none !important; }}
    [data-testid="stSidebar"] {{ display: none !important; }}
    
    .block-container {{ 
        padding-top: 0rem !important; 
        margin-top: -20px !important;
        padding-bottom: 120px !important; 
    }}
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&display=swap');
    html, body, [class*="st-"] {{ font-family: 'Inter', sans-serif !important; }}
    .stApp {{ background: linear-gradient(135deg, #050a0f, #101e2b); color: #e0e0e0; }}
    h1, h2, h3 {{ color: #ffffff !important; font-weight: 800 !important; }}
    
    .card {{ background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.07); padding: 30px; border-radius: 16px; margin-bottom: 24px; }}
    .promo-banner {{ background: linear-gradient(90deg, #0056b3, #00a8ff); padding: 20px; border-radius: 12px; text-align: center; color: white; margin-bottom: 24px; font-weight: 600; }}
    .profile-box {{ background: rgba(255, 255, 255, 0.05); padding: 30px; border-radius: 20px; text-align: center; border: 1px solid rgba(0, 123, 255, 0.2); }}
    
    .profile-img-container {{ width: 110px; height: 140px; border-radius: 10px; overflow: hidden; margin: 0 auto 15px auto; border: 2px solid #00a8ff; box-shadow: 0 4px 15px rgba(0, 168, 255, 0.25); }}
    .profile-img-container img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}

    /* Styling tombol tab atas */
    .stButton>button {{ width: 100%; border-radius: 50px; height: 3.2em; background-color: rgba(255, 255, 255, 0.04); color: #ffffff; font-weight: 600; font-size: 14px; border: 1px solid rgba(255, 255, 255, 0.1); }}
    .stButton>button:hover {{ background-color: rgba(0, 168, 255, 0.2); border-color: #00a8ff; color: #00a8ff; }}

    /* Paksa kolom tab atas sejajar menyamping */
    div[data-testid="stHorizontalBlock"] {{
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 8px !important;
    }}
    div[data-testid="stHorizontalBlock"] > div {{
        flex: 1 !important;
        min-width: 0 !important;
    }}

    /* KONTROL UTAMA BOTTOM NAVBAR AGAR FIXED DAN TIDAK BISA TERTUTUP SCROLL */
    .custom-bottom-nav {{
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        width: 100% !important;
        background: rgba(10, 17, 26, 0.98) !important;
        backdrop-filter: blur(15px) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
        display: flex !important;
        justify-content: space-around !important;
        align-items: center !important;
        padding: 10px 5px 15px 5px !important;
        z-index: 9999999 !important;
        box-shadow: 0 -8px 25px rgba(0, 0, 0, 0.8) !important;
    }}
    
    .nav-item {{
        text-align: center;
        color: #a0a0a0;
        text-decoration: none;
        font-size: 12px;
        font-weight: 600;
        flex: 1;
        transition: 0.2s;
    }}
    
    .nav-item.active {{
        color: #00a8ff;
    }}
    
    .nav-item div:first-child {{
        font-size: 20px;
        margin-bottom: 2px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. Header Utama (Logo ditarik ke atas)
st.markdown(f"""
    <div style="text-align: center; margin-top: -65px; margin-bottom: 10px;">
        <div style="margin-bottom: -15px;">
            <img src="data:image/png;base64,{logo_base64}" style="width: 550px; height: auto; filter: drop-shadow(0px 0px 35px rgba(0, 168, 255, 0.35));">
        </div>
        <div style="font-size: 3.5rem; font-weight: 900; color: #ffffff; letter-spacing: -2px; line-height: 1; position: relative; z-index: 2;">
            Paidi.ai
        </div>
        <div style="font-size: 1.2rem; font-weight: 400; color: #00a8ff; margin-top: 2px; letter-spacing: 5px; text-transform: uppercase; position: relative; z-index: 2;">
            Video Studio
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. Konten Berdasarkan Menu Utama
if st.session_state.active_menu == "Beranda":
    
    # Pill Tabs Sejajar Menyamping di Atas Konten (Dilengkapi st.rerun agar langsung merespons)
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        if st.button("✨ Buat Klip", key="btn_buat_klip"):
            st.session_state.active_tab = "Buat Klip"
            st.rerun()
    with col_t2:
        if st.button("🕒 Klip Saya", key="btn_klip_saya"):
            st.session_state.active_tab = "Klip Saya"
            st.rerun()
    with col_t3:
        if st.button("⚙️ Pengaturan", key="btn_pengaturan"):
            st.session_state.active_tab = "Pengaturan"
            st.rerun()

    st.markdown("<p style='text-align: center; color: rgba(255,255,255,0.6); font-size: 0.9rem; margin-top: 10px; margin-bottom: 20px;'>Tempel link, pilih mode, lalu AI proses klipnya.</p>", unsafe_allow_html=True)

    # Isi Berdasarkan Tab Aktif
    if st.session_state.active_tab == "Buat Klip":
        st.markdown("""<div class="promo-banner">🚀 PROMO PELUNCURAN BETA: Klaim 5 Sesi Gratis + Diskon 50% untuk Paket Pro hari ini!</div>""", unsafe_allow_html=True)

        link = st.text_input("Tempel Tautan YouTube Anda", placeholder="https://www.youtube.com/watch?v=...")
        
        c1, c2 = st.columns(2)
        with c1: 
            st.selectbox("Durasi Klip", ["Pendek (15-30 detik)", "Standar (30-60 detik)"])
            st.selectbox("Rasio Video", ["9:16 (TikTok/Reels)", "1:1 (Square)", "16:9 (Landscape)"])
        with c2:
            st.selectbox("Resolusi", ["720p HD", "1080p Full HD"])
            st.selectbox("Fokus Konten", ["🔥 Multi-Analisis AI", "Fokus Hook Utama"])
        
        if st.button("✨ Eksekusi Analisis", key="exec_analisis"):
            if link:
                with st.spinner("🚀 AI sedang memproses video..."):
                    st.success("Analisis berhasil! Data telah siap.")
            else:
                st.warning("Masukkan tautan YouTube terlebih dahulu.")

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("👤 Tentang Founder")
        st.markdown(f"""
        <div class="profile-box">
            <div class="profile-img-container">
                <img src="data:image/jpeg;base64,{img_base64}">
            </div>
            <h3 style="margin-top:10px; margin-bottom:5px;">Usman Shidiq</h3>
            <p style="color:#00a8ff; font-weight:600; margin-bottom:15px;">Founder & CEO of Paidi.ai</p>
            <p style="font-size:0.95em; line-height:1.6; opacity:0.9; max-width: 500px; margin: 0 auto;">
                "Misi kami adalah mendemokratisasi teknologi editing video. Paidi.ai hadir untuk membantu kreator Indonesia memangkas waktu produksi tanpa mengorbankan kualitas konten."
            </p>
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.active_tab == "Klip Saya":
        st.markdown("""
        <div class="card" style="text-align: center; padding: 40px;">
            <h3>🎬 Kamu udah bikin 3 klip 🎉</h3>
            <p style="color: rgba(255,255,255,0.7); margin-top: 10px; margin-bottom: 20px;">
                Kredit kamu habis. Top up untuk bikin 30 klip lagi mulai Rp 19.000, langsung jadi dan bisa kamu posting hari ini.
            </p>
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.active_tab == "Pengaturan":
        st.markdown("""
        <div class="card">
            <h3>⚙️ Pengaturan Akun Studio</h3>
            <p style="color: rgba(255,255,255,0.7);">Kelola konfigurasi API, profil, dan preferensi aplikasi Anda di sini.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 📜 Legalitas & Keamanan Platform")
    st.markdown("""
    <div class="card" style="border-left: 4px solid #00a8ff;">
        <p style="font-size: 14px; line-height: 1.6; margin-bottom: 12px;">
            <strong>Paidi.ai</strong> beroperasi dengan menjunjung tinggi standar legalitas dan pelindungan data pengguna di Indonesia. Seluruh pemrosesan kecerdasan buatan mematuhi regulasi privasi yang berlaku.
        </p>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 14px 0;">
        <p style="font-size: 13px; margin: 0; opacity: 0.9; line-height: 1.6;">
            🛡️ <strong>Kepatuhan Data:</strong> Perlindungan Data Pribadi (UU PDP)<br>
            📄 <strong>Ketentuan Layanan:</strong> Hak Cipta Konten & Kebijakan Penggunaan Wajar (Fair Use AI)<br>
            🔒 <strong>Keamanan:</strong> Enskripsi End-to-End untuk setiap berkas media yang diproses
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🏢 Informasi Korporat & Kontak Resmi")
    st.markdown("""
    <div class="card" style="border-left: 4px solid #007bff; background: rgba(0, 0, 0, 0.2);">
        <p style="font-size: 14px; line-height: 1.6; margin-bottom: 12px;">
            <strong>PT Paidi.ai Group</strong> didirikan pada tahun <strong>2026</strong> di Kota Malang, Jawa Timur oleh <strong>Usman Shidiq</strong>. Kami berkomitmen membangun fondasi perangkat lunak rintisan berbasis kecerdasan buatan untuk revolusi konten digital Indonesia.
        </p>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 14px 0;">
        <p style="font-size: 13px; margin: 0; opacity: 0.9; line-height: 1.6;">
            📍 <strong>Alamat Kantor:</strong> Ruko WOW Sawojajar, Kec. Kedungkandang, Kota Malang, Jawa Timur 65139<br>
            📞 <strong>WhatsApp Korporat:</strong> 083853413171<br>
            ✉️ <strong>Layanan Gmail Resmi:</strong> support@paidi.ai / usmancipanky@gmail.com<br>
            📱 <strong>Media Sosial:</strong> TikTok & Instagram (@Paidi.ai.idn)
        </p>
        <div style="text-align: center; margin-top: 20px; font-size: 12px; opacity: 0.6;">
            © 2026 PT Paidi.ai Group. Hak Cipta Dilindungi Undang-Undang.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_menu == "Pembayaran":
    st.markdown("# 💳 Pembayaran & Paket")
    st.markdown("""
    <div class="card">
        <h3>Sisa Sesi Anda</h3>
        <p style="font-size: 1.5rem; font-weight: bold; color: #00a8ff;">5 / 10 Sesi</p>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 14px 0;">
        <p>Top up paket Anda untuk membuat lebih banyak klip video sinematik berkualitas tinggi.</p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_menu == "Affiliate":
    st.markdown("# 🤝 Program Affiliate")
    st.markdown("""
    <div class="card">
        <h3>Dapatkan Penghasilan Tambahan</h3>
        <p>Bagikan link referral unik Anda kepada kreator lain dan dapatkan komisi menarik dari setiap transaksi yang berhasil.</p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_menu == "Bantuan":
    st.markdown("# ❓ Pusat Bantuan & Kontak")
    st.markdown("""
    <div class="card">
        <h3>Butuh Bantuan?</h3>
        <p>Tim dukungan PT Paidi.ai Group siap membantu Anda melalui WhatsApp resmi di <strong>083853413171</strong> atau melalui email ke <strong>support@paidi.ai</strong>.</p>
    </div>
    """, unsafe_allow_html=True)

# 6. Render Navigasi Bawah Menggunakan HTML Murni agar Benar-Benar Mengambang & Fixed
active_beranda = "active" if st.session_state.active_menu == "Beranda" else ""
active_pembayaran = "active" if st.session_state.active_menu == "Pembayaran" else ""
active_affiliate = "active" if st.session_state.active_menu == "Affiliate" else ""
active_bantuan = "active" if st.session_state.active_menu == "Bantuan" else ""

st.markdown(f"""
    <div class="custom-bottom-nav">
        <a href="?menu=Beranda" target="_self" class="nav-item {active_beranda}">
            <div>🏠</div>
            <div>Beranda</div>
        </a>
        <a href="?menu=Pembayaran" target="_self" class="nav-item {active_pembayaran}">
            <div>💳</div>
            <div>Pembayaran</div>
        </a>
        <a href="?menu=Affiliate" target="_self" class="nav-item {active_affiliate}">
            <div>🤝</div>
            <div>Affiliate</div>
        </a>
        <a href="?menu=Bantuan" target="_self" class="nav-item {active_bantuan}">
            <div>❓</div>
            <div>Bantuan</div>
        </a>
    </div>
""", unsafe_allow_html=True)
