import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

def show():
    # Título da página
    st.title("Dashboard - Visão Geral")

    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total de Startups", value="12", delta="2 novos")
    with col2:
        st.metric(label="Checkpoints Pendentes", value="5", delta="-2")
    with col3:
        st.metric(label="Reuniões esta Semana", value="8", delta="3")
    with col4:
        st.metric(label="Média de Maturidade", value="65%", delta="+5%")

    # Dividindo a tela em duas colunas
    col_left, col_right = st.columns([2, 1])

    with col_left:
        # Gráfico de distribuição por nível de maturidade
        st.subheader("Distribuição por Nível de Maturidade")
        
        # Dados de exemplo
        data = {
            'Nível': ['Pré-operação', 'Operação', 'Tração', 'Escala'],
            'Quantidade': [3, 4, 3, 2]
        }
        df = pd.DataFrame(data)
        
        fig = px.bar(df, x='Nível', y='Quantidade',
                    color='Quantidade',
                    color_continuous_scale=['#4CAF50', '#673AB7'])
        st.plotly_chart(fig, use_container_width=True)

        # Tabela de startups recentes
        st.subheader("Startups Recentes")
        startups_df = pd.DataFrame({
            'Startup': ['Startup A', 'Startup B', 'Startup C'],
            'Nível': ['Operação', 'Pré-operação', 'Tração'],
            'Última Atualização': ['2024-01-15', '2024-01-14', '2024-01-10']
        })
        st.dataframe(startups_df, use_container_width=True)

    with col_right:
        # Próximas reuniões
        st.subheader("Próximas Reuniões")
        today = datetime.now()
        meetings = [
            {"startup": "Startup A", "data": today + timedelta(days=1), "tipo": "Checkpoint"},
            {"startup": "Startup B", "data": today + timedelta(days=3), "tipo": "Mentoria"},
            {"startup": "Startup C", "data": today + timedelta(days=5), "tipo": "Avaliação"}
        ]
        
        for meeting in meetings:
            with st.container():
                st.markdown(f"""
                    <div style='padding: 10px; border: 1px solid #ddd; border-radius: 5px; margin: 5px 0;'>
                        <h4 style='color: #4CAF50; margin: 0;'>{meeting['startup']}</h4>
                        <p style='margin: 5px 0;'>{meeting['data'].strftime('%d/%m/%Y')}</p>
                        <p style='margin: 0;'>{meeting['tipo']}</p>
                    </div>
                """, unsafe_allow_html=True)

        # Alertas importantes
        st.subheader("Alertas")
        alerts = [
            {"tipo": "warning", "msg": "3 startups com checkpoint atrasado"},
            {"tipo": "info", "msg": "Novo relatório disponível"},
            {"tipo": "success", "msg": "2 startups prontas para graduação"}
        ]
        
        for alert in alerts:
            if alert["tipo"] == "warning":
                st.warning(alert["msg"])
            elif alert["tipo"] == "info":
                st.info(alert["msg"])
            elif alert["tipo"] == "success":
                st.success(alert["msg"])

if __name__ == "__main__":
    show()