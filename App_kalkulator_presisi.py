import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Zuhri Formalism - Formulator Suite",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Formulator & Manufacturing Suite")
st.subheader("Zuhri Formalism — Industrial Pesticide Formulation Engine")

st.markdown("---")

# Input Pengguna
batch_volume = st.number_input("Volume Target Produksi (Liter):", min_value=1.0, value=100.0, step=10.0)

database_formulasi = {
    "Abamectin 18 g/l (Setara Demolish)": {
        "targetG": 18, "bobotJenis": 0.95, 
        "pelarut": "Xylene / Pelarut Organik", "emulsifierRatio": 0.05, "hppBahan": 450000
    },
    "Imidakloprid 200 g/l (Setara Confidor)": {
        "targetG": 200, "bobotJenis": 1.10, 
        "pelarut": "DMF / N-Methylpyrrolidone", "emulsifierRatio": 0.07, "hppBahan": 350000
    },
    "Difenokonazol 250 g/l (Setara Score)": {
        "targetG": 250, "bobotJenis": 1.05, 
        "pelarut": "Aromatik Hidrokarbon", "emulsifierRatio": 0.06, "hppBahan": 400000
    },
    "Glifosat 480 g/l (Setara Roundup)": {
        "targetG": 480, "bobotJenis": 1.20, 
        "pelarut": "Air Demineralisasi + Surfactant", "emulsifierRatio": 0.08, "hppBahan": 95000
    }
}

pilihan_produk = st.selectbox("Pilih Produk Acuan / Bahan Aktif:", list(database_formulasi.keys()))
purity = st.number_input("Kemurnian Bahan Baku Teknis (Technical Grade %):", min_value=50.0, max_value=99.0, value=95.0)

st.markdown("")

# Tombol Kalkulasi
if st.button("🚀 HITUNG FORMULA & BIAYA PRODUKSI", use_container_width=True):
    item = database_formulasi[pilihan_produk]
    
    # Kalkulasi Stoikiometri
    gram_target_total = item["targetG"] * batch_volume
    gram_bahan_teknis = gram_target_total / (purity / 100.0)
    
    berat_total_batch_kg = batch_volume * item["bobotJenis"]
    berat_bahan_teknis_kg = gram_bahan_teknis / 1000.0
    berat_emulsifier_kg = berat_total_batch_kg * item["emulsifierRatio"]
    berat_pelarut_kg = berat_total_batch_kg - (berat_bahan_teknis_kg + berat_emulsifier_kg)
    
    total_biaya = berat_bahan_teknis_kg * (item["hppBahan"] * (purity / 100.0))
    hpp_per_liter = total_biaya / batch_volume

    # Menampilkan Hasil dalam Kotak Estetik
    st.success("Hasil Perumusan & Komposisi Batch Industri Berhasil Dihitung!")
    
    st.markdown("### Komposisi Bahan Baku:")
    st.info(
        f"* **Bahan Baku Teknis ({purity}%):** `{berat_bahan_teknis_kg:.2f} Kg`\n"
        f"* **Pelarut ({item['pelarut']}):** `{berat_pelarut_kg:.2f} Kg`\n"
        f"* **Sistem Emulsifier (HLB Optimal):** `{berat_emulsifier_kg:.2f} Kg`"
    )
    
    st.markdown("### Analisis Finansial:")
    st.warning(
        f"* **Estimasi Total HPP Batch:** `Rp {total_biaya:,.0f}`\n"
        f"* **Estimasi HPP per Liter:** `Rp {round(hpp_per_liter):,.0f} / Liter`"
    )

    st.markdown("### Prosedur Pencampuran Pabrikasi (SOP):")
    st.markdown(f"1. Masukkan **{berat_pelarut_kg:.2f} Kg** pelarut `{item['pelarut']}` ke dalam tangki pencampur utama (*mixing vessel*).")
    st.markdown(f"2. Secara perlahan, masukkan bahan aktif teknis sebanyak **{berat_bahan_teknis_kg:.2f} Kg** sambil diaduk menggunakan *high-speed stirrer*.")
    st.markdown(f"3. Tambahkan sistem emulsifier sebanyak **{berat_emulsifier_kg:.2f} Kg** untuk mengunci kestabilan emulsi (fase minyak/air).")
    st.markdown("4. Lakukan uji homogenitas dan indeks bias, lalu produk siap dikemas ke dalam botol.")
