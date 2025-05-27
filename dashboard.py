import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_autorefresh import st_autorefresh

LOG_FILE = 'log_prediksi.log'

def load_log():
    try:
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
        data = []
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) < 3:
                continue
            time = parts[0].strip()
            content = parts[2].strip()

            log_parts = content.replace('Nama: ', '').replace('IPK: ', '') \
                               .replace('Kehadiran: ', '').replace('Organisasi: ', '') \
                               .replace('Hasil: ', '').replace('Predikat: ', '') \
                               .replace('Waktu: ', '').split(', ')
            if len(log_parts) < 6:
                continue
            nama, ipk, hadir, org, hasil, predikat, waktu = (*log_parts[:6], log_parts[-1])
            data.append({
                'Waktu Log': time,
                'Nama': nama,
                'IPK': float(ipk),
                'Kehadiran': int(hadir),
                'Organisasi': int(org),
                'Hasil': hasil,
                'Predikat': predikat,
                'Inferensi (s)': float(waktu.replace('s', ''))
            })
        return pd.DataFrame(data)
    except FileNotFoundError:
        return pd.DataFrame()

st.set_page_config(page_title="Monitoring Model Kelulusan", layout="wide")
st.title("🎓 Dashboard Monitoring Prediksi Kelulusan Mahasiswa")

st_autorefresh(interval=5000, limit=None, key="refresh")

df = load_log()

if df.empty:
    st.warning("Belum ada data prediksi yang tersedia.")
else:
    st.subheader("📄 Riwayat Prediksi")
    st.dataframe(df[::-1].reset_index(drop=True), use_container_width=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Prediksi", len(df))
    col2.metric("Lulus Tepat Waktu", len(df[df['Hasil'] == 'Lulus Tepat Waktu']))
    col3.metric("Tidak Lulus Tepat Waktu", len(df[df['Hasil'] == 'Tidak Lulus Tepat Waktu']))
    col4.metric("Predikat Cumlaude", len(df[df['Predikat'] == 'Cumlaude']))

    st.subheader("📊 Statistik Prediksi")

    fig1, ax1 = plt.subplots(figsize=(5,5))
    counts = df['Hasil'].value_counts()
    ax1.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=['#4CAF50','#F44336'])
    ax1.set_title('Perbandingan Lulus vs Tidak Lulus')

    fig2, ax2 = plt.subplots(figsize=(6,5))
    ax2.plot(df['Inferensi (s)'].values[::-1], marker='o', linestyle='-')
    ax2.set_ylabel("Waktu (detik)")
    ax2.set_xlabel("Urutan Prediksi")
    ax2.set_title("Waktu Inferensi per Prediksi")

    colA, colB = st.columns(2)
    with colA:
        st.pyplot(fig1)
    with colB:
        st.pyplot(fig2)
