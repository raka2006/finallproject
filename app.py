import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
import re

# =========================================================
# BACKGROUND HITAM + PARTIKEL ANGKA & SIMBOL KALKULUS
# =========================================================
st.markdown(
    """
    <style>
    body, .stApp { background-color: #0d0d0d; color: #ffffff; overflow: hidden; }
    .particle { position: absolute; color: rgba(255,255,255,0.5); font-size: 16px; animation: float linear infinite; }
    @keyframes float { 0% { transform: translateY(100vh) translateX(0); opacity:0; } 50% { opacity:1; } 100% { transform: translateY(-10vh) translateX(100vw); opacity:0; } }
    .css-1v3fvcr { background-color: #1a1a1a !important; color: white !important; }
    .css-ffhzg2 { color: white !important; }
    </style>
    """, unsafe_allow_html=True
)

symbols = ['∫','Σ','dx','dy','Δ','∂'] + [str(i) for i in range(10)]
particles_html = ""
for i in range(200):
    sym = np.random.choice(symbols)
    top = np.random.randint(0,100)
    left = np.random.randint(0,100)
    size = np.random.randint(12,22)
    duration = np.random.randint(10,25)
    delay = np.random.randint(0,15)
    particles_html += f'<div class="particle" style="top:{top}vh; left:{left}vw; font-size:{size}px; animation-duration:{duration}s; animation-delay:{delay}s;">{sym}</div>\n'
st.markdown(particles_html, unsafe_allow_html=True)

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(page_title="Calculus & Matrix Application", layout="wide")
st.title("📘 Calculus, Matrix, 3D Curve & Story Problems Application")
st.write("Final Project Application: Derivative, Integral, Matrix, 3D Curve, and Story Problem Solving (Indonesian & English).")

# =========================================================
# MEMBERS OF THE GROUP
# =========================================================
st.header("👥 Members of the Group")
cols = st.columns(4)
with cols[0]:
    st.image("https://printed-amethyst-lljrkyuwdm-s5iecdnwun.edgeone.dev/a2464207-e6f1-4f25-9bce-1d230733b846.jpeg", caption="1. Raka Raya Pratama", width=200)
with cols[1]:
    st.image("https://bored-pink-bfe6q7k27z-opxswhtwta.edgeone.dev/a8cc0aaa-9064-4fe4-9e4a-5dfbbafa188e.jpeg", caption="2. Faqih Ahmad Hersanto", width=200)
with cols[2]:
    st.image("https://essential-coffee-ckkctskbqm-k1ufq8gqyq.edgeone.dev/5cea401c-d11b-472d-8432-99cb2bf0d364.jpeg", caption="3. Fajar Dewo Haryanto", width=200)
with cols[3]:
    st.image("https://automatic-coffee-wwi6lb8ump-4yibjm8v8m.edgeone.dev/IMG_1557.png", caption="4. Honey Gunawan", width=200)

# =========================================================
# LANGUAGE DETECTION
# =========================================================
def detect_language(text):
    indo_keywords = ["seorang","petani","pagar","luas","keliling","kandang","keuntungan","berapa","maksimum",
                     "pedagang","toko","jual","barang"]
    eng_keywords = ["farmer","fence","area","perimeter","profit","maximum","how",
                    "shop","seller","business","sell","product"]
    text = text.lower()
    if any(k in text for k in indo_keywords): return "id"
    if any(k in text for k in eng_keywords): return "en"
    return "id"

# =========================================================
# STORY PROBLEM PARSER
# =========================================================
def parse_story_problem(text):
    text_lower = text.lower()
    x = sp.Symbol("x")
    numbers = re.findall(r"\d+(?:\.\d+)?", text_lower)
    numbers = list(map(float,numbers))
    if not numbers: return None,None

    if any(k in text_lower for k in ["luas","area","persegi panjang","rectangle","kandang","pagar"]):
        P = numbers[0]
        return x*(P/2 - x), "area"
    if any(k in text_lower for k in ["volume","kubus","cube","box"]):
        return x**3, "volume"
    if any(k in text_lower for k in ["keuntungan","profit","laba","pedagang","shop","seller","toko"]):
        if len(numbers)>=2:
            price,cost=numbers[0],numbers[1]
            return (price-cost)*x, "profit"
    return None,None

# =========================================================
# MENU
menu = st.sidebar.selectbox("Select Menu", ["Derivative","Integral","Matrix","3D Curve","Story Problems"])

