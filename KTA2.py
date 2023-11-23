import streamlit as st
from sympy import symbols, diff, simplify
from streamlit_option_menu import option_menu

#navigasi sidebar
with st.sidebar :
    selected = option_menu('Menu',
    ['Home','Panduan Program','Rumus'],
    default_index=0)

# Sambungkan file CSS
st.markdown(
    '<link rel="stylesheet" type="text/css" href="styles.css">',
    unsafe_allow_html=True
)

#halaman panduan program
if (selected == 'Home') :
    st.title('KALKULUS I') 
    st.write('Turunan Aljabar')
    # Tambahkan informasi kelompok
    st.write('Anggota Kelompok :')
    st.write('- Ririn Rahma Arifa_237006171_Kelas F')
    st.write('- Tia Amelia_237006162_Kelas E')
    st.write('- Rheyna Louisa_237006169_Kelas F')

# Fungsi untuk mengganti operator pangkat
def ganti_operator_pangkat(ekspresi):
    ekspresi = ekspresi.replace('^', '**')
    return ekspresi

#halaman panduan program
if (selected == 'Panduan Program') :
    st.title('PANDUAN PROGRAM')
    #panduan
    st.write('PANDUAN SIDEBAR :')
    st.write('1. Home, menampilkan menu utama')
    st.write('2. Panduan Program, menampilkan petunjuk untuk menggunakan program')
    st.write('3. Rumus, menampilkan kalkultor turunan aljabar')
    st.write('')
    st.write('PANDUAN MENU RUMUS :')
    st.write('1. Nilai dapat diisi dengan niali positif dan negatif')
    st.write('2. Nilai dapat diisi dengan negatif tak hingga sampai positif tak hingga')
    st.write('3. Untuk menambahkan variabel "X" gunakan symbol bintang (*)')
    st.write('4. Untuk menambahkan pangkat gunakan symbol sirkumfleks (^)')
    st.write('5. Tombol hitung digunakan untuk menampilkan hasil turunan')
    st.write('6. Tombol enter pada keyboard dapat digunakan untuk menghapus seluruh hasil turunan')


#halaman rumus
if (selected == 'Rumus') :
    def kalkulator_turunan(ekspresi):
        # Membuat simbol variabel
        x = symbols('x')

        try:
            # Mengevaluasi ekspresi dan menghitung turunan pertama
            fungsi = simplify(ekspresi)
            #turunan_pertama = diff(fungsi, x)
            # Turunan pertama
            turunan_pertama = diff(fungsi, x)

            # Turunan kedua
            turunan_kedua = diff(turunan_pertama, x)

            # Turunan ketiga
            turunan_ketiga = diff(turunan_kedua, x)

            # Menampilkan fungsi asli
            st.write("Fungsi asli f(x) =", fungsi)

            # Menampilkan turunan 
            st.write("Y ' =", turunan_pertama)
            st.write("Y '' =", turunan_kedua)
            st.write("Y ''' =", turunan_ketiga)
            #st.success(f"Turunannya adalah = {turunan_pertama}")

        except Exception as e:
            st.write("Terjadi kesalahan:", e)

    def main():
        st.title("Kalkulator Turunan Aljabar")

        # Menerima ekspresi dari pengguna
        ekspresi = st.text_input("Masukkan ekspresi turunanan aljabar")

        # Memanggil kalkulator_turunan jika pengguna menekan tombol "Hitung"
        if st.button("Hitung"):
            kalkulator_turunan(ekspresi)

            

    if __name__ == "__main__":
        main()
