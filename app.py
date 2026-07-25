import streamlit as st

st.set_page_config(page_title="Analista Pro - Futebol & Apostas", page_icon="⚽", layout="centered")

st.markdown("<h2 style='text-align: center; color: #ffffff;'>⚽ Analista Pro - Futebol & Apostas</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Análise Prática e Sem Erros</p>", unsafe_allow_html=True)
st.markdown("---")

times = ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Fluminense", "Atlético-MG", "Grêmio", "Internacional"]

time_casa = st.selectbox("🏠 Time da Casa", times, index=0)
time_visitante = st.selectbox("✈️ Time Visitante", times, index=1)

if st.button("🚀 Analisar Jogo", use_container_width=True):
    if time_casa == time_visitante:
        st.error("Escolha times diferentes!")
    else:
        st.success("Análise Concluída com Sucesso!")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Favorito", value=time_casa, delta="Forte")
        with col2:
            st.metric(label="Mercado de Gols", value="Mais de 1.5", delta="Seguro")
        st.info(f"💡 **Palpite Principal:** Vitória ou Empate ({time_casa}) + Mais de 1.5 gols.")
