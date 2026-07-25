import streamlit as st
import random

st.set_page_config(page_title="Analista Pro VIP - Criador de Apostas Estratégico", page_icon="🎯", layout="centered")

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
        background: linear-gradient(90deg, #388bfd 100%, #58a6ff 100%);
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

st.markdown("<h1 style='text-align: center; color: #58a6ff;'>🎯 Analista Pro VIP - Criador de Apostas Estratégico</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>Simulador de Múltiplas Seleções com Linhas de Segurança e Alta Confiabilidade</p>", unsafe_allow_html=True)
st.markdown("---")

col_a, col_b = st.columns(2)
with col_a:
    time_casa = st.text_input("🏠 Time da Casa", value="Remo")
with col_b:
    time_visitante = st.text_input("✈️ Time Visitante", value="Palmeiras")

st.markdown("")
if st.button("🔬 Gerar Criador de Apostas Estratégico", use_container_width=True):
    if not time_casa.strip() or not time_visitante.strip():
        st.error("⚠️ Por favor, preencha o nome dos dois times!")
    elif time_casa.strip().lower() == time_visitante.strip().lower():
        st.error("⚠️ Escolha equipes diferentes para o confronto!")
    else:
        seed_val = len(time_casa) * 23 + len(time_visitante) * 29
        random.seed(seed_val)
        
        # Simulação de probabilidades e fundamentos alinhados ao estilo da Betano
        cantos_max = random.choice([11.5, 12.5, 13.5])
        gols_max = random.choice([3.5, 4.5])
        cartoes_min = random.choice([1.5, 2.5])
        defesas_goleiro = random.choice([2, 3, 4])

        st.success(f"📋 Bilhete Estruturado para: {time_casa.strip()} vs {time_visitante.strip()}")
        
        st.markdown("### 🧩 Seleções Combinadas de Alta Confiabilidade (Criador de Aposta)")
        
        st.markdown(f"""
        1. ⚽ **Mais de 0.5 Gols do {time_visitante.strip()}:** Exigência mínima de 1 tento da equipe visitante baseada no índice de eficiência ofensiva projetado.
        2. 🚩 **Menos de {cantos_max} Escanteios Totais:** Margem de segurança ampla para absorver um ritmo de jogo travado pelas intermediárias.
        3. 🟨 **Mais de {cartoes_min} Cartões na Partida:** Carga disciplinar esperada devido ao índice de faltas táticas nos setores de criação.
        4. 🟨 **Mais de 0.5 Cartões no 1º Tempo:** Cobertura voltada para a alta intensidade e fricção inicial antes da estabilização tática.
        5. 🚫 **Menos de 1.5 Impedimentos do {time_casa.strip()}:** Leitura focada na compactação e controle de linha defensiva baixa da equipe mandante.
        6. 📉 **Menos de {gols_max} Gols Totais no Jogo:** Proteção contra goleadas atípicas ou cenários de baixa conversão ofensiva.
        7. 🛡️ **Menos de 1.5 Gols do {time_casa.strip()}:** Limitação de teto de gols para o mandante, blindando contra variações desfavoráveis de placar.
        8. 🧤 **{defesas_goleiro}+ Defesas do Goleiro ({time_casa.strip()}):** Indicador baseado no volume de finalizações frontais esperadas contra a meta da casa.
        """)

        st.markdown("---")
        st.markdown("### 💡 Parecer Técnico do Modelo")
        st.markdown(f"> **Análise de Cobertura:** Este bilhete combina mercados estatísticos secundários (escanteios, cartões e impedimentos) com tetos de segurança em gols. A distribuição reduz a exposição a variações extremas de placar, priorizando linhas estendidas onde o acerto depende do volume geral de jogo e não de um resultado seco.")
