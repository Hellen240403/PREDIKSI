import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def load_data(file_path, index_col=None):
    # index_col akan diabaikan jika None
    df = pd.read_csv(file_path, index_col=index_col)
    return df

def app():
    # Judul dan Informasi mengenai Dasboard
    st.title("Platform Prediksi Cuaca Kota Surabaya :thunder_cloud_and_rain:")

    with st.expander("Pendahuluan"):
        tab1, tab2, tab3 = st.tabs(["Latar Belakang", "Tujuan", "Manfaat"])
        with tab1:
            st.info("""
	    Prediksi cuaca adalah proses untuk memprediksi kondisi atmosfer 
            pada waktu tertentu di masa depan yang dilakukan dengan menganalisis data 
            meteorologi yang ada. Perkembangannya teknologi dan metode yang terus meningkat 
            membuat banyak pilihan untuk memprediksi cuaca dengan sangat canggih. Proses 
            ini melibatkan penggunaan berbagai metode statistika dan algoritma pemrograman 
            untuk memodelkan dinamika atmosfer. Berbagai parameter cuaca seperti suhu, 
            kelembapan, tekanan udara, kecepatan angin, dan curah hujan digunakan untuk 
            membuat ramalan cuaca yang dapat memberikan informasi kepada masyarakat untuk 
            kegiatan sehari-hari. Dalam era teknologi yang semakin maju, prediksi cuaca 
            menjadi lebih akurat dan dapat diakses dengan mudah melalui berbagai platform 
            digital, memberikan kemudahan bagi masyarakat dalam merencanakan aktivitas mereka.

            Kota Surabaya merupakan salah satu kota metropolitan dan kota besar di Indonesia 
            dengan berbagai aktivitas ekonomi, sosial, dan budaya yang sangat tinggi. Aktifitas 
            masyarakat Kota Surabaya sangat padat pada jam tertentu karena kegiatan yang 
            dilakukan secara bersama. Masyarakat dituntut untuk terus waspada terhadap kondisi 
            sekitar lingkungannya agar beraktifitas dengan aman. Cuaca menjadi sangat penting 
            diperhatikan oleh masyarakat karna kondisi yang tidak menentu setiap waktunya. Oleh 
            karena itu, informasi prediksi cuaca yang akurat sangat penting untuk mendukung 
            keberlangsungan aktivitas tersebut. Kondisi tersebut menjadi pemicu untuk melakukan 
            penelitian khusus mengenai prediksi cuaca Kota Surabaya untuk meningkatkan kualitas 
            ramalan cuaca di daerah tersebut. Mengingat tantangan geografis dan dinamika cuaca 
            tropis yang unik, model prediksi cuaca yang lebih tepat dan efisien sangat diperlukan 
            untuk menghadapi ketidakpastian yang terjadi di masa depan.
	    """)
        with tab2:
            st.info("""
	    Tujuan dari penelitian ini adalah untuk mengembangkan model prediksi cuaca 
            yang akurat untuk Kota Surabaya dengan menggunakan metode Artificial Neural Network 
            (ANN) dan Long Short-Term Memory (LSTM) berdasarkan data cuaca terbaru. Adapaun tujuan 
            penelitian secara spesifik dijabarkan sebagai berikut. 
	        1. Membangun model prediksi cuaca yang dapat memproyeksikan kondisi atmosfer Kota Surabaya 
            dengan menggunakan data meteorologi yang diambil dari BMKG (Badan Meteorologi, Klimatologi, 
            dan Geofisika) pada periode 2023-2025.
	        2. Mengoptimalkan performa prediksi cuaca dengan memanfaatkan metode ANN dan LSTM untuk 
            mengidentifikasi pola cuaca yang lebih kompleks, terutama yang berhubungan dengan 
            ketergantungan jangka panjang dalam data cuaca.
	        3. Menilai akurasi model prediksi yang dibangun dengan membandingkan hasil prediksi dari 
            ANN dan LSTM untuk memastikan metode yang paling sesuai digunakan untuk prediksi cuaca Kota 
            Surabaya.
            4. Memberikan kontribusi dalam pengembangan model prediksi cuaca berbasis teknologi 
            kecerdasan buatan di Indonesia, khususnya untuk meningkatkan kualitas peramalan cuaca di 
            wilayah perkotaan yang dinamis.
	    """)
        with tab3:
            st.info("""
            Penelitian ini memberikan berbagai manfaat yang dapat diterapkan dalam bidang meteorologi 
            dan kehidupan sehari-hari, antara lain:
            1. Meningkatkan akurasi prediksi cuaca Kota Surabaya
            Dengan menggunakan model ANN dan LSTM, penelitian ini dapat memberikan prediksi cuaca yang 
            lebih akurat dan relevan untuk wilayah Kota Surabaya, membantu masyarakat dalam merencanakan 
            kegiatan mereka dengan lebih tepat.
            2. Mendukung pengambilan keputusan
            Hasil prediksi cuaca yang lebih akurat dapat membantu pemerintah daerah, sektor transportasi,
            pertanian, dan sektor lainnya dalam merencanakan kebijakan atau aktivitas yang lebih efisien,
            terutama yang bergantung pada kondisi cuaca.
            3. Meningkatkan kesiapsiagaan terhadap bencana cuaca ekstrem
            Dengan model prediksi cuaca yang lebih canggih, dapat dilakukan deteksi lebih awal terhadap 
            potensi cuaca ekstrem, seperti hujan lebat atau angin kencang, yang dapat mengurangi risiko 
            bencana dan kerugian bagi masyarakat.
            4. Kontribusi terhadap penelitian meteorologi berbasis kecerdasan buatan
            Penelitian ini juga memberikan kontribusi dalam pengembangan model-model prediksi cuaca 
            berbasis kecerdasan buatan (AI), memperkenalkan pendekatan ANN dan LSTM sebagai alat yang 
            efektif dalam analisis data cuaca yang dinamis.
            5. Peningkatan pemahaman tentang pola cuaca tropis
            Penelitian ini dapat membantu memetakan pola cuaca di daerah tropis, khususnya di Surabaya, 
            yang memiliki tantangan cuaca dan iklim yang spesifik, memberikan wawasan lebih dalam tentang b
            agaimana cuaca berkembang di kawasan tersebut.
            """)
    with st.expander("Metode"):
        st.write("""
            Neural Network (NN) adalah model komputasi yang terinspirasi oleh cara kerja otak 
            manusia dalam memproses informasi. Salah satu varian dari NN adalah Artificial Neural 
            Network (ANN) yang telah terbukti efektif dalam memecahkan berbagai masalah termasuk 
            dalam prediksi cuaca. ANN bekerja dengan cara menghubungkan sejumlah besar unit 
            pemrosesan sederhana yang disebut neuron, yang saling terhubung dalam lapisan-lapisan 
            dan mempelajari pola dari data yang ada. Sementara itu, Long Short-Term Memory (LSTM) 
            merupakan bagian dari keluarga Neural Network yang diturunkan dari Recurrent Neural 
            Network (RNN). RNN adalah jenis neural network yang dirancang untuk menangani data 
            berurutan (sequential data), di mana output pada suatu waktu dipengaruhi oleh input 
            pada waktu sebelumnya. Namun, RNN memiliki kelemahan yang sering terjadi masalah 
            vanishing gradient dan exploding gradient. Keterbatasan metode RNN menjadi pemicu 
            dalam munculnya metode LSTM. Long Short-Term Memory (LSTM) adalah jenis jaringan 
            syaraf tiruan yang lebih spesifik yang dirancang untuk menangani data berurutan 
            seperti data cuaca yang memiliki ketergantungan waktu. LSTM sangat berguna untuk 
            memodelkan peramalan cuaca jangka panjang, karena kemampuannya dalam mengingat 
            informasi historis dan memprediksi tren cuaca yang lebih kompleks dan berubah seiring 
            waktu. Kombinasi antara ANN dan LSTM memberikan potensi besar untuk meningkatkan 
            akurasi prediksi cuaca, terutama dalam situasi yang melibatkan banyak variabel yang 
            saling berinteraksi.
        """)

    # Load Dataset
    df = load_data("data/df_hujan.csv")
	st.write(df.head())  
	st.write(df.columns)
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    df.set_index('tanggal', inplace=True)

    #Menampilkan data hujan
    st.divider()
    st.subheader("Data Cuaca Tahun 2023-2025")
    st.dataframe(df, use_container_width=True)
    url1 = "https://dataonline.bmkg.go.id/home"
    st.caption("Data cuaca Kota Surabaya diperoleh melalui website BMKG Tahun 2023-2025(%s)" % url1)
