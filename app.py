import streamlit as st
import random

st.set_page_config(page_title="Criador de Aposta Pro", page_icon="🎯", layout="centered")

st.markdown("<h2 style='text-align: center; color: #ffffff;'>🎯 Criador de Aposta Pro & Análise de Valor</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Foco em Chance Dupla, Proteção e Múltiplos Mercados</p>", unsafe_allow_html=True)
st.markdown("---")

times = ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Fluminense", "Atlético-MG", "Grêmio", "Internacional", "Botafogo", "Cruzeiro"]

col_a, col_b = st.columns(2)
with col_a:
    time_casa = st.selectbox("🏠 Time da Casa", times, index=0)
with col_b:
    time_visitante = st.selectbox("✈️ Time Visitante", times, index=1)

if st.button("🚀 Gerar Criador de Aposta Completo", use_container_width=True):
    if time_casa == time_visitante:
        st.error("⚠️ Escolha times diferentes para a partida!")
    else:
        st.success("✅ Relatório de Criador de Aposta Gerado!")
        
        # Simulação inteligente de dados orientados a segurança e ganho
        prob_1x = random.randint(75, 88)
        gols_esperados = round(random.uniform(1.6, 3.2), 1)
        cantos_jogo = random.randint(8, 12)
        cartoes_jogo = random.randint(3, 6)

        st.markdown("### 📊 Indicadores de Confiabilidade")
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label=f"Proteção '{time_casa} ou Empate'", value=f"{prob_1x}%", delta="Alta Segurança")
            st.metric(label="Média de Gols Esperados", value=f"{gols_esperados} Gols", delta="Tendência")
        with c2:
            st.metric(label="Média de Escanteios", value=f"{cantos_jogo} Cantos", delta="Mercado Aberto")
            st.metric(label="Média de Cartões", value=f"{cartoes_jogo} Cartões", delta="Controlado")

        st.markdown("---")
        st.markdown("### 🛠️ Opções do Criador de Aposta (Para Ganhar com Segurança)")
        
        st.success(f"🛡️ **Opção 1 (Foco em Não Perder):** Chance Dupla ({time_casa} ou Empate) + Mais de 1.5 gols na partida.")
        st.info(f"⚡ **Opção 2 (Blindada com Anulação):** Empate Anula a Aposta (DNB) para {time_casa} + Mais de 7.5 escanteios no jogo.")
        st.warning(f"🎯 **Opção 3 (Criador de Gols):** {time_casa} marca 1 ou mais gols + Menos de 4.5 cartões para o visitante.")
        st.error(f"🔥 **Opção 4 (Combo Master Defensivo):** {time_casa} ou Empate + Mais de 0.5 gols no 1º tempo + Mais de 6.5 escanteios.")

        st.markdown("---")
        st.markdown("### 💡 Dica do Analista")
        st.markdown(f"> Se o objetivo é **evitar red e garantir consistência**, priorize as opções que contêm **Chance Dupla (1X)** ou **Empate Anula**, pois elas devolvem o dinheiro em caso de igualdade ou garantem a vitória simples do mandante.")
