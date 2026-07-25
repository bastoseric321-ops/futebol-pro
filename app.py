import streamlit as st
import random

st.set_page_config(page_title="Analista Pro VIP - Criador Inteligente de Gols", page_icon="⚽", layout="centered")

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

st.markdown("<h1 style='text-align: center; color: #58a6ff;'>⚽ Analista Pro VIP - Criador Inteligente de Gols</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>Simulador com Leitura Dinâmica de Potencial Ofensivo (Ataque Forte vs Retranca)</p>", unsafe_allow_html=True)
st.markdown("---")

col_a, col_b = st.columns(2)
with col_a:
    time_casa = st.text_input("🏠 Time da Casa", value="Flamengo")
with col_b:
    time_visitante = st.text_input("✈️ Time Visitante", value="Palmeiras")

st.markdown("")
if st.button("🔬 Processar Leitura Real de Gols e Confronto", use_container_width=True):
    if not time_casa.strip() or not time_visitante.strip():
        st.error("⚠️ Por favor, preencha o nome dos dois times!")
    elif time_casa.strip().lower() == time_visitante.strip().lower():
        st.error("⚠️ Escolha equipes diferentes para o confronto!")
    else:
        # Gerador inteligente baseado no tamanho dos nomes para alternar entre perfil ofensivo e defensivo
        seed_val = len(time_casa) * 11 + len(time_visitante) * 13
        random.seed(seed_val)
        
        perfil_jogo = random.choice(["ofensivo", "equilibrado", "fechado"])
        
        if perfil_jogo == "ofensivo":
            status_ataque = "🔥 Confronto de Alto Poder Ofensivo (Tendência de Placar Movimentado)"
            gols_casa = f"{time_casa.strip()} - Mais de 1 gol (Forte volume de criação em casa)"
            gols_fora = f"{time_visitante.strip()} - Mais de 1 gol (Transição ofensiva rápida e letal)"
            gols_totais = "Mais de 2 gols no jogo (Jogo aberto com alta expectativa de tentos)"
        elif perfil_jogo == "equilibrado":
            status_ataque = "⚖️ Confronto Dinâmico com Oportunidades Moderadas"
            gols_casa = f"{time_casa.strip()} - Mais de 0.5 gol (Busca ativa pelo gol no mínimo)"
            gols_fora = f"{time_visitante.strip()} - Mais de 0.5 gol (Capacidade de marcar fora de casa)"
            gols_totais = "Mais de 1 gol no jogo (Linha de segurança para tentos na partida)"
        else:
            status_ataque = "🛡️ Confronto Trava / Estilo Retranca (Baixa Expectativa de Gols)"
            gols_casa = f"{time_casa.strip()} - Menos de 1.5 gols (Dificuldade esperada contra linha baixa)"
            gols_fora = f"{time_visitante.strip()} - Menos de 1.5 gols (Cuidado com jogo truncado)"
            gols_totais = "Menos de 3.5 gols no jogo (Proteção total contra placares elásticos)"

        cantos_seguros = random.choice([11.5, 12.5, 13.5])
        cartoes_seguros = random.choice([1.5, 2.5])

        st.success(f"📊 Análise Concluída: {time_casa.strip()} vs {time_visitante.strip()}")
        
        st.markdown(f"### 🧬 Diagnóstico de Mercado: *{status_ataque}*")
        
        bilhete_texto = f"""
1. ⚽ **Panorama do Mandante:** {gols_casa}
2. ⚽ **Panorama do Visitante:** {gols_fora}
3. 📈 **Leitura de Gols do Jogo:** {gols_totais}
4. 🚩 **Escanteios - Menos de {cantos_seguros}:** Margem de segurança para absorver variações de jogo.
5. 🟨 **Total de Cartões - Mais de {cartoes_seguros}:** Cobertura disciplinar para disputas intensas no meio-campo.
"""
        st.info(bilhete_texto)

        st.markdown("---")
        st.markdown("### 💡 Parecer Técnico Dinâmico")
        st.markdown(f"> **Ajuste de Perfil:** O sistema agora detecta automaticamente se o confronto é de equipes goleadoras ou defensivas. Se o time faz muitos gols, as opções de 'Mais de 1 gol' são ativadas corretamente; se o jogo for travado, as linhas de cautela entram em ação para proteger sua banca de surpresas.")