# =========================================================
# DERIVATIVE
if menu=="Derivative":
    st.header("🧮 Derivative (2D & 3D)")
    expr_input = st.text_input("Enter function f(x, y):","x**2 + y**2")
    x,y = sp.symbols("x y")
    if st.button("Calculate & Plot"):
        try:
            expr = sp.sympify(expr_input)
            st.success(f"∂f/∂x = {sp.diff(expr,x)}")
            st.success(f"∂f/∂y = {sp.diff(expr,y)}")
            X,Y = np.meshgrid(np.linspace(-5,5,50),np.linspace(-5,5,50))
            f = sp.lambdify((x,y),expr,"numpy"); Z=f(X,Y)
            fig = go.Figure(data=[go.Surface(x=X,y=Y,z=Z)])
            fig.update_layout(scene=dict(xaxis=dict(color='white'),yaxis=dict(color='white'),zaxis=dict(color='white')), paper_bgcolor='black')
            st.plotly_chart(fig,use_container_width=True)
        except Exception as e: st.error(e)

# =========================================================
# INTEGRAL
elif menu=="Integral":
    st.header("📐 Integral")
    expr_input = st.text_input("Enter function f(x, y):","x**2 + y**2")
    x,y = sp.symbols("x y")
    if st.button("Calculate Integral"):
        try:
            expr=sp.sympify(expr_input)
            st.success(f"∫ f dx = {sp.integrate(expr,x)}")
            st.success(f"∫ f dy = {sp.integrate(expr,y)}")
        except Exception as e: st.error(e)

# =========================================================
# MATRIX
elif menu=="Matrix":
    st.header("🔢 Matrix Operations")
    A_input = st.text_area("Matrix A (rows separated by new lines)")
    B_input = st.text_area("Matrix B (rows separated by new lines)")
    def parse_matrix(text): return np.array([[float(n) for n in row.split()] for row in text.splitlines()])
    if st.button("Calculate"):
        try:
            A=parse_matrix(A_input); B=parse_matrix(B_input)
            st.write("A + B =", A+B)
            st.write("A × B =", A@B)
            st.write("det(A) =", np.linalg.det(A))
        except Exception as e: st.error(e)

# =========================================================
# 3D CURVE
elif menu=="3D Curve":
    st.header("📊 3D Curve")
    func_input = st.text_input("z = f(x, y)","x**2 + y**2")
    x,y = sp.symbols("x y")
    if st.button("Show Curve"):
        expr=sp.sympify(func_input); f=sp.lambdify((x,y),expr,"numpy")
        X,Y=np.meshgrid(np.linspace(-5,5,50),np.linspace(-5,5,50)); Z=f(X,Y)
        fig=go.Figure(data=[go.Surface(x=X,y=Y,z=Z)])
        fig.update_layout(scene=dict(xaxis=dict(color='white'),yaxis=dict(color='white'),zaxis=dict(color='white')), paper_bgcolor='black')
        st.plotly_chart(fig,use_container_width=True)

# =========================================================
# STORY PROBLEMS FINAL + Batas x linear profit
elif menu=="Story Problems":
    st.header("📖 Story Problem Solving (Indonesian & English)")
    story = st.text_area("Enter the story problem:",
                         "Seorang pedagang menjual apel. Harga jual per apel 5 ribu rupiah, biaya per apel 2 ribu rupiah.")
    max_x = st.number_input("Masukkan jumlah maksimum barang (untuk profit linear)", min_value=1, max_value=10000, value=100, step=1)
    
    if st.button("Solve Problem"):
        lang = detect_language(story)
        expr, problem_type = parse_story_problem(story)
        x = sp.Symbol("x")
        
        if expr is None:
            numbers = re.findall(r"\d+(?:\.\d+)?", story)
            numbers = list(map(float,numbers))
            if len(numbers) >= 2:
                price, cost = numbers[0], numbers[1]
                expr = (price-cost)*x
                problem_type = "profit"
            else:
                st.error("Tidak ada angka yang bisa dipakai untuk perhitungan." if lang=="id" else
                         "No numbers detected for calculation.")
        
        derivative = sp.diff(expr, x)
        critical_points = sp.solve(derivative, x)
        
        if not critical_points:
            if problem_type=="profit":
                values = [(0, expr.subs(x,0)), (max_x, expr.subs(x,max_x))]
                optimum = max(values, key=lambda t: float(t[1]))
                st.warning("Profit linear: maksimum dihitung menggunakan x=0 dan x=max_x." if lang=="id" else
                           "Linear profit: maximum computed using x=0 and x=max_x.")
            else:
                optimum_val = expr.subs(x,1)
                optimum = [(1,optimum_val)]
        else:
            values = [(p, expr.subs(x,p)) for p in critical_points]
            optimum = max(values, key=lambda t: float(t[1]))
        
        st.latex(f"f(x) = {sp.latex(expr)}")
        if isinstance(optimum, list):
            st.success(f"Contoh optimum: x = {optimum[0][0]}, hasil = {optimum[0][1]}")
        else:
            st.success(f"Optimum: x = {optimum[0]}, hasil = {optimum[1]}")
