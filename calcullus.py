import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# =============================
#       CONFIG HALAMAN
# =============================
st.set_page_config(page_title="Aplikasi Kalkulus & Matriks", layout="wide")

# =============================
#       PILIH BAHASA
# =============================
language = st.sidebar.radio("Pilih Bahasa / Choose Language:", ["Bahasa Indonesia", "English"])

# =============================
#       JUDUL
# =============================
if language == "Bahasa Indonesia":
    st.title("📘 Aplikasi Kalkulus & Matriks")
    st.write("Selamat datang di aplikasi final project Kalkulus & Matriks.")
else:
    st.title("📘 Calculus & Matrices App")
    st.write("Welcome to the final project Calculus & Matrices app.")

# =============================
#       FOTO ANGGOTA KELOMPOK
# =============================
st.header("👥 Anggota Kelompok" if language == "Bahasa Indonesia" else "👥 Group Members")
cols = st.columns(4)

with cols[0]:
    st.image(
        "https://printed-amethyst-lljrkyuwdm-s5iecdnwun.edgeone.dev/a2464207-e6f1-4f25-9bce-1d230733b846.jpeg",
        caption="1. Raka Raya Pratama", width=250
    )
with cols[1]:
    st.image(
        "https://bored-pink-bfe6q7k27z-opxswhtwta.edgeone.dev/a8cc0aaa-9064-4fe4-9e4a-5dfbbafa188e.jpeg",
        caption="2. Faqih Ahmad Hersanto", width=250
    )
with cols[2]:
    st.image(
        "https://essential-coffee-ckkctskbqm-k1ufq8gqyq.edgeone.dev/5cea401c-d11b-472d-8432-99cb2bf0d364.jpeg",
        caption="3. Fajar Dewo Haryanto", width=250
    )
with cols[3]:
    st.image(
        "https://automatic-coffee-wwi6lb8ump-4yibjm8v8m.edgeone.dev/IMG_1557.png",
        caption="4. Honey Gunawan", width=250
    )

# =============================
#       MENU APLIKASI
# =============================
menu = st.sidebar.selectbox(
    "Pilih menu / Choose menu:",
    ["Derivatif", "Integral", "Matriks", "Kurva 3D", "Optimasi Cerita"]
)

# =============================
#       FITUR DERIVATIF
# =============================
if menu == "Derivatif":
    st.header("🧮 Menghitung Turunan (Derivatif)" if language=="Bahasa Indonesia" else "🧮 Compute Derivative")
    expr_input = st.text_input("Masukkan fungsi (misal: x**2 + 3*x + 2): " if language=="Bahasa Indonesia" else "Enter function (e.g., x**2 + 3*x + 2): ")
    x = sp.Symbol("x")
    if st.button("Hitung Derivatif" if language=="Bahasa Indonesia" else "Compute Derivative"):
        try:
            expr = sp.sympify(expr_input)
            derivative = sp.diff(expr, x)
            st.success(f"Turunan: {derivative}" if language=="Bahasa Indonesia" else f"Derivative: {derivative}")
        except Exception as e:
            st.error(f"Error: {e}")

# =============================
#       FITUR INTEGRAL
# =============================
elif menu == "Integral":
    st.header("📐 Menghitung Integral" if language=="Bahasa Indonesia" else "📐 Compute Integral")
    expr_input = st.text_input("Masukkan fungsi (misal: x**2 + 3*x): " if language=="Bahasa Indonesia" else "Enter function (e.g., x**2 + 3*x): ")
    x = sp.Symbol("x")
    if st.button("Hitung Integral" if language=="Bahasa Indonesia" else "Compute Integral"):
        try:
            expr = sp.sympify(expr_input)
            integral = sp.integrate(expr, x)
            st.success(f"Hasil Integral: {integral} + C" if language=="Bahasa Indonesia" else f"Integral result: {integral} + C")
        except Exception as e:
            st.error(f"Error: {e}")

# =============================
#       FITUR MATRIKS
# =============================
elif menu == "Matriks":
    st.header("🔢 Operasi Matriks" if language=="Bahasa Indonesia" else "🔢 Matrix Operations")
    st.write("Masukkan matriks A dan B dengan format:" if language=="Bahasa Indonesia" else "Enter matrices A and B like this:")
    st.code("1 2\n3 4", language="text")
    A_input = st.text_area("Matriks A" if language=="Bahasa Indonesia" else "Matrix A")
    B_input = st.text_area("Matriks B" if language=="Bahasa Indonesia" else "Matrix B")
    def parse_matrix(text):
        return np.array([[float(num) for num in row.split()] for row in text.splitlines()])
    if st.button("Hitung Operasi Matriks" if language=="Bahasa Indonesia" else "Compute Matrix Operations"):
        try:
            A = parse_matrix(A_input)
            B = parse_matrix(B_input)
            st.write("### Matriks A:" if language=="Bahasa Indonesia" else "### Matrix A:")
            st.write(A)
            st.write("### Matriks B:" if language=="Bahasa Indonesia" else "### Matrix B:")
            st.write(B)
            st.write("### A + B:" if language=="Bahasa Indonesia" else "### A + B:")
            st.write(A + B)
            st.write("### A × B:" if language=="Bahasa Indonesia" else "### A × B:")
            st.write(A @ B)
            st.write("### Determinan A:" if language=="Bahasa Indonesia" else "### Determinant of A:")
            st.write(np.linalg.det(A))
        except Exception as e:
            st.error(f"Error: {e}")

