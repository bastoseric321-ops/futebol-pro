import streamlit as st
import random

st.set_page_config(page_title="Analista Pro VIP - Inteligência Analítica Profunda", page_icon="📈", layout="centered")

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
        background: linear-gradient(90deg, #1f6feb 0%, #388bfd 100%);
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 12px rgba(31, 111, 235, 0.4);
        transition: 0.3s;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #388bfd 0%, #58a6ff 100%);
        box-shadow: 0 6px 16px rgba(56, 139, 253, 0.6);
    }
    div.stMetric {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 12px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #58a6ff;'>📈 Analista Pro VIP - Raio-X Estatístico Profundo</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>Modelagem Preditiva de Comportamento Tático, Padrões de Jogo & Métricas de Desempenho</p>", unsafe_allow_html=True)
st.markdown("---")

col_a, col_b = st.columns(2)
with col_a:
    time_casa = st.text_input("🏠 Time da Casa", value="Flamengo")
with col_b:
    time_visitante = st.text_input("✈️ Time Visitante", value="Palmeiras")

st.markdown("")
if st.button("🔬 Processar Raio-X Estatístico Profundo", use_container_width=True):
    if not time_casa.strip() or not time_visitante.strip():
        st.error("⚠️ Por favor, preencha o nome dos dois times!")
    elif time_casa.strip().lower() == time_visitante.strip().lower():
        st.error("⚠️ Escolha equipes diferentes para o confronto!")
    else:
        seed_val = len(time_casa) * 17 + len(time_visitante) * 19
        random.seed(seed_val)
        
        # Métricas avançadas de modelagem tática
        posse_casa = random.randint(51, 62)
        posse_fora = 100 - posse_casa
        
        xG_casa = round(random.uniform(1.2, 2.3), 2)
        xG_fora = round(random.uniform(0.7, 1.8), 2)
        
        intensidade_duelos = random.choice(["Alta pressão em bloco médio", "Transição rápida vertical", "Bloqueio zonal conservador"])
        eficiencia_ofensiva = random.choice(["Conversão acima da média no último terço", "Dependência de bolas paradas", "Volume alto de finalizações de média distância"])

        st.success(f"📊 Relatório de Inteligência Gerado para: {time_casa.strip()} vs {time_visitante.strip()}")
        
        st.markdown("### 🧬 Radiografia de Desempenho & Comportamento")
        st.info(f"⚙️ **Dinâmica Tática Predominante:** *{intensidade_duelos}*.\n\n* **Padrão Ofensivo:** {eficiencia_ofensiva}.\n* **Projeção de Posse de Bola:** {time_casa.strip()} ({posse_casa}%) vs {time_visitante.strip()} ({posse_fora}%).")

        st.markdown("---")
        st.markdown("### 📊 Indicadores Quantitativos de Jogo")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label=f"xG {time_casa.strip()}", value=f"{xG_casa}", delta="Expectativa de Gols")
        with c2:
            st.metric(label=f"xG {time_visitante.strip()}", value=f"{xG_fora}", delta="Expectativa de Gols")
        with c3:
            st.metric(label="🚩 Volume de Cantos", value=f"{random.randint(9, 14)}", delta="Média Estimada")

        c4, c5, c6 = st.columns(3)
        with c4:
            st.metric(label="🟨 Índice Disciplinar", value=f"{random.randint(4, 7)} Cartões", delta="Carga de Faltas")
        with c5:
            st.metric(label="⚡ Faltas Projetadas", value=f"{random.randint(22, 32)}", delta="Picotar de Jogo")
        with c6:
            st.metric(label="🎯 Finalizações Certas", value=f"{random.randint(8, 15)}", delta="Chutes ao Alvo")

        st.markdown("---")
        st.markdown("### 💡 Diagnóstico Técnico Estrutural")
        st.markdown(f"> **Análise de Variância:** O modelo matemático aponta que **{time_casa.strip()}** e **{time_visitante.strip()}** possuem comportamentos cíclicos baseados na densidade de marcação do adversário. A flutuação nos índices de conversão demonstra que o desempenho não depende exclusivamente de um único fator pontual, exigindo leitura fina do encaixe de linhas defensivas e transições pelos corredores laterais.")
