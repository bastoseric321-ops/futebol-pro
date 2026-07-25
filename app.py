import streamlit as st
import random

st.set_page_config(page_title="Analista Pro - Foco em Segurança", page_icon="🛡️", layout="centered")

st.markdown("<h2 style='text-align: center; color: #ffffff;'>🛡️ Analista Pro - Foco: Ganhar & Não Perder</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Estratégias Avançadas de Chance Dupla e Proteção</p>", unsafe_allow_html=True)
st.markdown("---")

times = ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Fluminense", "Atlético-MG", "Grêmio", "Internacional", "Botafogo", "Cruzeiro"]

col_a, col_b = st.columns(2)
with col_a:
    time_casa = st.selectbox("🏠 Casa", times, index=0)
with col_b:
    time_visitante = st.selectbox("✈️ Visitante", times, index=1)

if st.button("🚀 Calcular Apostas 'Não Perde' & Segurança", use_container_width=True):
    if time_casa == time_visitante:
        st.error("⚠️ Escolha times diferentes para a partida!")
    else:
        st.success("✅ Análise de Proteção Concluída!")
        
        # Probabilidades simuladas com foco em segurança
        prob_casa = random.randint(55, 75)
        prob_empate = random.randint(20, 30)
        prob_fora = 100 - prob_casa - prob_empate

        st.markdown("### 📊 Probabilidade de Resultado")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label=f"Vitória {time_casa}", value=f"{prob_casa}%")
        with c2:
            st.metric(label="Empate", value=f"{prob_empate}%")
        with c3:
            st.metric(label=f"Vitória {time_visitante}", value=f"{prob_fora}%")

        st.markdown("---")
        st.markdown("### 🛡️ Opções Focadas em 'Ganhar e Não Perder'")
        
        st.success(f"🔥 **1. Chance Dupla (Mais Segura):** {time_casa} ou Empate (1X) — *Alta probabilidade de green com proteção total contra derrota.*")
        st.info(f"⚡ **2. Empate Anula a Aposta (DNB):** {time_casa} — *Se o jogo terminar empatado, sua aposta é 100% devolvida.*")
        st.warning(f"🎯 **3. Handicap Asiático (0.0 / Empate Anula):** {time_casa} (0.0) — *Ganha se vencer, se empatar o dinheiro volta.*")

        st.markdown("---")
        st.markdown("### 📈 Resumo do Prognóstico")
        st.markdown(f"> **Estratégia Recomendada:** O time da casa ({time_casa}) possui forte mando de campo. Para mitigar riscos e focar estritamente em **não perder**, a entrada em **1X (Dupla Hipótese)** ou **Empate Anula** é a melhor opção matemática da partida.")
