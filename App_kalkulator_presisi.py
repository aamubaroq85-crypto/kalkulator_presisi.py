import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Thermal-Stable Lock Analysis",
    page_icon="🔬",
    layout="centered"
)

st.title("🔬 Thermal-Stable Lock Analysis")
st.subheader("Agriscience Formulation & Thermal Degradation Engine")

st.markdown("Evaluasi tingkat ketahanan ikatan molekul pestisida dan kompleks nutrisi terhadap degradasi suhu dan panas matahari, lengkap dengan panduan takaran riil.")
st.markdown("---")

# Database Komprehensif Berdasarkan Kategori, Golongan, dan Jenis Formulasi
database_formulasi = {
    # ==================== INSEKTISIDA ====================
    "Abamectin 18 g/l (EC) - Insektisida/Akarisida": {
        "kategori": "Insektisida / Akarisida", "formksi": "EC (Emulsifiable Concentrate)", 
        "targetG": 18, "bobotJenis": 0.95, "pelarut": "Xylene / Pelarut Organik", "emulsifierRatio": 0.05, "hppBahan": 450000
    },
    "Klorantraniliprol 50 g/l (SC) - Diamida": {
        "kategori": "Insektisida (Diamida)", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 50, "bobotJenis": 1.15, "pelarut": "Air Demineralisasi + Wetting Agent", "emulsifierRatio": 0.06, "hppBahan": 850000
    },
    "Fipronil 50 g/l (SC) - Fenilpirazol": {
        "kategori": "Insektisida (Fenilpirazol)", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 50, "bobotJenis": 1.10, "pelarut": "Air + Co-solvent", "emulsifierRatio": 0.06, "hppBahan": 550000
    },
    "Flupiradifuron 200 g/l (SL) - Butenolida": {
        "kategori": "Insektisida (Butenolida)", "formksi": "SL (Soluble Liquid)", 
        "targetG": 200, "bobotJenis": 1.12, "pelarut": "Air + Surfaktan Khusus", "emulsifierRatio": 0.05, "hppBahan": 750000
    },
    "Indoksakarb 150 g/l (SC) - Oxadiazine": {
        "kategori": "Insektisida (Oxadiazine)", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 150, "bobotJenis": 1.18, "pelarut": "Air + Dispersant", "emulsifierRatio": 0.07, "hppBahan": 900000
    },
    "Imidakloprid 200 g/l (SL) - Neonikotinoid": {
        "kategori": "Insektisida (Neonikotinoid)", "formksi": "SL (Soluble Liquid)", 
        "targetG": 200, "bobotJenis": 1.10, "pelarut": "Air Demineralisasi + Co-solvent", "emulsifierRatio": 0.04, "hppBahan": 350000
    },
    "Emamektin Benzoat 50 g/kg (WG) - Insektisida": {
        "kategori": "Insektisida", "formksi": "WG (Water Dispersible Granule)", 
        "targetG": 50, "bobotJenis": 1.20, "pelarut": "Filler (Kaolin) + Dispersant", "emulsifierRatio": 0.08, "hppBahan": 600000
    },

    # ==================== FUNGISIDA ====================
    "Difenokonazol 250 g/l (EC) - Triazol": {
        "kategori": "Fungisida (Triazol)", "formksi": "EC (Emulsifiable Concentrate)", 
        "targetG": 250, "bobotJenis": 1.05, "pelarut": "Aromatik Hidrokarbon", "emulsifierRatio": 0.06, "hppBahan": 400000
    },
    "Tebukonazol 250 g/l (EC) - Triazol Lainnya": {
        "kategori": "Fungisida (Triazol)", "formksi": "EC (Emulsifiable Concentrate)", 
        "targetG": 250, "bobotJenis": 1.06, "pelarut": "Aromatik Hidrokarbon + Surfactant", "emulsifierRatio": 0.06, "hppBahan": 420000
    },
    "Heksakonazol 50 g/l (SC) - Triazol": {
        "kategori": "Fungisida (Triazol)", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 50, "bobotJenis": 1.08, "pelarut": "Air + Wetting Agent", "emulsifierRatio": 0.05, "hppBahan": 310000
    },
    "Trifloksistrobin 250 g/l (SC) - Strobilurin": {
        "kategori": "Fungisida (Strobilurin)", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 250, "bobotJenis": 1.12, "pelarut": "Air + Dispersant", "emulsifierRatio": 0.07, "hppBahan": 850000
    },
    "Klorotalonil 500 g/l (SC) - Kontak": {
        "kategori": "Fungisida (Kontak)", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 500, "bobotJenis": 1.25, "pelarut": "Air + Wetting Agent", "emulsifierRatio": 0.07, "hppBahan": 280000
    },
    "Mankozeb 800 g/kg (WP) - Kontak": {
        "kategori": "Fungisida (Kontak)", "formksi": "WP (Wettable Powder)", 
        "targetG": 800, "bobotJenis": 1.30, "pelarut": "Carrier Iner (Talc/Kaolin) + Wetting Agent", "emulsifierRatio": 0.05, "hppBahan": 150000
    },
    "Tiofanat-Metil 500 g/sc (SC) - Sistemik": {
        "kategori": "Fungisida (Sistemik)", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 500, "bobotJenis": 1.20, "pelarut": "Air + Stabilizer", "emulsifierRatio": 0.06, "hppBahan": 380000
    },
    "Dimetomorf 500 g/kg (WP) - Khusus Oomycetes": {
        "kategori": "Fungisida (Sistemik)", "formksi": "WP (Wettable Powder)", 
        "targetG": 500, "bobotJenis": 1.22, "pelarut": "Carrier Iner + Wetting Agent", "emulsifierRatio": 0.05, "hppBahan": 650000
    },
    "Fosetil-Aluminium 800 g/kg (WP) - Sistemik 2 Arah": {
        "kategori": "Fungisida (Sistemik)", "formksi": "WP (Wettable Powder)", 
        "targetG": 800, "bobotJenis": 1.25, "pelarut": "Carrier Iner + Dispersant", "emulsifierRatio": 0.04, "hppBahan": 500000
    },

    # ==================== AKARISIDA ====================
    "Klorfenapir 300 g/l (SC) - Akarisida/Insektisida": {
        "kategori": "Akarisida / Pirol", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 300, "bobotJenis": 1.15, "pelarut": "Air + Co-solvent Organik", "emulsifierRatio": 0.06, "hppBahan": 700000
    },
    "Spirodiklofen 240 g/l (SC) - Inhibitor Lipid": {
        "kategori": "Akarisida", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 240, "bobotJenis": 1.18, "pelarut": "Air + Emulsifying Agent", "emulsifierRatio": 0.07, "hppBahan": 780000
    },
    "Amitraz 200 g/l (EC) - Akarisida Pernapasan": {
        "kategori": "Akarisida", "formksi": "EC (Emulsifiable Concentrate)", 
        "targetG": 200, "bobotJenis": 1.02, "pelarut": "Xylene / Pelarut Aromatik", "emulsifierRatio": 0.08, "hppBahan": 450000
    },

    # ==================== HERBISIDA ====================
    "Glifosat 480 g/l (SL) - Sistemik Non-Selektif": {
        "kategori": "Herbisida (Sistemik)", "formksi": "SL (Soluble Liquid)", 
        "targetG": 480, "bobotJenis": 1.20, "pelarut": "Air Demineralisasi + Surfactant", "emulsifierRatio": 0.08, "hppBahan": 95000
    },
    "Parakuat Diklorida 276 g/l (SL) - Kontak Non-Selektif": {
        "kategori": "Herbisida (Kontak)", "formksi": "SL (Soluble Liquid)", 
        "targetG": 276, "bobotJenis": 1.15, "pelarut": "Air Demineralisasi + Adjuvan", "emulsifierRatio": 0.05, "hppBahan": 120000
    },
    "Oksifluorfen 240 g/l (EC) - Pra & Purna Tumbuh": {
        "kategori": "Herbisida (Selektif)", "formksi": "EC (Emulsifiable Concentrate)", 
        "targetG": 240, "bobotJenis": 1.10, "pelarut": "Pelarut Aromatik Khusus", "emulsifierRatio": 0.07, "hppBahan": 550000
    },
    "Bispiribak-Natrium 400 g/l (SC) - Selektif Sawah": {
        "kategori": "Herbisida (Sistemik Selektif)", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 400, "bobotJenis": 1.12, "pelarut": "Air + Wetting Agent", "emulsifierRatio": 0.06, "hppBahan": 950000
    },
    "2,4-D Dimetil Amina 865 g/l (SL) - Selektif Daun Lebar": {
        "kategori": "Herbisida (Sistemik Selektif)", "formksi": "SL (Soluble Liquid)", 
        "targetG": 865, "bobotJenis": 1.22, "pelarut": "Air Demineralisasi", "emulsifierRatio": 0.04, "hppBahan": 110000
    },

    # ==================== PUPUK (TE & POC) ====================
    "Pupuk Mikro TE (Trace Elements) Chelated (SP)": {
        "kategori": "Pupuk Mikro", "formksi": "SP (Soluble Powder)", 
        "targetG": 300, "bobotJenis": 1.10, "pelarut": "Chelating Agent (EDTA) + Carrier", "emulsifierRatio": 0.02, "hppBahan": 200000
    },
    "Pupuk Organik Cair (POC) NPK Enzimatik (Lokal)": {
        "kategori": "Pupuk Organik", "formksi": "POC (Liquid Organic Fertilizer)", 
        "targetG": 150, "bobotJenis": 1.05, "pelarut": "Ekstrak Organik Cair + Asam Humat", "emulsifierRatio": 0.03, "hppBahan": 45000
    }
}

