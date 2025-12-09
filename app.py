import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go

st.set_page_config(page_title="Aplikasi Kalkulus & Matriks & Soal Cerita", layout="wide")

st.title("📘 Aplikasi Kalkulus, Matriks, Kurva 3D & Soal Cerita")
st.write("Selamat datang di aplikasi final project Kalkulus, Matriks, Kurva 3D, dan Soal Cerita Interaktif.")

# =========================================================
# FOTO ANGGOTA KELOMPOK
# =========================================================
st.header("👥 Anggota Kelompok")
cols = st.columns(4)

with cols[0]:
    st.image("https://printed-amethyst-lljrkyuwdm-s5iecdnwun.edgeone.dev/a2464207-e6f1-4f25-9bce-1d230733b846.jpeg", caption="1. Raka Raya Pratama", width=250)
with cols[1]:
    st.image("https://bored-pink-bfe6q7k27z-opxswhtwta.edgeone.dev/a8cc0aaa-9064-4fe4-9e4a-5dfbbafa188e.jpeg", caption="2. Faqih Ahmad Hersanto", width=250)
with cols[2]:
    st.image("https://essential-coffee-ckkctskbqm-k1ufq8gqyq.edgeone.dev/5cea401c-d11b-472d-8432-99cb2bf0d364.jpeg", caption="3. Fajar Dewo Haryanto", width=250)
with cols[3]:
    st.image("https://automatic-coffee-wwi6lb8ump-4yibjm8v8m.edgeone.dev/IMG_1557.png", caption="4. Honey Gunawan", width=250)

# =========================================================
# MENU APLIKASI
# =========================================================
menu = st.sidebar.selectbox(
    "Pilih menu / Select menu:",
    ["Derivatif", "Integral", "Matriks", "Kurva 3D", "Soal Cerita Interaktif / Story Problem"]
)

# =========================================================
# FITUR DERIVATIF
# =========================================================
if menu == "Derivatif":
    st.header("🧮 Turunan (Derivatif) 2D & 3D")
    expr_input = st.text_input("Masukkan fungsi f(x, y) (misal: x**2 + y**2):", "x**2 + y**2")
    x, y = sp.symbols("x y")
    
    if st.button("Hitung Turunan & Plot"):
        try:
            expr = sp.sympify(expr_input)
            fx = sp.diff(expr, x)
            fy = sp.diff(expr, y)
            st.success(f"Turunan parsial ∂f/∂x: {fx}")
            st.success(f"Turunan parsial ∂f/∂y: {fy}")
            
            # 2D Plot Turunan
            x_vals = np.linspace(-10,10,50)
            y_vals = np.linspace(-10,10,50)
            X, Y = np.meshgrid(x_vals, y_vals)
            f_lamb = sp.lambdify((x,y), expr, "numpy")
            Z = f_lamb(X,Y)
            
            fig2d = go.Figure()
            fig2d.add_trace(go.Contour(z=Z, x=x_vals, y=y_vals, colorscale="Viridis"))
            fig2d.update_layout(title="Kontur Fungsi f(x, y)")
            st.plotly_chart(fig2d, use_container_width=True)
            
            # 3D Plot Turunan
            fig3d = go.Figure()
            fig3d.add_trace(go.Surface(z=Z, x=X, y=Y, colorscale="Viridis"))
            fig3d.update_layout(title="Permukaan Fungsi f(x, y)", scene=dict(
                xaxis_title='X', yaxis_title='Y', zaxis_title='f(x,y)'
            ))
            st.plotly_chart(fig3d, use_container_width=True)
            
        except Exception as e:
            st.error(f"Error: {e}")

# =========================================================
# FITUR INTEGRAL
# =========================================================
elif menu == "Integral":
    st.header("📐 Integral 2D & 3D")
    expr_input = st.text_input("Masukkan fungsi f(x, y) (misal: x**2 + y**2):", "x**2 + y**2")
    x, y = sp.symbols("x y")
    
    if st.button("Hitung Integral & Plot"):
        try:
            expr = sp.sympify(expr_input)
            integral_x = sp.integrate(expr, x)
            integral_y = sp.integrate(expr, y)
            st.success(f"Integral terhadap x: {integral_x} + C")
            st.success(f"Integral terhadap y: {integral_y} + C")
            
            # 2D Plot
            x_vals = np.linspace(-10,10,50)
            y_vals = np.linspace(-10,10,50)
            X, Y = np.meshgrid(x_vals, y_vals)
            f_lamb = sp.lambdify((x,y), expr, "numpy")
            Z = f_lamb(X,Y)
            fig2d = go.Figure()
            fig2d.add_trace(go.Contour(z=Z, x=x_vals, y=y_vals, colorscale="Viridis"))
            fig2d.update_layout(title="Kontur Integral Fungsi f(x, y)")
            st.plotly_chart(fig2d, use_container_width=True)
            
            # 3D Plot
            fig3d = go.Figure()
            fig3d.add_trace(go.Surface(z=Z, x=X, y=Y, colorscale="Viridis"))
            fig3d.update_layout(title="Permukaan Integral Fungsi f(x, y)", scene=dict(
                xaxis_title='X', yaxis_title='Y', zaxis_title='f(x,y)'
            ))
            st.plotly_chart(fig3d, use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")

# =========================================================
# FITUR MATRIKS
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
# FITUR KURVA 3D
# =========================================================
elif menu == "Kurva 3D":
    st.header("📊 Visualisasi Kurva 3D")
    func_input_3d = st.text_input("Masukkan fungsi z = f(x, y):", "x**2 + y**2")
    x, y = sp.symbols("x y")
    x_range = st.slider("Rentang x", -10, 10, (-5, 5))
    y_range = st.slider("Rentang y", -10, 10, (-5, 5))
    if st.button("Tampilkan Kurva 3D"):
        try:
            expr = sp.sympify(func_input_3d)
            f = sp.lambdify((x, y), expr, "numpy")
            X = np.linspace(x_range[0], x_range[1], 50)
            Y = np.linspace(y_range[0], y_range[1], 50)
            X, Y = np.meshgrid(X, Y)
            Z = f(X, Y)
            fig = go.Figure()
            fig.add_trace(go.Surface(z=Z, x=X, y=Y, colorscale="Viridis"))
            fig.update_layout(title="Kurva 3D Interaktif", scene=dict(
                xaxis_title='X', yaxis_title='Y', zaxis_title='Z'
            ))
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")

# =========================================================
# FITUR SOAL CERITA INTERAKTIF
# =========================================================
elif menu == "Soal Cerita Interaktif / Story Problem":
    st.header("📖 Soal Cerita Interaktif / Story Problem")
    bahasa = st.radio("Pilih bahasa / Select language:", ["Indonesia", "English"])

    if bahasa == "Indonesia":
        st.subheader("Masukkan fungsi dalam bentuk x (misal: x*(10-x) untuk luas)")
        st.write("Gunakan `x` sebagai variabel. Aplikasi akan menampilkan nilai maksimum/minimum (luas, keliling, volume, keuntungan).")
    else:
        st.subheader("Enter function in terms of x (e.g., x*(10-x) for area)")
        st.write("Use `x` as variable. The app will find maximum/minimum value (area, perimeter, volume, profit).")

    func_input_story = st.text_input("Fungsi / Function:", "x*(10-x)")
    x_story = sp.Symbol("x")

    if st.button("Hitung Soal Cerita"):
        try:
            expr = sp.sympify(func_input_story)
            derivative = sp.diff(expr, x_story)
            critical_points = sp.solve(derivative, x_story)
            results = [(p, expr.subs(x_story, p)) for p in critical_points]

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
