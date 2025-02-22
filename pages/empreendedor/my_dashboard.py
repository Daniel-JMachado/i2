import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

def show():
    # Estilo personalizado para páginas do empreendedor
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to bottom, #FFFFFF, #af69cd);
        }
        .metric-card {
            background-color: #FFFFFF;
            border: 1px solid #673AB7;
            padding: 15px;
            border-radius: 10px;
            margin: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Dashboard da Startup")

    # Métricas principais em cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric("Nível de Maturidade", "45%", "↗️ +5%")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric("Checkpoints Realizados", "8", "→ 2 pendentes")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric("Mentorias", "12", "↗️ +3 este mês")
        st.markdown("</div>", unsafe_allow_html=True)

    # Dividindo a tela em duas colunas
    col_left, col_right = st.columns([2, 1])

    with col_left:
        # Gráfico de evolução
        st.subheader("Evolução da Maturidade")
        # Dados simulados para o gráfico
        dates = ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06']
        valores = [20, 25, 35, 38, 42, 45]
        df_evolucao = pd.DataFrame({
            'Data': dates,
            'Maturidade (%)': valores
        })
        fig = px.line(df_evolucao, x='Data', y='Maturidade (%)',
                     title='Evolução da Maturidade')
        st.plotly_chart(fig, use_container_width=True)

        # Progresso nas áreas de conhecimento
        st.subheader("Progresso por Área")
        areas = {
            'Tecnologia': 65,
            'Mercado': 45,
            'Gestão': 30,
            'Capital': 25,
            'Empreendedor': 40
        }
        
        for area, valor in areas.items():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.progress(valor/100)
            with col2:
                st.write(f"{valor}%")

    with col_right:
        # Próximos eventos
        st.subheader("Próximos Eventos")
        eventos = [
            {
                "tipo": "🎯 Checkpoint",
                "data": "15/02/2024",
                "desc": "Revisão técnica"
            },
            {
                "tipo": "👥 Mentoria",
                "data": "20/02/2024",
                "desc": "Marketing Digital"
            },
            {
                "tipo": "📊 Apresentação",
                "data": "01/03/2024",
                "desc": "Demo Day"
            }
        ]

        for evento in eventos:
            st.markdown(f"""
                <div style='padding: 10px; background-color: #FFFFFF; 
                     border: 1px solid #673AB7; border-radius: 5px; margin: 5px 0;'>
                    <h4 style='color: #673AB7; margin: 0;'>{evento['tipo']}</h4>
                    <p style='margin: 5px 0;'><strong>{evento['data']}</strong></p>
                    <p style='margin: 0;'>{evento['desc']}</p>
                </div>
            """, unsafe_allow_html=True)

        # Alertas e lembretes
        st.subheader("Alertas")
        st.info("📝 Relatório mensal pendente")
        st.warning("⚠️ Checkpoint em 3 dias")
        st.success("✅ Mentoria agendada")

        # Meta mais próxima
        st.subheader("Próxima Meta")
        st.markdown("""
            <div style='padding: 15px; background-color: #FFFFFF; 
                 border: 2px solid #673AB7; border-radius: 10px; margin: 10px 0;'>
                <h4 style='color: #673AB7; margin: 0;'>Meta: Validação de Mercado</h4>
                <p>Prazo: 28/02/2024</p>
                <div style='background-color: #F3F0FF; padding: 5px; border-radius: 5px;'>
                    <p>✓ Pesquisa de mercado</p>
                    <p>✓ Entrevistas com clientes</p>
                    <p>□ Análise de competidores</p>
                    <p>□ Definição de preço</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()