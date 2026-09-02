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

# Database Lengkap Berdasarkan Kategori, Jenis Formulasi, dan Standar Komersial
database_formulasi = {
    # INSEKTISIDA & AKARISIDA
    "Abamectin 18 g/l (EC) - Insektisida/Akarisida": {
        "kategori": "Insektisida / Akarisida", "formksi": "EC (Emulsifiable Concentrate)", 
        "targetG": 18, "bobotJenis": 0.95, "pelarut": "Xylene / Pelarut Organik", "emulsifierRatio": 0.05, "hppBahan": 450000
    },
    "Emamektin Benzoat 50 g/kg (WG) - Insektisida": {
        "kategori": "Insektisida", "formksi": "WG (Water Dispersible Granule)", 
        "targetG": 50, "bobotJenis": 1.20, "pelarut": "Filler (Kaolin) + Dispersant", "emulsifierRatio": 0.08, "hppBahan": 600000
    },
    "Imidakloprid 200 g/l (SL) - Insektisida": {
        "kategori": "Insektisida", "formksi": "SL (Soluble Liquid)", 
        "targetG": 200, "bobotJenis": 1.10, "pelarut": "Air Demineralisasi + Co-solvent", "emulsifierRatio": 0.04, "hppBahan": 350000
    },
    
    # FUNGISIDA
    "Difenokonazol 250 g/l (EC) - Fungisida": {
        "kategori": "Fungisida", "formksi": "EC (Emulsifiable Concentrate)", 
        "targetG": 250, "bobotJenis": 1.05, "pelarut": "Aromatik Hidrokarbon", "emulsifierRatio": 0.06, "hppBahan": 400000
    },
    "Klorotalonil 500 g/l (SC) - Fungisida": {
        "kategori": "Fungisida", "formksi": "SC (Suspension Concentrate)", 
        "targetG": 500, "bobotJenis": 1.25, "pelarut": "Air + Wetting Agent", "emulsifierRatio": 0.07, "hppBahan": 280000
    },
    "Mankozeb 800 g/kg (WP) - Fungisida": {
        "kategori": "Fungisida", "formksi": "WP (Wettable Powder)", 
        "targetG": 800, "bobotJenis": 1.30, "pelarut": "Carrier Iner (Talc/Kaolin) + Wetting Agent", "emulsifierRatio": 0.05, "hppBahan": 150000
    },

    # HERBISIDA
    "Glifosat 480 g/l (SL) - Herbisida": {
        "kategori": "Herbisida", "formksi": "SL (Soluble Liquid)", 
        "targetG": 480, "bobotJenis": 1.20, "pelarut": "Air Demineralisasi + Surfactant", "emulsifierRatio": 0.08, "hppBahan": 95000
    },
    "Parakuat Diklorida 276 g/l (SL) - Herbisida": {
        "kategori": "Herbisida", "formksi": "SL (Soluble Liquid)", 
        "targetG": 276, "bobotJenis": 1.15, "pelarut": "Air Demineralisasi + Adjuvan", "emulsifierRatio": 0.05, "hppBahan": 120000
    },

    # PUPUK (TE & POC)
    "Pupuk Mikro TE (Trace Elements) Chelated (WP/SP)": {
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
    st.markdown(f"3. Masukkan agen surfaktan/emulsifier/wetting sebanyak **{berat_emulsifier_kg:.2f} Kg** untuk mengoptimalkan stabilitas fisik.")
    st.markdown("4. Lakukan uji homogenitas akhir, viskositas, dan pH sebelum produk dikemas ke dalam wadah komersial.")
