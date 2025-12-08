import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aplikasi Kalkulus & Matriks", layout="wide")

st.title("📘 Aplikasi Kalkulus & Matriks & Soal Cerita")
st.write("Selamat datang di aplikasi final project Kalkulus, Matriks, dan Soal Cerita Interaktif.")

# =========================================================
#                   FOTO ANGGOTA KELOMPOK
# =========================================================
st.header("👥 Anggota Kelompok")

cols = st.columns(4)

with cols[0]:
    st.image(
        "https://printed-amethyst-lljrkyuwdm-s5iecdnwun.edgeone.dev/a2464207-e6f1-4f25-9bce-1d230733b846.jpeg",
        caption="1. Raka Raya Pratama",
        width=250
    )

with cols[1]:
    st.image(
        "https://bored-pink-bfe6q7k27z-opxswhtwta.edgeone.dev/a8cc0aaa-9064-4fe4-9e4a-5dfbbafa188e.jpeg",
        caption="2. Faqih Ahmad Hersanto",
        width=250
    )

with cols[2]:
    st.image(
        "https://essential-coffee-ckkctskbqm-k1ufq8gqyq.edgeone.dev/5cea401c-d11b-472d-8432-99cb2bf0d364.jpeg",
        caption="3. Fajar Dewo Haryanto",
        width=250
    )

with cols[3]:
    st.image(
        "https://automatic-coffee-wwi6lb8ump-4yibjm8v8m.edgeone.dev/IMG_1557.png",
        caption="4. Honey Gunawan",
        width=250
    )

