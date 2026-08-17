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
    initial_sidebar_state="expanded"
)

# 2. CSS Kustom
st.markdown(f"""
    <style>
    /* Hapus paksa teks navigasi otomatis */
    [data-testid="stHeader"] {{ display: none !important; }}
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="st-"] {{
        font-family: 'Inter', sans-serif !important;
    }}
    .stApp {{ 
        background: linear-gradient(135deg, #050a0f, #101e2b); 
        color: #e0e0e0; 
    }}
    h1, h2, h3 {{ color: #ffffff !important; font-weight: 800 !important; }}
    
    .card {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.07);
        padding: 30px;
        border-radius: 16px;
        margin-bottom: 24px;
    }}
    .promo-banner {{
        background: linear-gradient(90deg, #0056b3, #00a8ff);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-bottom: 24px;
        font-weight: 600;
    }}
    .profile-box {{
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid rgba(0, 123, 255, 0.2);
    }}
    
    .profile-img-container {{
        width: 110px;
        height: 140px;
        border-radius: 10px;
        overflow: hidden;
        margin: 0 auto 15px auto;
        border: 2px solid #00a8ff;
        box-shadow: 0 4px 15px rgba(0, 168, 255, 0.25);
    }}
    .profile-img-container img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }}

    .stButton>button {{
        width: 100%;
        border-radius: 10px;
        height: 3.5em;
        background-color: #007bff;
        color: white;
        font-weight: 600;
        font-size: 16px;
        border: none;
    }}
    .stButton>button:hover {{ background-color: #0056b3; }}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
st.sidebar.image("47836-removebg-preview.png", width=80)
st.sidebar.markdown("### Navigasi Sistem")
menu = st.sidebar.radio("", ["Beranda & Studio", "Kredit & Paket", "Program Affiliate", "Akun & Profil"])

# 4. Halaman Beranda & Studio
if menu == "Beranda & Studio":
    # Header: Logo P diperbesar melebihi teks, digeser ke kanan, diposisikan agak ke atas dan ke tengah
    st.markdown(f"""
        <div style="display: flex; align-items: flex-end; gap: 8px; margin-top: -10px; margin-bottom: 5px; flex-wrap: wrap; justify-content: center; text-align: center;">
            <img src="data:image/png;base64,{logo_base64}" style="height: 75px; margin-bottom: -4px;">
            <span style="font-size: 2.5rem; font-weight: 800; color: #ffffff; letter-spacing: -1px; line-height: 1;">aidai.ai</span>
        </div>
        <div style="font-size: 2.3rem; font-weight: 800; color: #ffffff; margin-bottom: 8px; letter-spacing: -1px; line-height: 1.1; text-align: center;">
            Video Studio
        </div>
        <p style='color:#00a8ff; font-weight:700; font-size: 1.05rem; margin-top:0px; margin-bottom: 25px; text-align: center;'>
            Ekstraksi Konten Sinematik
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="promo-banner">
        🚀 PROMO PELUNCURAN BETA: Klaim 5 Sesi Gratis + Diskon 50% untuk Paket Pro hari ini!
    </div>
    """, unsafe_allow_html=True)

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

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🏢 Informasi Korporat & Kontak Resmi")
    st.markdown("""
    <div class="card" style="border-left: 4px solid #007bff;">
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
    </div>
    """, unsafe_allow_html=True)

elif menu == "Kredit & Paket":
    st.markdown("# 💳 Kredit & Paket")
    st.write("Sisa sesi Anda: **5 / 10 Sesi**")

elif menu == "Program Affiliate":
    st.markdown("# 🤝 Program Affiliate")
    st.write("Dapatkan komisi dengan membagikan link referral Anda.")

elif menu == "Akun & Profil":
    st.markdown("# 👤 Akun & Profil")
    st.write("Informasi lengkap akun akan muncul di sini.")
