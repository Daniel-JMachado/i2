import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

def show():
    # Estilo personalizado
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to bottom, #FFFFFF, #af69cd);
        }
        .report-card {
            background-color: #FFFFFF;
            border: 1px solid #673AB7;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .status-badge {
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 14px;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Relatórios")

    # Filtros
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        periodo = st.selectbox(
            "Período",
            ["Último mês", "Últimos 3 meses", "Últimos 6 meses", "Todo o período"]
        )
    with col2:
        area = st.selectbox(
            "Área",
            ["Todas", "Tecnologia", "Mercado", "Gestão", "Capital", "Empreendedor"]
        )
    with col3:
        tipo = st.selectbox(
            "Tipo",
            ["Todos", "Checkpoint", "Mentoria", "Avaliação"]
        )

    # Tabs principais
    tab1, tab2, tab3 = st.tabs(["📊 Progresso", "📝 Avaliações", "📈 Métricas"])

    with tab1:
        # Gráfico de evolução geral
        st.subheader("Evolução Geral")
        
        # Dados simulados
        dates = ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05']
        progress = [45, 48, 52, 55, 60]
        df = pd.DataFrame({
            'Mês': dates,
            'Progresso (%)': progress
        })
        fig = px.line(df, x='Mês', y='Progresso (%)', markers=True)
        st.plotly_chart(fig, use_container_width=True)

        # Radar chart das áreas
        st.subheader("Desempenho por Área")
        areas_valores = {
            'Área': ['Tecnologia', 'Mercado', 'Gestão', 'Capital', 'Empreendedor'],
            'Atual': [65, 45, 30, 25, 40],
            'Anterior': [55, 40, 25, 20, 35]
        }
        df_areas = pd.DataFrame(areas_valores)
        fig_radar = px.line_polar(df_areas, r='Atual', theta='Área', line_close=True)
        fig_radar.add_trace(px.line_polar(df_areas, r='Anterior', theta='Área').data[0])
        st.plotly_chart(fig_radar, use_container_width=True)

    with tab2:
        st.subheader("Últimas Avaliações")
        
        avaliacoes = [
            {
                "data": "15/01/2024",
                "tipo": "Checkpoint",
                "status": "Concluído",
                "areas": "Tecnologia, Mercado",
                "feedback": "Bom progresso no desenvolvimento do MVP. Necessidade de melhorar aspectos de validação com clientes.",
                "pontos_fortes": ["MVP desenvolvido", "Equipe técnica formada"],
                "pontos_melhoria": ["Validação com clientes", "Definição de métricas"]
            },
            {
                "data": "01/01/2024",
                "tipo": "Mentoria",
                "status": "Concluído",
                "areas": "Gestão",
                "feedback": "Estruturação do processo de gestão em andamento. Necessário definir KPIs principais.",
                "pontos_fortes": ["Organização interna", "Documentação"],
                "pontos_melhoria": ["Definição de KPIs", "Processo de decisão"]
            }
        ]

        for av in avaliacoes:
            st.markdown(f"""
                <div class='report-card'>
                    <h4 style='color: #673AB7;'>{av['data']} - {av['tipo']}</h4>
                    <p><strong>Áreas:</strong> {av['areas']}</p>
                    <p><strong>Feedback:</strong> {av['feedback']}</p>
                    <div style='margin: 10px 0;'>
                        <p><strong>Pontos Fortes:</strong></p>
                        <ul>{''.join([f"<li>{ponto}</li>" for ponto in av['pontos_fortes']])}</ul>
                        <p><strong>Pontos de Melhoria:</strong></p>
                        <ul>{''.join([f"<li>{ponto}</li>" for ponto in av['pontos_melhoria']])}</ul>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.subheader("Métricas Principais")
        
        # KPIs
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Taxa de Progresso", "15% / mês", "↗️ +2%")
            st.metric("Checkpoints Concluídos", "8/10", "80%")
            st.metric("Mentorias Realizadas", "12", "↗️ +3")
        with col2:
            st.metric("Tempo no Programa", "8 meses", "16 restantes")
            st.metric("Metas Atingidas", "15/20", "75%")
            st.metric("Nível de Engajamento", "92%", "↗️ +5%")

        # Timeline de marcos
        st.subheader("Timeline de Marcos")
        marcos = [
            {"data": "12/2023", "evento": "Início do Programa"},
            {"data": "01/2024", "evento": "MVP Desenvolvido"},
            {"data": "02/2024", "evento": "Primeira Venda"},
            {"data": "03/2024", "evento": "Expansão da Equipe"}
        ]

        for marco in marcos:
            st.markdown(f"""
                <div style='padding: 10px; border-left: 3px solid #673AB7; margin: 5px 0;'>
                    <strong>{marco['data']}</strong><br>
                    {marco['evento']}
                </div>
            """, unsafe_allow_html=True)

        # Botão de download do relatório completo
        st.download_button(
            label="📥 Download Relatório Completo",
            data="dados_do_relatorio",
            file_name=f"relatorio_startup_{datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    show()