# =========================================================
#                   MENU APLIKASI
# =========================================================
menu = st.sidebar.selectbox(
    "Pilih menu / Select menu:",
    ["Derivatif", "Integral", "Matriks", "Kurva 3D", "Soal Cerita Interaktif / Story Problem"]
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
    x = sp.Symbol("x")

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

    st.write("Masukkan matriks A dan B dengan format:")
    st.code("1 2\n3 4", language="text")

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

# =========================================================
#                FITUR KURVA 3D
# =========================================================
elif menu == "Kurva 3D":
    st.header("📊 Visualisasi Kurva 3D")

    st.write("Masukkan fungsi dalam bentuk f(x, y)")
    st.code("Contoh: x**2 + y**2", language="python")

    func_input = st.text_input("Masukkan fungsi z = f(x, y):", "x**2 + y**2")

    x = sp.Symbol("x")
    y = sp.Symbol("y")

    x_range = st.slider("Rentang x", -10, 10, (-5, 5))
    y_range = st.slider("Rentang y", -10, 10, (-5, 5))

    if st.button("Tampilkan Kurva 3D"):
        try:
            expr = sp.sympify(func_input)
            f = sp.lambdify((x, y), expr, "numpy")

            X = np.linspace(x_range[0], x_range[1], 50)
            Y = np.linspace(y_range[0], y_range[1], 50)
            X, Y = np.meshgrid(X, Y)
            Z = f(X, Y)

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(X, Y, Z)

            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_zlabel("Z")

            st.pyplot(fig)

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

# =========================================================
#                FITUR SOAL CERITA INTERAKTIF
# =========================================================
elif menu == "Soal Cerita Interaktif / Story Problem":
    st.header("📖 Soal Cerita Interaktif / Story Problem")

    bahasa = st.radio("Pilih bahasa / Select language:", ["Indonesia", "English"])

    if bahasa == "Indonesia":
        st.subheader("Masukkan fungsi dalam bentuk x (misal: x*(10-x) untuk luas)")
        st.write("Gunakan `x` sebagai variabel. Aplikasi akan menampilkan nilai maksimum/minimum.")
    else:
        st.subheader("Enter function in terms of x (e.g., x*(10-x) for area)")
        st.write("Use `x` as variable. The app will find maximum/minimum value.")

    func_input = st.text_input("Fungsi / Function:", "x*(10-x)")
    x = sp.Symbol("x")

    if st.button("Hitung / Solve"):
        try:
            expr = sp.sympify(func_input)
            derivative = sp.diff(expr, x)
            critical_points = sp.solve(derivative, x)

            results = []
            for point in critical_points:
                value = expr.subs(x, point)
                results.append((point, value))

            max_point = max(results, key=lambda t: t[1])
            min_point = min(results, key=lambda t: t[1])

            if bahasa == "Indonesia":
                st.success(f"Nilai maksimum: x = {max_point[0]}, f(x) = {max_point[1]}")
                st.success(f"Nilai minimum: x = {min_point[0]}, f(x) = {min_point[1]}")
            else:
                st.success(f"Maximum value: x = {max_point[0]}, f(x) = {max_point[1]}")
                st.success(f"Minimum value: x = {min_point[0]}, f(x) = {min_point[1]}")

        except Exception as e:
            st.error(f"Terjadi kesalahan / Error: {e}")
elif menu == "Soal Cerita Interaktif / Story Problem":
    st.header("📖 Soal Cerita Interaktif / Story Problem")

    bahasa = st.radio("Pilih bahasa / Select language:", ["Indonesia", "English"])

    if bahasa == "Indonesia":
        st.subheader("Masukkan fungsi dalam bentuk x (misal: x*(10-x) untuk luas)")
        st.write("Gunakan `x` sebagai variabel. Aplikasi akan menampilkan nilai maksimum/minimum.")
    else:
        st.subheader("Enter function in terms of x (e.g., x*(10-x) for area)")
        st.write("Use `x` as variable. The app will find maximum/minimum value.")

    func_input = st.text_input("Fungsi / Function:", "x*(10-x)")
    x = sp.Symbol("x")

    if st.button("Hitung / Solve"):
        try:
            expr = sp.sympify(func_input)
            derivative = sp.diff(expr, x)
            critical_points = sp.solve(derivative, x)

            results = []
            for point in critical_points:
                value = expr.subs(x, point)
                results.append((point, value))

            max_point = max(results, key=lambda t: t[1])
            min_point = min(results, key=lambda t: t[1])

            if bahasa == "Indonesia":
                st.success(f"Nilai maksimum: x = {max_point[0]}, f(x) = {max_point[1]}")
                st.success(f"Nilai minimum: x = {min_point[0]}, f(x) = {min_point[1]}")
            else:
                st.success(f"Maximum value: x = {max_point[0]}, f(x) = {max_point[1]}")
                st.success(f"Minimum value: x = {min_point[0]}, f(x) = {min_point[1]}")

        except Exception as e:
            st.error(f"Terjadi kesalahan / Error: {e}")
elif menu == "Soal Cerita Interaktif / Story Problem":
    st.header("📖 Soal Cerita Interaktif / Story Problem")

    bahasa = st.radio("Pilih bahasa / Select language:", ["Indonesia", "English"])

    if bahasa == "Indonesia":
        st.subheader("Masukkan fungsi dalam bentuk x (misal: x*(10-x) untuk luas)")
        st.write("Gunakan `x` sebagai variabel. Aplikasi akan menampilkan nilai maksimum/minimum.")
    else:
        st.subheader("Enter function in terms of x (e.g., x*(10-x) for area)")
        st.write("Use `x` as variable. The app will find maximum/minimum value.")

    func_input = st.text_input("Fungsi / Function:", "x*(10-x)")
    x = sp.Symbol("x")

    if st.button("Hitung / Solve"):
        try:
            expr = sp.sympify(func_input)
            derivative = sp.diff(expr, x)
            critical_points = sp.solve(derivative, x)

            results = []
            for point in critical_points:
                value = expr.subs(x, point)
                results.append((point, value))

            max_point = max(results, key=lambda t: t[1])
            min_point = min(results, key=lambda t: t[1])

            if bahasa == "Indonesia":
                st.success(f"Nilai maksimum: x = {max_point[0]}, f(x) = {max_point[1]}")
                st.success(f"Nilai minimum: x = {min_point[0]}, f(x) = {min_point[1]}")
            else:
                st.success(f"Maximum value: x = {max_point[0]}, f(x) = {max_point[1]}")
                st.success(f"Minimum value: x = {min_point[0]}, f(x) = {min_point[1]}")

        except Exception as e:
            st.error(f"Terjadi kesalahan / Error: {e}")
elif menu == "Soal Cerita Interaktif / Story Problem":
    st.header("📖 Soal Cerita Interaktif / Story Problem")

    bahasa = st.radio("Pilih bahasa / Select language:", ["Indonesia", "English"])

    if bahasa == "Indonesia":
        st.subheader("Masukkan fungsi dalam bentuk x (misal: x*(10-x) untuk luas)")
        st.write("Gunakan `x` sebagai variabel. Aplikasi akan menampilkan nilai maksimum/minimum.")
    else:
        st.subheader("Enter function in terms of x (e.g., x*(10-x) for area)")
        st.write("Use `x` as variable. The app will find maximum/minimum value.")

    func_input = st.text_input("Fungsi / Function:", "x*(10-x)")
    x = sp.Symbol("x")

    if st.button("Hitung / Solve"):
        try:
            expr = sp.sympify(func_input)
            derivative = sp.diff(expr, x)
            critical_points = sp.solve(derivative, x)

            results = []
            for point in critical_points:
                value = expr.subs(x, point)
                results.append((point, value))

            max_point = max(results, key=lambda t: t[1])
            min_point = min(results, key=lambda t: t[1])

            if bahasa == "Indonesia":
                st.success(f"Nilai maksimum: x = {max_point[0]}, f(x) = {max_point[1]}")
                st.success(f"Nilai minimum: x = {min_point[0]}, f(x) = {min_point[1]}")
            else:
                st.success(f"Maximum value: x = {max_point[0]}, f(x) = {max_point[1]}")
                st.success(f"Minimum value: x = {min_point[0]}, f(x) = {min_point[1]}")

        except Exception as e:
            st.error(f"Terjadi kesalahan / Error: {e}")