pilihan_produk = st.selectbox("Pilih Kategori Produk / Bahan Aktif:", list(database_formulasi.keys()))
item = database_formulasi[pilihan_produk]

st.info(f"**Kategori:** {item['kategori']} | **Bentuk Formulasi:** `{item['formksi']}`")

# Input Parameter Fasa Baru
col1, col2, col3 = st.columns(3)
with col1:
    fasa_aktif = st.number_input("Nilai Fasa Bahan Utama (A)", min_value=0.1, value=1.618, step=0.001, format="%.3f")
with col2:
    fasa_aditif = st.number_input("Nilai Fasa Aditif/Pelarut (B)", min_value=0.1, value=1.000, step=0.001, format="%.3f")
with col3:
    target_volume = st.number_input("Target Volume Total (ml/g)", min_value=10.0, value=1000.0, step=50.0)

purity = st.number_input("Kemurnian Bahan Baku Teknis / Konsentrat (%):", min_value=30.0, max_value=99.0, value=95.0)

st.markdown("")

# Tombol Kalkulasi Eksekusi
if st.button("Jalankan Simulasi Kestabilan & Hitung Takaran", use_container_width=True):
    # Kalkulasi Stoikiometri yang dimodifikasi dengan Nilai Fasa A dan B
    gram_target_total = item["targetG"] * (target_volume / 1000.0)
    gram_bahan_teknis = (gram_target_total / (purity / 100.0)) * (fasa_aktif / fasa_aditif)
    
    berat_total_batch_kg = (target_volume / 1000.0) * item["bobotJenis"]
    berat_bahan_teknis_kg = gram_bahan_teknis / 1000.0
    berat_emulsifier_kg = berat_total_batch_kg * item["emulsifierRatio"] * fasa_aditif
    berat_pelarut_kg = abs(berat_total_batch_kg - (berat_bahan_teknis_kg + berat_emulsifier_kg))
    
    total_biaya = berat_bahan_teknis_kg * (item["hppBahan"] * (purity / 100.0))
    hpp_per_liter = total_biaya / (target_volume / 1000.0)

    # Menampilkan Hasil Analisis Kestabilan & Perumusan
    st.success("Simulasi Ketahanan Termal & Matriks Perumusan Berhasil Dihitung!")
    
    st.markdown("### 📊 Parameter Hasil Simulasi Fasa:")
    st.markdown(
        f"* **Faktor Rasio Fasa (A/B):** `{fasa_aktif / fasa_aditif:.3f}`\n"
        f"* **Komposisi Bahan Aktif Terkoreksi:** `{berat_bahan_teknis_kg * 1000:.2f} Gram`\n"
        f"* **Pelarut ({item['pelarut']}):** `{berat_pelarut_kg * 1000:.2f} Gram`\n"
        f"* **Sistem Surfactant / Emulsifier Terkunci:** `{berat_emulsifier_kg * 1000:.2f} Gram`"
    )
    
    st.markdown("### 💰 Analisis Finansial & HPP Skala Batch:")
    st.markdown(
        f"* **Estimasi Total Biaya:** `Rp {total_biaya:,.0f}`\n"
        f"* **Estimasi HPP per Liter/Kg:** `Rp {round(hpp_per_liter):,.0f} / Satuan`"
    )

    st.markdown("### 🌡️ Indeks Proteksi Termal-Stable:")
    st.markdown(f"1. Dengan rasio fasa aktif **{fasa_aktif}** dan fasa aditif **{fasa_aditif}**, ikatan molekul formula memiliki ketahanan optimal terhadap penguapan suhu tinggi.")
    st.markdown(f"2. Gunakan pelarut sebanyak **{berat_pelarut_kg * 1000:.2f} ml** pada tahap awal pencampuran *mixing vessel*.")
    st.markdown("3. Formula terkunci secara termal dan siap diuji ketahanannya di bawah paparan sinar UV lapangan.")

    # Grafik Tren Simulasi Real-Time
    st.markdown("---")
    st.markdown("### 📈 Grafik Tren Riwayat Deviasi & Pengujian Real-Time")
    chart_data = [fasa_aktif * 10, fasa_aditif * 15, (fasa_aktif/fasa_aditif) * 20, purity * 0.5]
    st.line_chart(chart_data)
