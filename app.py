import streamlit as st
import base64

# --- FUNGSI & STATE ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

# Inisialisasi Session State untuk Pengaturan (Default Value)
if "duration" not in st.session_state: st.session_state.duration = "Pendek (15-30 detik)"
if "ratio" not in st.session_state: st.session_state.ratio = "9:16 (TikTok/Reels)"
if "resolution" not in st.session_state: st.session_state.resolution = "1080p Full HD"
if "focus" not in st.session_state: st.session_state.focus = "🔥 Multi-Analisis AI"

# --- CSS STYLING ---
st.markdown("""
    <style>
    /* ... (CSS sebelumnya tetap sama) ... */
    .custom-bottom-nav { position: fixed; bottom: 0; left: 0; width: 100%; background: rgba(10, 17, 26, 0.98); 
                         border-top: 1px solid rgba(255, 255, 255, 0.1); display: flex; justify-content: space-around; 
                         padding: 10px; z-index: 9999; }
    .nav-link { color: #a0a0a0; text-decoration: none; text-align: center; font-size: 12px; }
    </style>
""", unsafe_allow_html=True)

# --- LOGIKA NAVIGASI ---
if "active_menu" not in st.session_state: st.session_state.active_menu = "Beranda"

# --- KONTEN BERDASARKAN MENU ---
if st.session_state.active_menu == "Beranda":
    st.title("Paidi.ai Studio")
    link = st.text_input("Tempel Tautan YouTube Anda", placeholder="https://youtube.com/...")
    if st.button("✨ Eksekusi Analisis"):
        if link: st.success("Memproses...")
        else: st.warning("Masukkan link dulu!")

elif st.session_state.active_menu == "Pengaturan":
    st.subheader("⚙️ Konfigurasi Klip")
    st.session_state.duration = st.selectbox("Durasi Klip", ["Pendek (15-30 detik)", "Standar (30-60 detik)"], index=["Pendek (15-30 detik)", "Standar (30-60 detik)"].index(st.session_state.duration))
    st.session_state.ratio = st.selectbox("Rasio Video", ["9:16 (TikTok/Reels)", "1:1 (Square)", "16:9 (Landscape)"], index=["9:16 (TikTok/Reels)", "1:1 (Square)", "16:9 (Landscape)"].index(st.session_state.ratio))
    st.session_state.resolution = st.selectbox("Resolusi", ["720p HD", "1080p Full HD"], index=["720p HD", "1080p Full HD"].index(st.session_state.resolution))
    st.session_state.focus = st.selectbox("Fokus Konten", ["🔥 Multi-Analisis AI", "Fokus Hook Utama"], index=["🔥 Multi-Analisis AI", "Fokus Hook Utama"].index(st.session_state.focus))
    st.info("Konfigurasi tersimpan otomatis.")

elif st.session_state.active_menu == "Bantuan":
    st.subheader("❓ Pusat Bantuan")
    st.markdown("Hubungi kami secara langsung:")
    
    # Tombol Aksi Bantuan
    st.link_button("💬 Chat via WhatsApp", "https://wa.me/6283853413171")
    st.link_button("✉️ Email ke Support", "mailto:support@paidi.ai")

# --- BOTTOM NAV BAR (Dengan Redirect Manual) ---
# Menggunakan callback untuk mengubah session_state
def set_menu(menu_name):
    st.session_state.active_menu = menu_name

st.markdown('<div class="custom-bottom-nav">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠 Beranda"): st.session_state.active_menu = "Beranda"; st.rerun()
with col2:
    if st.button("⚙️ Setting"): st.session_state.active_menu = "Pengaturan"; st.rerun()
with col3:
    if st.button("🤝 Affiliate"): st.session_state.active_menu = "Affiliate"; st.rerun()
with col4:
    if st.button("❓ Bantuan"): st.session_state.active_menu = "Bantuan"; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
