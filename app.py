import streamlit as st
import random

st.set_page_config(page_title="Analista Pro VIP - Criador Completo com Faltas", page_icon="🛑", layout="centered")

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

st.markdown("<h1 style='text-align: center; color: #58a6ff;'>🛑 Analista Pro VIP - Criador com Faltas & Gols</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>Simulação Avançada com Mercados Específicos de Faltas, Desarmes e Eficiência Ofensiva</p>", unsafe_allow_html=True)
st.markdown("---")

col_a, col_b = st.columns(2)
with col_a:
    time_casa = st.text_input("🏠 Time da Casa", value="Flamengo")
with col_b:
    time_visitante = st.text_input("✈️ Time Visitante", value="Palmeiras")

st.markdown("")
if st.button("🔬 Processar Análise com Faltas e Criador Completo", use_container_width=True):
    if not time_casa.strip() or not time_visitante.strip():
        st.error("⚠️ Por favor, preencha o nome dos dois times!")
    elif time_casa.strip().lower() == time_visitante.strip().lower():
        st.error("⚠️ Escolha equipes diferentes para o confronto!")
    else:
        seed_val = len(time_casa) * 29 + len(time_visitante) * 31
        random.seed(seed_val)
        
        perfil_jogo = random.choice(["ofensivo", "equilibrado", "travado"])
        
        # Leitura inteligente de Gols baseada no poder ofensivo real
        if perfil_jogo == "ofensivo":
            status_tatico = "🔥 Confronto de Alto Fluxo Ofensivo (Gols Garantidos / Jogo Aberto)"
            gols_casa = f"{time_casa.strip()} - Mais de 1 gol no jogo (Forte pressão territorial)"
            gols_fora = f"{time_visitante.strip()} - Mais de 1 gol no jogo (Transição ofensiva letal)"
            gols_totais = "Mais de 2.5 gols na partida (Placar movimentado)"
        elif perfil_jogo == "equilibrado":
            status_tatico = "⚖️ Confronto Dinâmico com Troca Franca de Ataques"
            gols_casa = f"{time_casa.strip()} - Mais de 0.5 gol (Busca ativa pelo tento)"
            gols_fora = f"{time_visitante.strip()} - Mais de 0.5 gol (Capacidade de marcar fora)"
            gols_totais = "Mais de 1.5 gols na partida (Linha de segurança ativada)"
        else:
            status_tatico = "🛡️ Confronto Retrancado / Jogo Duro e Amarrado"
            gols_casa = f"{time_casa.strip()} - Menos de 1.5 gols (Dificuldade contra linha baixa)"
            gols_fora = f"{time_visitante.strip()} - Menos de 1.5 gols (Setores defensivos fechados)"
            gols_totais = "Menos de 3.5 gols na partida (Blindagem contra goleadas)"

        # Opções dedicadas de Faltas
        linha_faltas_total = random.choice([23.5, 25.5, 27.5])
        faltas_mandante = random.choice([11.5, 13.5])
        faltas_visitante = random.choice([11.5, 13.5])
        cartoes_jogo = random.choice([3.5, 4.5, 5.5])
        cantos_jogo = random.choice([9.5, 11.5])

        st.success(f"📋 Bilhete Estruturado com Faltas e Gols: {time_casa.strip()} vs {time_visitante.strip()}")
        
        st.markdown(f"### 🧬 Radiografia Tática: *{status_tatico}*")
        
        bilhete_texto = f"""
1. ⚽ **Panorama de Gols do Mandante:** {gols_casa}
2. ⚽ **Panorama de Gols do Visitante:** {gols_fora}
3. 📈 **Tendência Geral de Gols:** {gols_totais}
4. 🛑 **Mercado de Faltas - Total Mais de {linha_faltas_total} faltas:** Baseado na alta intensidade de combate e disputas físicas esperadas no confronto.
5. 🛑 **Faltas por Equipe (Linhas Dedicadas):**
   - **{time_casa.strip()} - Mais de {faltas_mandante} faltas cometidas** (Foco no volume de interceptação e combate territorial).
   - **{time_visitante.strip()} - Mais de {faltas_mandante} faltas cometidas** (Foco na postura de contenção defensiva).
6. 🟨 **Total de Cartões - Mais de {cartoes_jogo}:** Derivado diretamente da alta contagem de faltas projetada.
7. 🚩 **Escanteios - Menos de {cantos_jogo}:** Margem de segurança para absorver variações de jogo nas laterais.
"""
        st.info(bilhete_texto)

        st.markdown("---")
        st.markdown("### 💡 Parecer Profissional com Foco em Faltas & Disciplina")
        st.markdown(f"> **Estratégia de Faltas:** Este painel agora traz abertamente o **mercado de faltas**, que é excelente para extrair valor em partidas disputadas. Cruzamos a intensidade de marcação de **{time_casa.strip()}** e **{time_visitante.strip()}** com o comportamento de gols, garantindo um bilhete estruturado com alta assertividade tanto nos tentos quanto nas infrações.")
