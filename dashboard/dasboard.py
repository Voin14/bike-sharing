import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
sns.set(style='darkgrid')

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🚲"
)
alt.themes.enable('dark')

# Load dataset
df_day = pd.read_csv(r"C:\Users\LENOVO\Documents\Python\BikeSharing\day.csv")

# Konversi tanggal ke datetime
df_day["dteday"] = pd.to_datetime(df_day["dteday"])

# Pastikan kolom 'season' tidak memiliki NaN sebelum mapping
df_day = df_day.dropna(subset=["season", "weathersit"])

# Pastikan kolom 'season' bertipe numerik sebelum mapping
if df_day["season"].dtype != "int64" and df_day["season"].dtype != "float64":
    df_day = df_day[df_day["season"].str.isnumeric()]
    df_day["season"] = df_day["season"].astype(int)

# Mapping musim dan kondisi cuaca
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
weather_mapping = {1: "Clear/Few Clouds", 2: "Mist/Cloudy", 3: "Light Snow/Rain", 4: "Heavy Rain/Snow"}

df_day["season"] = df_day["season"].map(season_mapping)
df_day["weathersit"] = df_day["weathersit"].astype(int).map(weather_mapping)

# Sidebar
with st.sidebar:
    st.title("🚲 Bike Sharing Dashboard")
    st.markdown("### Data Overview")
    
    start_date = st.date_input("Mulai Tanggal", df_day["dteday"].min())
    end_date = st.date_input("Akhir Tanggal", df_day["dteday"].max())
    selected_season = st.multiselect("Pilih Musim", df_day["season"].dropna().unique(), df_day["season"].dropna().unique())
    selected_weather = st.multiselect("Pilih Kondisi Cuaca", df_day["weathersit"].dropna().unique(), df_day["weathersit"].dropna().unique())

# Filter dataset berdasarkan input pengguna
df_filtered = df_day[(df_day["dteday"] >= pd.to_datetime(start_date)) &
                     (df_day["dteday"] <= pd.to_datetime(end_date)) &
                     (df_day["season"].isin(selected_season)) &
                     (df_day["weathersit"].isin(selected_weather))]

st.caption("By Adam Havenia Pratama")

# Menampilkan metrik utama
with st.container():
    st.title("📊 Statistik Penyewaan Sepeda")
    col1, col2 = st.columns(2)
    col1.metric("Rata-rata Penyewaan Sepeda", round(df_filtered["cnt"].mean(), 2))
    col2.metric("Total Penyewaan", "{:,}".format(df_filtered["cnt"].sum()))

    # Visualisasi penyewaan berdasarkan musim
    st.subheader("🚲 Penyewaan Sepeda Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x="season", y="cnt", data=df_filtered, palette="coolwarm", ci=None, ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    # Menambahkan label angka dalam ribuan pada setiap batang
    for p in ax.patches:
        ax.annotate(f'{p.get_height()/1000:.1f}K', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')
    
    st.pyplot(fig)

    # Visualisasi penyewaan berdasarkan cuaca
    st.subheader("🌤️ Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
    if df_filtered["weathersit"].notna().any():
        fig, ax = plt.subplots(figsize=(6,4))
        sns.boxplot(x="weathersit", y="cnt", data=df_filtered, palette="coolwarm", ax=ax)
        ax.set_xlabel("Kondisi Cuaca")
        ax.set_ylabel("Jumlah Penyewaan Sepeda")
        st.pyplot(fig)
    else:
        st.warning("Tidak ada data untuk kondisi cuaca yang dipilih.")

# Tren Penyewaan Harian
with st.container():
    st.subheader("📅 Tren Penyewaan Sepeda Per Hari")
    chart = alt.Chart(df_filtered).mark_line().encode(
        x='dteday:T',
        y='cnt:Q',
        tooltip=['dteday', 'cnt']
    ).properties(
        width=600,
        height=300
    )
    st.altair_chart(chart, use_container_width=True)

# Tabel Data
st.title("📄 Data Penyewaan Sepeda")
st.dataframe(df_filtered)
