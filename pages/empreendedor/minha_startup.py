import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    # Estilo personalizado para páginas do empreendedor
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to bottom, #FFFFFF, #af69cd);  /* Violeta bem claro */
        }
        .metric-card {
            background-color: #F3F0FF;
            border: 1px solid #673AB7;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Minha Startup")

    # Informações básicas da startup
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Wonder Data Labs")
        st.markdown("""
        **Site:** www.wonderdatalabs.com  
        **Área de Atuação:** Analytics  
        **Modelo de Negócio:** B2B  
        **Data de Início:** 21/2024  
        """)
    
    with col2:
        st.metric("Nível de Maturidade", "Operação", "↗️ +5%")
        st.metric("Tempo no Programa", "8 meses", "16 meses restantes")

    # Progress bar do programa
    st.subheader("Progresso no Programa")
    progress = 0.45  # 45% de progresso
    st.progress(progress)
    
    # Tabs para diferentes seções
    tab1, tab2, tab3 = st.tabs(["📊 Desempenho", "📝 Checkpoints", "👥 Time"])

    with tab1:
        # Gráfico de radar das áreas de conhecimento
        st.subheader("Áreas de Conhecimento")
        areas = {
            'Área': ['Tecnologia', 'Mercado', 'Gestão', 'Capital', 'Empreendedor'],
            'Valor': [80, 65, 45, 55, 70]
        }
        df_areas = pd.DataFrame(areas)
        fig = px.line_polar(df_areas, r='Valor', theta='Área', line_close=True)
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

        # Status dos passos em cada área
        st.subheader("Status por Área")
        for area in ['Tecnologia', 'Mercado', 'Gestão', 'Capital', 'Empreendedor']:
            with st.expander(area):
                for i in range(1, 5):  # 4 passos por área
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"Passo {i}")
                    with col2:
                        status = ["Concluído", "Em andamento", "Não iniciado", "Pausado"][i-1]
                        st.write(status)

    with tab2:
        st.subheader("Próximo Checkpoint")
        with st.container():
            st.markdown("""
            📅 **Data:** 15/02/2024  
            🎯 **Objetivo:** Revisão do desenvolvimento técnico  
            📌 **Áreas:** Tecnologia, Mercado  
            """)

        st.subheader("Histórico de Checkpoints")
        checkpoints = [
            {
                "data": "10/01/2024",
                "tipo": "Regular",
                "areas": "Tecnologia, Mercado",
                "resultado": "Positivo"
            },
            {
                "data": "15/12/2023",
                "tipo": "Mentoria",
                "areas": "Gestão",
                "resultado": "Em desenvolvimento"
            }
        ]

        for checkpoint in checkpoints:
            st.markdown(f"""
                <div style='padding: 10px; border: 1px solid #673AB7; border-radius: 5px; margin: 5px 0; background-color: #F3F0FF;'>
                    <h4 style='color: #673AB7; margin: 0;'>{checkpoint['data']} - {checkpoint['tipo']}</h4>
                    <p><strong>Áreas:</strong> {checkpoint['areas']}</p>
                    <p><strong>Resultado:</strong> {checkpoint['resultado']}</p>
                </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.subheader("Equipe")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Fundador
            **Nome:** João Silva  
            **Cargo:** CEO  
            **Email:** joao@wonderdatalabs.com
            """)
        
        with col2:
            st.markdown("""
            ### Mentor
            **Nome:** Maria Santos  
            **Área:** Analytics  
            **Próxima Mentoria:** 20/02/2024
            """)

if __name__ == "__main__":
    show()