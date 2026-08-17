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

# State untuk pengaturan video/ekstraksi (agar tersimpan di menu Pengaturan)
if "setting_subtitle" not in st.session_state: st.session_state.setting_subtitle = True
if "setting_headline" not in st.session_state: st.session_state.setting_headline = True
if "setting_rasio" not in st.session_state: st.session_state.setting_rasio = "9:16 (TikTok/Reels)"
if "setting_resolusi" not in st.session_state: st.session_state.setting_resolusi = "1080p Full HD"
if "setting_durasi" not in st.session_state: st.session_state.setting_durasi = "Standar (30-60 detik)"
if "setting_fokus" not in st.session_state: st.session_state.setting_fokus = "Golden moment"

# Tangkap parameter query string manual untuk navigasi bawah agar sinkron
if "menu" in st.query_params:
    val_menu = st.query_params["menu"]
    if isinstance(val_menu, list):
        st.session_state.active_menu = val_menu[0]
    else:
        st.session_state.active_menu = val_menu

# 3. CSS Kustom untuk Mengunci Navigasi Bawah Secara Mutlak & Styling Komponen
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

    /* Styling tombol tab atas secara umum */
    .stButton>button {{ width: 100%; border-radius: 50px; height: 3.2em; background-color: rgba(255, 255, 255, 0.04); color: #ffffff; font-weight: 600; font-size: 14px; border: 1px solid rgba(255, 255, 255, 0.1); transition: all 0.2s ease; }}
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

    /* KONTROL UTAMA BOTTOM NAVBAR AGAR FIXED */
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
    
    # Pill Tabs Atas dengan logika Callback langsung memperbarui state tab
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

    # --- ISI TAB ATAS 1: BUAT KLIP ---
    if st.session_state.active_tab == "Buat Klip":
        st.markdown("""<div class="promo-banner">🚀 PROMO PELUNCURAN BETA: Klaim 5 Sesi Gratis + Diskon 50% untuk Paket Pro hari ini!</div>""", unsafe_allow_html=True)

        link = st.text_input("Tempel Tautan YouTube Anda", placeholder="https://www.youtube.com/watch?v=...")
        
        st.info(f"💡 Konfigurasi Aktif Saat Ini (dari Pengaturan): Rasio **{st.session_state.setting_rasio}**, Resolusi **{st.session_state.setting_resolusi}**, Durasi **{st.session_state.setting_durasi}**, Fokus **{st.session_state.setting_fokus}**.")
        
        if st.button("✨ Eksekusi Analisis & Ekstrak AI", key="exec_analisis"):
            if link:
                with st.spinner("🚀 AI sedang membaca video & mendeteksi bagian terbaik..."):
                    st.success("Analisis berhasil! AI telah mendeteksi momen terbaik. Cek tab 'Klip Saya' untuk melihat hasilnya.")
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

    # --- ISI TAB ATAS 2: KLIP SAYA (Maksimal 3 Klip untuk Free User) ---
    elif st.session_state.active_tab == "Klip Saya":
        st.markdown("### 🎬 Hasil Ekstraksi Klip AI (Free User: 3/3 Klip Siap)")
        st.markdown("<p style='color: rgba(255,255,255,0.7); font-size: 0.9rem;'>Berikut adalah hasil potongan video siap unduh lengkap dengan analisis potensi viral, caption, dan hashtag.</p>", unsafe_allow_html=True)

        # Klip 1
        st.markdown("""
        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h4 style="margin: 0; color: #00a8ff;">🔥 Klip #1: Momen Paling Mengejutkan</h4>
                <span style="background: rgba(0, 168, 255, 0.2); color: #00a8ff; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold;">Potensi FYP: 96% (Sangat Tinggi)</span>
            </div>
            <p style="font-size: 13px; color: rgba(255,255,255,0.7);">Durasi: 0:45 detik | Format: 9:16 Siap Upload</p>
            <div style="background: rgba(0,0,0,0.4); padding: 15px; border-radius: 8px; margin: 10px 0;">
                <p style="margin: 0 0 8px 0; font-size: 13px;"><strong>📝 Rekomendasi Caption:</strong><br>Gak nyangka banget bagian akhir video ini bikin merinding! 🤯 Tonton sampai habis ya! #paidi #fyp</p>
                <p style="margin: 0; font-size: 13px; color: #00a8ff;"><strong># Hashtag Terlaris:</strong> #viral #trending #paidiaistudio #edukasiai #fypindonesia</p>
            </div>
            <button style="width: 100%; background: #00a8ff; color: white; border: none; padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px;">📥 Unduh Video Klip #1 (HD)</button>
        </div>
        """, unsafe_allow_html=True)

        # Klip 2
        st.markdown("""
        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h4 style="margin: 0; color: #00a8ff;">⚡ Klip #2: Penjelasan Inti (Golden Moment)</h4>
                <span style="background: rgba(0, 168, 255, 0.2); color: #00a8ff; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold;">Potensi FYP: 89% (Tinggi)</span>
            </div>
            <p style="font-size: 13px; color: rgba(255,255,255,0.7);">Durasi: 0:30 detik | Format: 9:16 Siap Upload</p>
            <div style="background: rgba(0,0,0,0.4); padding: 15px; border-radius: 8px; margin: 10px 0;">
                <p style="margin: 0 0 8px 0; font-size: 13px;"><strong>📝 Rekomendasi Caption:</strong><br>Rahasia ini akhirnya terbongkar! Simak baik-baik penjelasan singkatnya di sini. 👇</p>
                <p style="margin: 0; font-size: 13px; color: #00a8ff;"><strong># Hashtag Terlaris:</strong> #tipsandtricks #ai #videomaker #trendingreels</p>
            </div>
            <button style="width: 100%; background: #00a8ff; color: white; border: none; padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px;">📥 Unduh Video Klip #2 (HD)</button>
        </div>
        """, unsafe_allow_html=True)

        # Klip 3
        st.markdown("""
        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h4 style="margin: 0; color: #00a8ff;">🎯 Klip #3: Kesimpulan & Hook Emosional</h4>
                <span style="background: rgba(0, 168, 255, 0.2); color: #00a8ff; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold;">Potensi FYP: 92% (Sangat Tinggi)</span>
            </div>
            <p style="font-size: 13px; color: rgba(255,255,255,0.7);">Durasi: 0:50 detik | Format: 9:16 Siap Upload</p>
            <div style="background: rgba(0,0,0,0.4); padding: 15px; border-radius: 8px; margin: 10px 0;">
                <p style="margin: 0 0 8px 0; font-size: 13px;"><strong>📝 Rekomendasi Caption:</strong><br>Pelajaran berharga yang harus kamu tahu hari ini. Setuju gak sama pendapat ini? 💬</p>
                <p style="margin: 0; font-size: 13px; color: #00a8ff;"><strong># Hashtag Terlaris:</strong> #inspirasi #motivasihidup #paidi #fypage</p>
            </div>
            <button style="width: 100%; background: #00a8ff; color: white; border: none; padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px;">📥 Unduh Video Klip #3 (HD)</button>
        </div>
        """, unsafe_allow_html=True)

    # --- ISI TAB ATAS 3: PENGATURAN ---
    elif st.session_state.active_tab == "Pengaturan":
        st.markdown("### ⚙️ Pengaturan Fitur & Ekstraksi Konten AI")
        st.markdown("<p style='color: rgba(255,255,255,0.7); font-size: 0.9rem;'>Sesuaikan preferensi subtitle, rasio, resolusi, dan fokus ekstraksi konten sesuai kebutuhan Anda.</p>", unsafe_allow_html=True)

        with st.form("form_pengaturan"):
            st.markdown("#### 🎨 Preferensi Tampilan Video")
            sub_val = st.checkbox("Aktifkan Subtitle Teks Otomatis", value=st.session_state.setting_subtitle)
            head_val = st.checkbox("Aktifkan Headline Judul Dinamis", value=st.session_state.setting_headline)
            
            c_set1, c_set2 = st.columns(2)
            with c_set1:
                rasio_val = st.selectbox("Rasio Aspek", ["9:16 (TikTok/Reels)", "1:1 (Square)", "16:9 (Landscape)"], index=["9:16 (TikTok/Reels)", "1:1 (Square)", "16:9 (Landscape)"].index(st.session_state.setting_rasio))
                durasi_val = st.selectbox("Durasi Klip", ["Pendek (15-30 detik)", "Standar (30-60 detik)"], index=["Pendek (15-30 detik)", "Standar (30-60 detik)"].index(st.session_state.setting_durasi))
            with c_set2:
                resolusi_val = st.selectbox("Resolusi Video", ["720p HD", "1080p Full HD"], index=["720p HD", "1080p Full HD"].index(st.session_state.setting_resolusi))
                fokus_val = st.selectbox("Fokus Ekstraksi Konten", ["Golden moment", "Emosional", "Potensi fyp"], index=["Golden moment", "Emosional", "Potensi fyp"].index(st.session_state.setting_fokus))

            submit_settings = st.form_submit_button("💾 Simpan Pengaturan")
            if submit_settings:
                st.session_state.setting_subtitle = sub_val
                st.session_state.setting_headline = head_val
                st.session_state.setting_rasio = rasio_val
                st.session_state.setting_resolusi = resolusi_val
                st.session_state.setting_durasi = durasi_val
                st.session_state.setting_fokus = fokus_val
                st.success("✅ Pengaturan berhasil disimpan secara permanen di sesi ini!")

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
        <a href="?menu=Bantuan" target="_sel
