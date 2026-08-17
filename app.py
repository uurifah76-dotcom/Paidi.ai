import streamlit as st
import base64

# --- FUNGSI UTAMA ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Paidi.ai | AI Video Studio",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- INISIALISASI STATE ---
if "active_menu" not in st.session_state: st.session_state.active_menu = "Beranda"
if "active_tab" not in st.session_state: st.session_state.active_tab = "Buat Klip"

# Menangani navigasi dari query parameter
query_params = st.query_params
if "menu" in query_params:
    st.session_state.active_menu = query_params["menu"][0]

# --- LOAD ASSETS (Pastikan file ada di folder yang sama) ---
img_base64 = get_base64_image("IMG-20260521-WA0022.jpg")
logo_base64 = get_base64_image("47836-removebg-preview.png")

# --- CSS KUSTOM ---
st.markdown(f"""
    <style>
    [data-testid="stHeader"] {{ display: none !important; }}
    [data-testid="stSidebar"] {{ display: none !important; }}
    .block-container {{ padding-top: 1rem !important; padding-bottom: 120px !important; }}
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&display=swap');
    html, body, [class*="st-"] {{ font-family: 'Inter', sans-serif !important; }}
    .stApp {{ background: linear-gradient(135deg, #050a0f, #101e2b); color: #e0e0e0; }}
    
    /* Navbar Bottom */
    .custom-bottom-nav {{
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: rgba(10, 17, 26, 0.98);
        backdrop-filter: blur(15px);
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        display: flex; justify-content: space-around; padding: 10px 5px 15px 5px;
        z-index: 999999;
    }}
    .nav-item {{ text-align: center; color: #a0a0a0; text-decoration: none; font-size: 12px; font-weight: 600; flex: 1; }}
    .nav-item.active {{ color: #00a8ff; }}
    </style>
""", unsafe_allow_html=True)

# --- HEADER LOGO ---
st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <img src="data:image/png;base64,{logo_base64}" style="width: 200px;">
        <h1 style="margin-top: -10px;">Paidi.ai</h1>
        <p style="color: #00a8ff; letter-spacing: 3px;">VIDEO STUDIO</p>
    </div>
""", unsafe_allow_html=True)

# --- LOGIKA KONTEN UTAMA ---
if st.session_state.active_menu == "Beranda":
    # Sub-tabs
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        if st.button("✨ Buat Klip"): st.session_state.active_tab = "Buat Klip"
    with col_t2:
        if st.button("🕒 Klip Saya"): st.session_state.active_tab = "Klip Saya"
    with col_t3:
        if st.button("⚙️ Pengaturan"): st.session_state.active_tab = "Pengaturan"

    if st.session_state.active_tab == "Buat Klip":
        st.info("🚀 PROMO: 5 Sesi Gratis!")
        link = st.text_input("Link YouTube", placeholder="https://youtube.com/...")
        if st.button("Eksekusi Analisis"):
            st.success("Analisis diproses!")
            
    elif st.session_state.active_tab == "Klip Saya":
        st.write("Daftar klip Anda kosong.")

elif st.session_state.active_menu == "Pembayaran":
    st.title("💳 Pembayaran")

elif st.session_state.active_menu == "Affiliate":
    st.title("🤝 Affiliate")

elif st.session_state.active_menu == "Bantuan":
    st.title("❓ Bantuan")

# --- BOTTOM NAV BAR (FIXED) ---
st.markdown(f"""
    <div class="custom-bottom-nav">
        <a href="?menu=Beranda" class="nav-item {'active' if st.session_state.active_menu == 'Beranda' else ''}">🏠<br>Beranda</a>
        <a href="?menu=Pembayaran" class="nav-item {'active' if st.session_state.active_menu == 'Pembayaran' else ''}">💳<br>Pembayaran</a>
        <a href="?menu=Affiliate" class="nav-item {'active' if st.session_state.active_menu == 'Affiliate' else ''}">🤝<br>Affiliate</a>
        <a href="?menu=Bantuan" class="nav-item {'active' if st.session_state.active_menu == 'Bantuan' else ''}">❓<br>Bantuan</a>
    </div>
""", unsafe_allow_html=True)
