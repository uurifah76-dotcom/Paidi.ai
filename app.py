import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Paidi.ai | AI Video Studio",
    page_icon="47836-removebg-preview.png",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. CSS Kustom Profesional
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif !important;
    }
    .stApp { 
        background: linear-gradient(135deg, #050a0f, #101e2b); 
        color: #e0e0e0; 
    }
    h1, h2, h3 { color: #ffffff !important; font-weight: 800 !important; }
    
    .card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.07);
        padding: 30px;
        border-radius: 16px;
        margin-bottom: 24px;
    }
    .promo-banner {
        background: linear-gradient(90deg, #0056b3, #00a8ff);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-bottom: 24px;
        font-weight: 600;
    }
    .profile-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid rgba(0, 123, 255, 0.2);
    }
    
    /* Styling kotak foto profil yang rapi, proporsional, dan tidak oversize */
    .profile-img-container {
        width: 150px;
        border-radius: 12px;
        overflow: hidden;
        margin: 0 auto;
        border: 2px solid #00a8ff;
        box-shadow: 0 4px 15px rgba(0, 168, 255, 0.25);
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.5em;
        background-color: #007bff;
        color: white;
        font-weight: 600;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover { background-color: #0056b3; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigasi
st.sidebar.image("47836-removebg-preview.png", width=80)
st.sidebar.markdown("### Navigasi Sistem")
menu = st.sidebar.radio("", ["Beranda & Studio", "Kredit & Paket", "Program Affiliate", "Akun & Profil"])

# 4. Halaman Beranda & Studio
if menu == "Beranda & Studio":
    # Header Utama
    col1, col2 = st.columns([1, 4.5], vertical_alignment="center")
    with col1: 
        st.image("47836-removebg-preview.png", width=110)
    with col2: 
        st.markdown("<h1 style='margin:0; font-size: 2.2rem;'>Paidi.ai Video Studio</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#00a8ff; font-weight:600; margin-top:5px;'>Ekstraksi Konten Sinematik: Dari Video Panjang ke Reels Viral</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Promo
    st.markdown("""
    <div class="promo-banner">
        🚀 PROMO PELUNCURAN BETA: Klaim 5 Sesi Gratis + Diskon 50% untuk Paket Pro hari ini!
    </div>
    """, unsafe_allow_html=True)

    # Input Form
    st.subheader("🛠️ Studio Pemrosesan")
    link = st.text_input("Tempel Tautan YouTube Anda", placeholder="https://www.youtube.com/watch?v=...")
    
    c1, c2 = st.columns(2)
    with c1: 
        st.selectbox("Durasi Klip", ["Pendek (15-30 detik)", "Standar (30-60 detik)"])
        st.selectbox("Rasio Video", ["9:16 (TikTok/Reels)", "1:1 (Square)", "16:9 (Landscape)"])
    with c2:
        st.selectbox("Resolusi", ["720p HD", "1080p Full HD"])
        st.selectbox("Fokus Konten", ["🔥 Multi-Analisis AI", "Fokus Hook Utama"])
    
    if st.button("✨ Eksekusi Analisis"):
        if link:
            with st.spinner("🚀 AI sedang memproses video..."):
                st.success("Analisis berhasil! Data telah siap.")
        else:
            st.warning("Masukkan tautan YouTube terlebih dahulu.")

    # Profil Founder (Kotak)
    st.subheader("👤 Tentang Founder")
    st.markdown('<div class="profile-box">', unsafe_allow_html=True)
    
    _, col_img, _ = st.columns([1, 1, 1])
    with col_img:
        st.markdown('<div class="profile-img-container">', unsafe_allow_html=True)
        st.image("IMG-20260521-WA0022.jpg", width=150)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("""
        <h3 style="margin-top:15px; margin-bottom:5px;">Usman Shidiq</h3>
        <p style="color:#00a8ff; font-weight:600; margin-bottom:15px;">Founder & CEO of Paidi.ai</p>
        <p style="font-size:0.95em; line-height:1.6; opacity:0.9; max-width: 500px; margin: 0 auto;">
            "Misi kami adalah mendemokratisasi teknologi editing video. Paidi.ai hadir untuk membantu kreator Indonesia memangkas waktu produksi tanpa mengorbankan kualitas konten."
        </p>
    </div>
    """, unsafe_allow_html=True)

# 5. Halaman Tambahan
elif menu == "Kredit & Paket":
    st.markdown("# 💳 Kredit & Paket")
    st.write("Sisa sesi Anda: **5 / 10 Sesi**")

elif menu == "Program Affiliate":
    st.markdown("# 🤝 Program Affiliate")
    st.write("Dapatkan komisi dengan membagikan link referral Anda.")

elif menu == "Akun & Profil":
    st.markdown("# 👤 Akun & Profil")
    st.write("Informasi lengkap akun akan muncul di sini.")
