import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols, diff, latex, solve
import re
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Mathematical Function & Optimization WebApp",
    page_icon="📊",
    layout="wide"
)

# Fungsi untuk parsing fungsi matematika
def parse_function(func_str):
    """Mengubah string fungsi menjadi ekspresi sympy"""
    try:
        x = symbols('x')
        # Replace eksponen Python dengan format sympy
        func_str = func_str.replace('^', '**')
        # Parse fungsi
        func = sp.sympify(func_str)
        return func, x
    except:
        return None, None

# Fungsi untuk menggambar plot
def plot_function(func, x_sym, x_range=(-10, 10), title="Function Plot"):
    """Membuat plot fungsi matematika"""
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    
    # Convert sympy function to numpy function
    func_numpy = sp.lambdify(x_sym, func, 'numpy')
    y_vals = func_numpy(x_vals)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'f(x) = {sp.pretty(func)}')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(x_range)
    
    return fig

# Fungsi untuk menghitung turunan dengan langkah-langkah
def calculate_derivative_steps(func, x_sym):
    """Menghitung turunan dengan menampilkan langkah-langkah"""
    steps = []
    
    # Langkah 1: Fungsi asli
    steps.append(("Fungsi Asli", f"f(x) = {sp.pretty(func)}"))
    steps.append(("Fungsi Asli (LaTeX)", f"${sp.latex(func)}$"))
    
    # Langkah 2: Turunan
    derivative = diff(func, x_sym)
    steps.append(("Turunan", f"f'(x) = {sp.pretty(derivative)}"))
    steps.append(("Turunan (LaTeX)", f"${sp.latex(derivative)}$"))
    
    return derivative, steps

# Fungsi untuk menyelesaikan masalah optimisasi
def solve_optimization_problem(problem_text):
    """Menyelesaikan masalah optimisasi dari teks"""
    try:
        # Contoh sederhana parsing masalah optimisasi
        if "volume" in problem_text.lower() and "kotak" in problem_text.lower():
            # Contoh: Kotak dengan volume maksimum
            x = symbols('x')
            # Asumsikan masalah volume kotak
            # Volume = x*(a-x)*(b-x) atau bentuk sederhana
            volume_func = x*(10-x)*(8-x)  # Contoh
            derivative = diff(volume_func, x)
            critical_points = solve(derivative, x)
            
            return {
                'problem_type': 'volume_box',
                'function': volume_func,
                'derivative': derivative,
                'critical_points': critical_points,
                'solution': f"Titik kritis: {critical_points}"
            }
        else:
            # Default: fungsi kuadrat
            x = symbols('x')
            func = -x**2 + 4*x + 5  # Contoh
            derivative = diff(func, x)
            critical_points = solve(derivative, x)
            
            return {
                'problem_type': 'quadratic',
                'function': func,
                'derivative': derivative,
                'critical_points': critical_points,
                'solution': f"Titik kritis: {critical_points}"
            }
    except:
        return None

# Halaman 1: Anggota Tim
def show_team_page():
    st.title("👥 Anggota Tim")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Nama Anggota 1")
        st.image("https://via.placeholder.com/150", caption="Foto Anggota 1", width=150)
        st.write("**Peran:** Project Manager & Developer")
        st.write("**Kontribusi:** Backend development, deployment")
    
    with col2:
        st.subheader("Nama Anggota 2")
        st.image("https://via.placeholder.com/150", caption="Foto Anggota 2", width=150)
        st.write("**Peran:** Frontend Developer")
        st.write("**Kontribusi:** UI/UX design, visualization")
    
    with col3:
        st.subheader("Nama Anggota 3")
        st.image("https://via.placeholder.com/150", caption="Foto Anggota 3", width=150)
        st.write("**Peran:** Matematika & Algoritma")
        st.write("**Kontribusi:** Mathematical modeling, optimization")

# Halaman 2: Visualisasi Fungsi & Turunan
def show_function_page():
    st.title("📈 Visualisasi Fungsi & Turunan")
    st.markdown("---")
    
    # Input fungsi
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Input Fungsi Matematika")
        func_input = st.text_input(
            "Masukkan fungsi f(x) (gunakan x sebagai variabel):",
            value="x**3 - 3*x**2 + 2",
            help="Contoh: x**2 + 2*x + 1, sin(x), exp(x), log(x)"
        )
    
    with col2:
        st.subheader("Rentang Plot")
        x_min = st.number_input("x minimum", value=-5.0)
        x_max = st.number_input("x maksimum", value=5.0)
    
    if func_input:
        func, x = parse_function(func_input)
        
        if func is not None:
            # Tampilkan fungsi dalam format yang mudah dibaca
            st.subheader("Fungsi Matematika")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Format Mudah Dibaca:**")
                st.code(f"f(x) = {sp.pretty(func)}")
            
            with col2:
                st.write("**Format LaTeX:**")
                st.latex(f"f(x) = {latex(func)}")
            
            # Plot fungsi asli
            st.subheader("Plot Fungsi")
            fig_original = plot_function(func, x, (x_min, x_max), "Fungsi Asli")
            st.pyplot(fig_original)
            
            # Hitung dan tampilkan turunan
            st.subheader("Kalkulasi Turunan")
            derivative, steps = calculate_derivative_steps(func, x)
            
            for step_name, step_content in steps:
                with st.expander(f"📝 {step_name}"):
                    if "LaTeX" in step_name:
                        st.latex(step_content)
                    else:
                        st.code(step_content)
            
            # Plot turunan
            st.subheader("Plot Fungsi Turunan")
            fig_derivative = plot_function(derivative, x, (x_min, x_max), "Fungsi Turunan")
            st.pyplot(fig_derivative)
            
            # Plot gabungan
            st.subheader("Perbandingan Fungsi dan Turunannya")
            fig_comparison, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
            
            x_vals = np.linspace(x_min, x_max, 400)
            func_numpy = sp.lambdify(x, func, 'numpy')
            deriv_numpy = sp.lambdify(x, derivative, 'numpy')
            
            ax1.plot(x_vals, func_numpy(x_vals), 'b-', linewidth=2, label=f'f(x) = {sp.pretty(func)}')
            ax1.set_title('Fungsi Asli')
            ax1.grid(True, alpha=0.3)
            ax1.legend()
            
            ax2.plot(x_vals, deriv_numpy(x_vals), 'r-', linewidth=2, label=f"f'(x) = {sp.pretty(derivative)}")
            ax2.set_title('Fungsi Turunan')
            ax2.grid(True, alpha=0.3)
            ax2.legend()
            
            st.pyplot(fig_comparison)
            
        else:
            st.error("❌ Error dalam parsing fungsi. Pastikan format benar!")

