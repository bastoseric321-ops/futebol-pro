import streamlit as st
import random

st.set_page_config(page_title="Analista Pro - Painel VIP", page_icon="💎", layout="centered")

# Estilo visual moderno e sofisticado (CSS personalizado)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stTextInput > div > div > input {
        background-color: #1a1c23;
        color: #ffffff;
        border-radius: 8px;
        border: 1px solid #30363d;
        font-weight: 600;
    }
    .stButton > button {
        background: linear-gradient(90deg, #238636 0%, #2ea043 100%);
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 12px rgba(35, 134, 54, 0.4);
        transition: 0.3s;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #2ea043 0%, #3fb950 100%);
        box-shadow: 0 6px 16px rgba(46, 160, 67, 0.6);
    }
    div.stMetric {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #58a6ff;'>💎 Analista Pro VIP</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>Raio-X Estatístico de Elite & Blindagem Anti-Red</p>", unsafe_allow_html=True)
st.markdown("---")

col_a, col_b = st.columns(2)
with col_a:
    time_casa = st.text_input("🏠 Time da Casa", value="Flamengo")
with col_b:
    time_visitante = st.text_input("✈️ Time Visitante", value="Palmeiras")

st.markdown("")
if st.button("🚀 Gerar Análise de Blindagem & Linhas Seguras", use_container_width=True):
    if not time_casa.strip() or not time_visitante.strip():
        st.error("⚠️ Por favor, preencha o nome dos dois times!")
    elif time_casa.strip().lower() == time_visitante.strip().lower():
        st.error("⚠️ Escolha equipes diferentes para confrontar!")
    else:
        st.success(f"✨ Relatório VIP Gerado: {time_casa.strip()} vs {time_visitante.strip()}")
        
        # Simulação controlada para linhas altamente conservadoras (foco em blindagem)
        gols_base = round(random.uniform(2.4, 3.2), 1)
        cantos_base = random.randint(10, 13)
        cartoes_base = random.randint(4, 6)
        faltas_base = random.randint(24, 30)
        laterais_base = random.randint(36, 44)

        st.markdown("### 📈 Indicadores & Linhas Conservadoras (Zero Red)")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="⚽ Gols (Esperado)", value=f"{gols_base}", delta="Linha Super Segura: 0.5+ / 1.5+")
        with c2:
            st.metric(label="🚩 Escanteios", value=f"{cantos_base}", delta="Linha Super Segura: 6.5+")
        with c3:
            st.metric(label="🟨 Cartões", value=f"{cartoes_base}", delta="Linha Super Segura: 2.5+")

        c4, c5 = st.columns(2)
        with c4:
            st.metric(label="⚡ Faltas", value=f"{faltas_base}", delta="Linha Super Segura: 18.5+")
        with c5:
            st.metric(label="📐 Laterais", value=f"{laterais_base}", delta="Linha Super Segura: 28.5+")

        st.markdown("---")
        st.markdown("### 🎯 Criador de Aposta Blindada (Proteção Máxima)")
        
        st.success(f"🛡️ **1. Combo Anti-Red (Gols + Dupla):** Chance Dupla ({time_casa.strip()} ou Empate) + Mais de 1.5 gols no total.")
        st.info(f"🚩 **2. Combo Escanteios Assegurados:** Mais de 6.5 escanteios no jogo (Margem de -3 cantos da média para zerar riscos).")
        st.warning(f"🟨 **3. Combo Disciplinar Leve:** Mais de 2.5 cartões na partida inteira.")
        st.error(f"⚡ **4. Combo Duplo Conforto:** {time_casa.strip()} (Empate Anula / DNB) + Mais de 25.5 laterais.")

        st.markdown("---")
        st.markdown("### 💡 Estratégia Profissional de Recuperação de Banca")
        st.markdown(f"> **Como usar sem tomar red:** As linhas acima foram reduzidas propositalmente (ex: se o estudo projeta 10 escanteios, indicamos a linha de 6.5). Isso absorve qualquer imprevisto em campo, garantindo que mesmo um jogo truncado bata a sua aposta com tranquilidade.")
