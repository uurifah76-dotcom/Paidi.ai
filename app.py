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
    layout="centered"
)

# 2. CSS Kustom - Menghilangkan jarak bawaan Streamlit di bagian atas
st.markdown(f"""
    <style>
    [data-testid="stHeader"] {{ display: none !important; }}
    /* Mengurangi jarak kosong di bagian paling atas aplikasi */
    .block-container {{ padding-top: 1rem !important; }}
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&display=swap');
    html, body, [class*="st-"] {{ font-family: 'Inter', sans-serif !important; }}
    .stApp {{ background: linear-gradient(135deg, #050a0f, #101e2b); color: #e0e0e0; }}
    
    .card {{ background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.07); padding: 30px; border-radius: 16px; margin-bottom: 24px; }}
    .promo-banner {{ background: linear-gradient(90deg, #0056b3, #00a8ff); padding: 20px; border-radius: 12px; text-align: center; color: white; margin-bottom: 24px; font-weight: 600; }}
    .profile-box {{ background: rgba(255, 255, 255, 0.05); padding: 30px; border-radius: 20px; text-align: center; border: 1px solid rgba(0, 123, 255, 0.2); }}
    
    .stButton>button {{ width: 100%; border-radius: 10px; height: 3.5em; background-color: #007bff; color: white; font-weight: 600; font-size: 16px; border: none; }}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
st.sidebar.image("47836-removebg-preview.png", width=80)
menu = st.sidebar.radio("Navigasi", ["Beranda & Studio", "Kredit & Paket", "Program Affiliate", "Akun & Profil"])

# 4. Halaman Beranda
if menu == "Beranda & Studio":
    # Header dengan Logo 450px dan posisi diangkat ke atas
    st.markdown(f"""
        <div style="text-align: center; margin-top: -30px; margin-bottom: 20px;">
            <div style="margin-bottom: 5px;">
                <img src="data:image/png;base64,{logo_base64}" style="width: 450px; height: auto; filter: drop-shadow(0px 0px 30px rgba(0, 168, 255, 0.3));">
            </div>
            <div style="font-size: 3.5rem; font-weight: 900; color: #ffffff; letter-spacing: -2px; line-height: 1;">
                Paidi.ai
            </div>
            <div style="font-size: 1.2rem; font-weight: 400; color: #00a8ff; margin-top: 5px; letter-spacing: 5px; text-transform: uppercase;">
                Video Studio
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""<div class="promo-banner">🚀 PROMO PELUNCURAN BETA: Klaim 5 Sesi Gratis!</div>""", unsafe_allow_html=True)

    # Input & Konten Lainnya...
    link = st.text_input("Tempel Tautan YouTube Anda", placeholder="https://www.youtube.com/watch?v=...")
    
    # [Tambahkan sisa komponen studio Anda di sini sesuai kode sebelumnya]
    if st.button("✨ Eksekusi Analisis"):
        st.success("Analisis diproses!")
