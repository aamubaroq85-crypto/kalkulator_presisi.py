import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Agriscience Formulation Engine",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Agriscience Formulation Engine")
st.subheader("Industrial Pesticide & Fertilizer Manufacturing Suite")

st.markdown("---")

# Input Parameter Utama
batch_volume = st.number_input("Volume Target Produksi (Liter / Kg):", min_value=1.0, value=100.0, step=10.0)

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

pilihan_produk = st.selectbox("Pilih Kategori & Bahan Aktif:", list(database_formulasi.keys()))
item = database_formulasi[pilihan_produk]

st.info(f"**Kategori:** {item['kategori']} | **Bentuk Formulasi:** `{item['formksi']}`")

purity = st.number_input("Kemurnian Bahan Baku Teknis / Konsentrat (%):", min_value=30.0, max_value=99.0, value=95.0)

st.markdown("")

# Tombol Kalkulasi Eksekusi
if st.button("🚀 HITUNG FORMULA & BIAYA PABRIKASI", use_container_width=True):
    # Kalkulasi Stoikiometri Matriks
    gram_target_total = item["targetG"] * batch_volume
    gram_bahan_teknis = gram_target_total / (purity / 100.0)
    
    berat_total_batch_kg = batch_volume * item["bobotJenis"]
    berat_bahan_teknis_kg = gram_bahan_teknis / 1000.0
    berat_emulsifier_kg = berat_total_batch_kg * item["emulsifierRatio"]
    berat_pelarut_kg = berat_total_batch_kg - (berat_bahan_teknis_kg + berat_emulsifier_kg)
    
    total_biaya = berat_bahan_teknis_kg * (item["hppBahan"] * (purity / 100.0))
    hpp_per_liter = total_biaya / batch_volume

    # Menampilkan Hasil Perumusan
    st.success("Matriks Formulasi Industri Berhasil Dihitung Berdasarkan Agriscience Standard!")
    
    st.markdown("### Komposisi Bahan Baku (Batch Formulation):")
    st.markdown(
        f"* **Bahan Aktif / Konsentrat ({purity}%):** `{berat_bahan_teknis_kg:.2f} Kg`\n"
        f"* **Pelarut / Carrier ({item['pelarut']}):** `{berat_pelarut_kg:.2f} Kg`\n"
        f"* **Sistem Surfactant / Emulsifier / Wetting:** `{berat_emulsifier_kg:.2f} Kg`"
    )
    
    st.markdown("### Analisis Finansial & HPP:")
    st.markdown(
        f"* **Estimasi Total Biaya Batch:** `Rp {total_biaya:,.0f}`\n"
        f"* **Estimasi HPP per Liter/Kg:** `Rp {round(hpp_per_liter):,.0f} / Satuan`"
    )

    st.markdown("### Prosedur Pencampuran Pabrikasi (SOP):")
    st.markdown(f"1. Masukkan **{berat_pelarut_kg:.2f} Kg** pelarut/pembawa ke dalam tangki pencampur utama (*mixing vessel*).")
    st.markdown(f"2. Masukkan bahan aktif utama sebanyak **{berat_bahan_teknis_kg:.2f} Kg** secara bertahap sambil diaduk konstan.")
    st.markdown(f"3. Masukkan agen surfaktan/emulsifier/wetting sebanyak **{berat_emulsifier_kg:.2f} Kg** untuk mengoptimalkan kestabilan fisik.")
    st.markdown("4. Lakukan uji homogenitas akhir, viskositas, dan pH sebelum produk dikemas ke dalam wadah komersial.")
