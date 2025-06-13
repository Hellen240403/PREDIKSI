import streamlit as st

def app():
    st.title("SkyWard Team")

    st.header("Inilah Kami")
    st.markdown("""
                Segenap mahasiswa Departemen Statistika Bisnis Angkatan 2022 yang sedang mengambil
                mata kuliah Machine Learning. Sebuah mata kuliah yang memperdalam ilmu kami dalam dunia 
                Artificial Intelligence (AI). Berfokus pada pelatihan dan pengembangan algoritma yang 
                diimplementasikan dalam dunia Statistika dan Bisnis. Melakukan project Prediksi Cuaca 
                yang diberi nama SkyWard sebagai perwujudan Kami atas kemahiran yang kami peroleh dari 
                mata kuliah Machine Learning.
        """)

    tab1, tab2, tab3 = st.tabs(["Dwi Ilham Ramadhany", "Hellen Aldenia Rovi", "Endita Prastyansyach"])

    # --- KONTEN TAB 1: DWI ILHAM RAMADHANY ---
    with tab1:
        col1, col2 = st.columns([1, 2], gap="medium")
        with col1:
            # Ganti dengan URL atau path ke foto Dwi
            st.image("https://i.imgur.com/FBLf82s.jpeg", caption="Dwi Ilham Ramadhany", use_column_width=True)

        with col2:
            st.subheader(" Dwi Ilham Ramadhany ")
            st.markdown(" Bangkalan, 7 November 2003 ")
            st.markdown(" 2043221054 ")
            
            st.markdown("---") # Garis pemisah
            
            st.markdown("#### Motivasi")
            st.info("""
            "Investasikanlah kesehatanmu selama mungkin."
            """)
            
            st.markdown("---") # Garis pemisah
            
            st.markdown("#### Kontak")
            st.markdown("📧 dwrmdhany11@gmail.com")


    # --- KONTEN TAB 2: HELLEN ALDENIA ROVI ---
    with tab2:
        col1, col2 = st.columns([1, 2], gap="medium")
        with col1:
            # Ganti dengan URL atau path ke foto Hellen
            st.image("https://i.imgur.com/eBf23v8.jpeg", caption="Hellen Aldenia Rovi", use_column_width=True)

        with col2:
            st.subheader("Hellen Aldenia Rovi")
            st.markdown("**Tempat, Tanggal Lahir:** Malang, 22 Agustus 2004")
            st.markdown("**NIM:** 12221032")
            
            st.markdown("---") # Garis pemisah
            
            st.markdown("#### Motivasi")
            st.info("""
            "Mengubah pola yang kompleks menjadi cerita yang sederhana dan dapat ditindaklanjuti adalah keajaiban sejati dari statistika."
            """)

            st.markdown("---") # Garis pemisah
            
            st.markdown("#### Kontak")
            st.markdown("📧 hellen.aldenia.skyward@gmail.com")

    # --- KONTEN TAB 3: ENDITA PRASTYANSYACH ---
    with tab3:
        col1, col2 = st.columns([1, 2], gap="medium")
        with col1:
            # Ganti dengan URL atau path ke foto Endita
            st.image("https://i.imgur.com/j4oXWqg.jpeg", caption="Endita Prastyansyach", use_column_width=True)

        with col2:
            st.subheader("Endita Prastyansyach")
            st.markdown("**Tempat, Tanggal Lahir:** Sidoarjo, 10 Januari 2004")
            st.markdown("**NIM:** 12221048")
            
            st.markdown("---") # Garis pemisah
            
            st.markdown("#### Motivasi")
            st.info("""
            "Tujuannya adalah membangun sistem cerdas yang tidak hanya memprediksi masa depan, tetapi juga membantu kita menciptakan masa depan yang lebih baik."
            """)

            st.markdown("---") # Garis pemisah
            
            st.markdown("#### Kontak")
            st.markdown("📧 endita.pras.skyward@gmail.com")

    st.subheader("Data Variabel")
    st.markdown("""
    Data yang digunakan dalam Prediksi Cuaca diambil dari laman resmi Badan Meteorologi, Klimatologi, dan Geofisika
    [Badan Meteorologi, Klimatologi, dan Geofisika](https://dataonline.bmkg.go.id/data_harian)
    
    Terimakasih kepada Lembaga Badan Meteorologi, Klimatologi, dan Geofisika yang menyediakan data 
    dengan akses yang sangat terjangkau. 
    """)

    