# Halaman 3: Penyelesaian Masalah Optimisasi
def show_optimization_page():
    st.title("🎯 Penyelesaian Masalah Optimisasi")
    st.markdown("---")
    
    st.subheader("Input Masalah Optimisasi")
    
    # Pilihan: contoh masalah atau input custom
    problem_option = st.selectbox(
        "Pilih jenis masalah:",
        ["Masalah Custom", "Contoh: Volume Maksimum Kotak", "Contoh: Luas Maksimum Persegi Panjang"]
    )
    
    if problem_option == "Masalah Custom":
        problem_text = st.text_area(
            "Deskripsikan masalah optimisasi Anda:",
            height=100,
            placeholder="Contoh: 'Tentukan ukuran kotak dengan volume maksimum jika panjang + lebar + tinggi = 100 cm'"
        )
    else:
        # Contoh masalah yang sudah ditentukan
        example_problems = {
            "Contoh: Volume Maksimum Kotak": "Sebuah kotak tanpa tutup dibuat dari karton berukuran 20 cm x 30 cm. Tentukan ukuran kotak untuk volume maksimum dengan memotong sudut-sudut persegi yang sama besar.",
            "Contoh: Luas Maksimum Persegi Panjang": "Tentukan ukuran persegi panjang dengan keliling 100 meter yang memiliki luas maksimum."
        }
        problem_text = example_problems[problem_option]
        st.text_area("Masalah:", value=problem_text, height=100)
    
    if st.button("🚀 Selesaikan Masalah") and problem_text:
        with st.spinner("Menyelesaikan masalah optimisasi..."):
            solution = solve_optimization_problem(problem_text)
            
            if solution:
                st.success("✅ Masalah berhasil diselesaikan!")
                
                # Tampilkan langkah-langkah penyelesaian
                st.subheader("📋 Langkah-langkah Penyelesaian")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**1. Pemodelan Matematika**")
                    st.write(f"Fungsi yang dioptimasi:")
                    st.latex(f"f(x) = {latex(solution['function'])}")
                
                with col2:
                    st.write("**2. Turunan Fungsi**")
                    st.write("Menghitung turunan pertama:")
                    st.latex(f"f'(x) = {latex(solution['derivative'])}")
                
                st.write("**3. Mencari Titik Kritis**")
                st.write("Menyelesaikan f'(x) = 0:")
                st.code(f"Titik kritis: {solution['critical_points']}")
                
                st.write("**4. Solusi**")
                st.info(f"**Hasil:** {solution['solution']}")
                
                # Plot solusi
                st.subheader("📊 Visualisasi Solusi")
                x = symbols('x')
                fig = plot_function(solution['function'], x, (-2, 10), "Fungsi Optimisasi")
                
                # Tandai titik kritis pada plot
                x_vals = np.linspace(-2, 10, 400)
                func_numpy = sp.lambdify(x, solution['function'], 'numpy')
                y_vals = func_numpy(x_vals)
                
                plt.figure(figsize=(10, 6))
                plt.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'f(x)')
                
                # Plot titik kritis
                for cp in solution['critical_points']:
                    if cp.is_real and -2 <= float(cp) <= 10:
                        cp_val = float(cp)
                        plt.plot(cp_val, func_numpy(cp_val), 'ro', markersize=8, label=f'Titik kritis: x = {cp_val:.2f}')
                
                plt.xlabel('x')
                plt.ylabel('f(x)')
                plt.title('Fungsi Optimisasi dengan Titik Kritis')
                plt.grid(True, alpha=0.3)
                plt.legend()
                st.pyplot(plt)
                
            else:
                st.error("❌ Tidak dapat menyelesaikan masalah. Periksa format input!")

# Navigasi sidebar
st.sidebar.title("🧭 Navigasi")
page = st.sidebar.radio(
    "Pilih Halaman:",
    ["Anggota Tim", "Visualisasi Fungsi", "Penyelesaian Optimisasi"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "**Aplikasi Web Matematika**\n\n"
    "Fitur:\n"
    "• Visualisasi fungsi matematika\n"
    "• Kalkulasi turunan dengan langkah-langkah\n"
    "• Penyelesaian masalah optimisasi\n"
    "• Plot interaktif"
)

# Routing halaman
if page == "Anggota Tim":
    show_team_page()
elif page == "Visualisasi Fungsi":
    show_function_page()
elif page == "Penyelesaian Optimisasi":
    show_optimization_page()