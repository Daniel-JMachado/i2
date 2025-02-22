import streamlit as st
import pandas as pd
from datetime import datetime

def show():
    st.title("Monitoramento de Startups")

    # Seleção da Startup
    startups = ["Startup A", "Startup B", "Startup C", "Startup D"]
    selected_startup = st.selectbox("Selecione a Startup", startups)

    # Tabs principais
    tab1, tab2 = st.tabs(["📊 Visão Geral", "📝 Checkpoints"])

    with tab1:
        # Informações gerais da startup
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Nível de Maturidade", "Operação", "↗️ 25%")
        with col2:
            st.metric("Tempo no Programa", "8 meses", "16 meses restantes")
        with col3:
            st.metric("Próximo Checkpoint", "15 dias", "📅 10/02/2024")

        # Áreas de Conhecimento
        st.subheader("Áreas de Conhecimento")
        areas = {
            "Tecnologia": 65,
            "Mercado": 45,
            "Gestão": 30,
            "Capital": 25,
            "Perfil Empreendedor": 40
        }
        
        for area, valor in areas.items():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.progress(valor/100)
            with col2:
                st.write(f"{valor}%")

        # Status dos 20 passos
        st.subheader("Status dos Passos")
        
        # Criando dados de exemplo para os passos
        passos_df = pd.DataFrame({
            'Área': ['Tecnologia'] * 4 + ['Mercado'] * 4 + ['Gestão'] * 4 + 
                   ['Capital'] * 4 + ['Perfil Empreendedor'] * 4,
            'Passo': range(1, 21),
            'Status': ['Concluído', 'Em andamento', 'Não iniciado', 'Pausado'] * 5
        })

        # Estilizando o status com cores
        def color_status(val):
            if val == 'Concluído':
                return 'background-color: #4CAF50; color: white'
            elif val == 'Em andamento':
                return 'background-color: #FFA726; color: white'
            elif val == 'Pausado':
                return 'background-color: #F44336; color: white'
            return 'background-color: #757575; color: white'

        st.dataframe(
            passos_df.style.applymap(color_status, subset=['Status']),
            use_container_width=True
        )

    with tab2:
        # Registro de Checkpoints
        st.subheader("Registro de Checkpoints")
        
        # Formulário para novo checkpoint
        with st.expander("📝 Novo Checkpoint"):
            checkpoint_form = st.form("novo_checkpoint")
            data = checkpoint_form.date_input("Data", datetime.now())
            tipo = checkpoint_form.selectbox(
                "Tipo de Reunião",
                ["Checkpoint Regular", "Mentoria", "Avaliação Especial"]
            )
            notas = checkpoint_form.text_area("Observações")
            areas_avaliadas = checkpoint_form.multiselect(
                "Áreas Avaliadas",
                ["Tecnologia", "Mercado", "Gestão", "Capital", "Perfil Empreendedor"]
            )
            submitted = checkpoint_form.form_submit_button("Registrar Checkpoint")
            
            if submitted:
                st.success("Checkpoint registrado com sucesso!")

        # Histórico de Checkpoints
        st.subheader("Histórico de Checkpoints")
        checkpoints = [
            {
                "Data": "2024-01-15",
                "Tipo": "Checkpoint Regular",
                "Observações": "Startup apresentou avanços significativos na área de mercado",
                "Áreas": "Mercado, Gestão"
            },
            {
                "Data": "2023-12-10",
                "Tipo": "Mentoria",
                "Observações": "Necessidade de melhorar aspectos técnicos",
                "Áreas": "Tecnologia"
            },
            {
                "Data": "2023-11-05",
                "Tipo": "Checkpoint Regular",
                "Observações": "Revisão geral do progresso",
                "Áreas": "Todas"
            }
        ]

        for checkpoint in checkpoints:
            with st.container():
                st.markdown(f"""
                    <div style='padding: 10px; border: 1px solid #ddd; border-radius: 5px; margin: 5px 0;'>
                        <h4 style='color: #4CAF50; margin: 0;'>{checkpoint['Data']} - {checkpoint['Tipo']}</h4>
                        <p style='margin: 5px 0;'><strong>Áreas:</strong> {checkpoint['Áreas']}</p>
                        <p style='margin: 0;'>{checkpoint['Observações']}</p>
                    </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()