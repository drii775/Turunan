import streamlit as st
from sympy import symbols, diff, simplify
from streamlit_option_menu import option_menu

#navigasi sidebar
with st.sidebar :
    selected = option_menu('Menu',
    ['Home','Panduan Program','Rumus'],
    default_index=0)

#halaman panduan program
if (selected == 'Home') :
    st.title('KALKULUS I') 
    st.text('Turunan Aljabar')

#halaman panduan program
if (selected == 'Panduan Program') :
    st.title('Panduan Program')
    
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
            st.write("Fungsi asli =", fungsi)

            # Menampilkan turunan 
            st.write("Turunan pertama =", turunan_pertama)
            st.write("Turunan kedua =", turunan_kedua)
            st.write("Turunan ketiga =", turunan_ketiga)
            #st.success(f"Turunannya adalah = {turunan_pertama}")

        except Exception as e:
            st.write("Terjadi kesalahan:", e)

    def main():
        st.title("Kalkulator Turunan Aljabar")

        # Menerima ekspresi dari pengguna
        ekspresi = st.text_input("Masukkan ekspresi aljabar dalam bentuk Python (gunakan x sebagai variabel):")

        # Memanggil kalkulator_turunan jika pengguna menekan tombol "Hitung"
        if st.button("Hitung"):
            kalkulator_turunan(ekspresi)
            

    if __name__ == "__main__":
        main()
