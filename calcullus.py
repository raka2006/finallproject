import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aplikasi Kalkulus & Matriks", layout="wide")

st.title("📘 Aplikasi Kalkulus & Matriks")
st.write("Selamat datang di aplikasi final project Kalkulus & Matriks.")

# =========================================================
#                   FOTO ANGGOTA KELOMPOK
# =========================================================
st.header("👥 Anggota Kelompok")

cols = st.columns(4)

with cols[0]:
    st.image(
        "https://printed-amethyst-lljrkyuwdm-s5iecdnwun.edgeone.dev/a2464207-e6f1-4f25-9bce-1d230733b846.jpeg",
        caption="1. Raka Raya Pratama",
        use_column_width=True
    )

with cols[1]:
    st.image(
        "https://bored-pink-bfe6q7k27z-opxswhtwta.edgeone.dev/a8cc0aaa-9064-4fe4-9e4a-5dfbbafa188e.jpeg",
        caption="2. Faqih Ahmad Hersanto",
        use_column_width=True
    )

with cols[2]:
    st.image(
        "https://essential-coffee-ckkctskbqm-k1ufq8gqyq.edgeone.dev/5cea401c-d11b-472d-8432-99cb2bf0d364.jpeg",
        caption="3. Fajar Dewo Haryanto",
        use_column_width=True
    )

with cols[3]:
    st.image(
        "https://automatic-coffee-wwi6lb8ump-4yibjm8v8m.edgeone.dev/IMG_1557.png",
        caption="4. Honey Gunawan",
        use_column_width=True
    )

# =========================================================
#                   MENU APLIKASI
# =========================================================
menu = st.sidebar.selectbox(
    "Pilih menu:",
    ["Derivatif", "Integral", "Matriks"]
)

# =========================================================
#                FITUR DERIVATIF
# =========================================================
if menu == "Derivatif":
    st.header("🧮 Menghitung Turunan (Derivatif)")

    expr_input = st.text_input("Masukkan fungsi (misal: x**2 + 3*x + 2): ")
    x = sp.Symbol("x")

    if st.button("Hitung Derivatif"):
        try:
            expr = sp.sympify(expr_input)
            derivative = sp.diff(expr, x)
            st.success(f"Turunan: {derivative}")
        except Exception as e:
            st.error(f"Error: {e}")

# =========================================================
#                FITUR INTEGRAL
# =========================================================
elif menu == "Integral":
    st.header("📐 Menghitung Integral")

    expr_input = st.text_input("Masukkan fungsi (misal: x**2 + 3*x): ")

    if st.button("Hitung Integral"):
        try:
            expr = sp.sympify(expr_input)
            integral = sp.integrate(expr, x)
            st.success(f"Hasil Integral: {integral} + C")
        except Exception as e:
            st.error(f"Error: {e}")

# =========================================================
#                FITUR MATRIKS
# =========================================================
elif menu == "Matriks":
    st.header("🔢 Operasi Matriks")

    st.write("Masukkan matriks A dan B dalam format contoh:")
    st.code("1 2 3\n4 5 6", language="text")

    A_input = st.text_area("Matriks A")
    B_input = st.text_area("Matriks B")

    def parse_matrix(text):
        return np.array([[float(num) for num in row.split()] for row in text.splitlines()])

    if st.button("Hitung Operasi Matriks"):
        try:
            A = parse_matrix(A_input)
            B = parse_matrix(B_input)

            st.write("### Matriks A:")
            st.write(A)

            st.write("### Matriks B:")
            st.write(B)

            st.write("### A + B:")
            st.write(A + B)

            st.write("### A × B:")
            st.write(A @ B)

            st.write("### Determinan A:")
            st.write(np.linalg.det(A))

        except Exception as e:
            st.error(f"Error: {e}")