# =============================
#       FITUR KURVA 3D
# =============================
elif menu == "Kurva 3D":
    st.header("📊 Visualisasi Kurva 3D" if language=="Bahasa Indonesia" else "📊 3D Curve Visualization")
    st.write("Masukkan fungsi dalam bentuk f(x, y)" if language=="Bahasa Indonesia" else "Enter a function in f(x, y) form")
    st.code("Contoh: x**2 + y**2" if language=="Bahasa Indonesia" else "Example: x**2 + y**2", language="python")
    func_input = st.text_input("Masukkan fungsi z = f(x, y):" if language=="Bahasa Indonesia" else "Enter function z = f(x, y):", "x**2 + y**2")
    x, y = sp.symbols('x y')
    x_range = st.slider("Rentang x" if language=="Bahasa Indonesia" else "X range", -10, 10, (-5, 5))
    y_range = st.slider("Rentang y" if language=="Bahasa Indonesia" else "Y range", -10, 10, (-5, 5))
    if st.button("Tampilkan Kurva 3D" if language=="Bahasa Indonesia" else "Show 3D Curve"):
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
            st.error(f"Terjadi kesalahan: {e}" if language=="Bahasa Indonesia" else f"Error occurred: {e}")

# =============================
#       FITUR OPTIMASI CERITA
# =============================
elif menu == "Optimasi Cerita":
    st.header("📊 Optimasi Cerita / Story Optimization")
    
    problem_type = st.selectbox(
        "Pilih tipe optimasi / Choose optimization type:",
        ["Luas / Area", "Keliling / Perimeter", "Volume", "Keuntungan / Profit"]
    )

    if problem_type == "Luas / Area":
        L, W = sp.symbols('L W', real=True, positive=True)
        perimeter = st.number_input("Masukkan keliling / Enter perimeter:", value=20)
        area = L * W
        W_expr = (perimeter/2 - L)
        area_expr = area.subs(W, W_expr)
        derivative = sp.diff(area_expr, L)
        solution = sp.solve(derivative, L)[0]
        max_area = area_expr.subs(L, solution)
        if st.button("Hitung / Compute"):
            st.success(f"Panjang optimal L = {solution}, Luas maksimum = {max_area}" if language=="Bahasa Indonesia" else f"Optimal length L = {solution}, Maximum area = {max_area}")

    elif problem_type == "Keliling / Perimeter":
        L, W = sp.symbols('L W', real=True, positive=True)
        area = st.number_input("Masukkan luas / Enter area:", value=20)
        perimeter_expr = 2*(L + W)
        W_expr = area/L
        perimeter_expr = perimeter_expr.subs(W, W_expr)
        derivative = sp.diff(perimeter_expr, L)
        solution = sp.solve(derivative, L)[0]
        min_perimeter = perimeter_expr.subs(L, solution)
        if st.button("Hitung / Compute"):
            st.success(f"Panjang optimal L = {solution}, Keliling minimum = {min_perimeter}" if language=="Bahasa Indonesia" else f"Optimal length L = {solution}, Minimum perimeter = {min_perimeter}")

    elif problem_type == "Volume":
        L, W, H = sp.symbols('L W H', real=True, positive=True)
        st.write("Masukkan panjang, lebar atau tinggi yang diketahui. Gunakan 0 untuk yang dicari." if language=="Bahasa Indonesia" else "Enter known length, width or height. Use 0 for unknown.")
        known_L = st.number_input("Panjang / Length:", value=0)
        known_W = st.number_input("Lebar / Width:", value=0)
        known_H = st.number_input("Tinggi / Height:", value=0)
        if st.button("Hitung / Compute Volume"):
            V = L * W * H
            if known_L!=0:
                V = V.subs(L, known_L)
            if known_W!=0:
                V = V.subs(W, known_W)
            if known_H!=0:
                V = V.subs(H, known_H)
            derivative_L = sp.diff(V, L)
            solution_L = sp.solve(derivative_L, L)
            st.success(f"Volume = {V}" if language=="Bahasa Indonesia" else f"Volume = {V}")

    elif problem_type == "Keuntungan / Profit":
        x = sp.Symbol('x', real=True)
        st.write("Masukkan fungsi pendapatan R(x) dan biaya C(x)" if language=="Bahasa Indonesia" else "Enter revenue R(x) and cost C(x)")
        revenue_input = st.text_input("Pendapatan R(x) / Revenue R(x):", "100*x")
        cost_input = st.text_input("Biaya C(x) / Cost C(x):", "40*x")
        R = sp.sympify(revenue_input)
        C = sp.sympify(cost_input)
        profit = R - C
        derivative = sp.diff(profit, x)
        solution = sp.solve(derivative, x)
        max_profit = profit.subs(x, solution[0])
        if st.button("Hitung / Compute Profit"):
            st.success(f"Jumlah optimal x = {solution[0]}, Keuntungan maksimum = {max_profit}" if language=="Bahasa Indonesia" else f"Optimal x = {solution[0]}, Maximum profit = {max_profit}")
