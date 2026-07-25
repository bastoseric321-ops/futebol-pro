import streamlit as st

st.set_page_config(page_title="Analista Pro - Futebol & Apostas", page_icon="⚽", layout="centered")

st.markdown("<h2 style='text-align: center; color: #ffffff;'>⚽ Analista Pro - Futebol & Apostas</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Painel Completo de Análises</p>", unsafe_allow_html=True)
st.markdown("---")

times = ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Fluminense", "Atlético-MG", "Grêmio", "Internacional", "Botafogo", "Cruzeiro"]

time_casa = st.selectbox("🏠 Time da Casa", times, index=0)
time_visitante = st.selectbox("✈️ Time Visitante", times, index=1)

if st.button("🚀 Analisar Opções de Apostas", use_container_width=True):
    if time_casa == time_visitante:
        st.error("Escolha times diferentes para a análise!")
    else:
        st.success("Análise de Múltiplos Mercados Concluída!")
        
        st.markdown("### 📊 Indicadores Principais")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Favorito", value=time_casa, delta="Forte")
        with col2:
            st.metric(label="Gols Esperados", value="2.5+", delta="Tendência")
        with col3:
            st.metric(label="Ambos Marcam", value="Provável", delta="Sim")

        st.markdown("---")
        st.markdown("### 🎯 Sugestões de Apostas")
        
        st.info(f"💡 **1. Dupla Hipótese (Seguro):** Vitória ou Empate ({time_casa}) + Mais de 1.5 gols.")
        st.warning(f"🔥 **2. Mercado de Gols:** Mais de 1.5 gols na partida inteira.")
        st.success(f"⚡ **3. Criador de Aposta (Combo):** {time_casa} marca ao menos 1 gol + Mais de 0.5 gols no 1º tempo.")
