import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

def show():
    # Estilo personalizado
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to bottom, #FFFFFF, #af69cd);
        }
        .meeting-card {
            background-color: #FFFFFF;
            border: 1px solid #673AB7;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .calendar-day {
            background-color: #FFFFFF;
            border: 1px solid #673AB7;
            padding: 10px;
            border-radius: 5px;
            margin: 2px;
            text-align: center;
        }
        .calendar-day:hover {
            background-color: #F3F0FF;
        }
        .meeting-status-scheduled {
            color: #4CAF50;
            font-weight: bold;
        }
        .meeting-status-pending {
            color: #FFA726;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Reuniões e Mentorias")

    # Tabs principais
    tab1, tab2, tab3 = st.tabs(["📅 Próximas Reuniões", "➕ Agendar", "📋 Histórico"])

    with tab1:
        # Próximas reuniões
        st.subheader("Reuniões Agendadas")
        
        proximas_reunioes = [
            {
                "data": "15/02/2024",
                "hora": "14:00",
                "tipo": "Checkpoint",
                "participantes": "João Silva, Maria Santos",
                "status": "Confirmada",
                "pauta": "Revisão do desenvolvimento técnico"
            },
            {
                "data": "20/02/2024",
                "hora": "10:00",
                "tipo": "Mentoria",
                "participantes": "Pedro Oliveira",
                "status": "Aguardando confirmação",
                "pauta": "Marketing Digital"
            }
        ]

        for reuniao in proximas_reunioes:
            st.markdown(f"""
                <div class='meeting-card'>
                    <h4 style='color: #673AB7;'>{reuniao['data']} - {reuniao['hora']}</h4>
                    <p><strong>Tipo:</strong> {reuniao['tipo']}</p>
                    <p><strong>Participantes:</strong> {reuniao['participantes']}</p>
                    <p><strong>Status:</strong> 
                        <span class='meeting-status-{"scheduled" if reuniao["status"] == "Confirmada" else "pending"}'>
                            {reuniao['status']}
                        </span>
                    </p>
                    <p><strong>Pauta:</strong> {reuniao['pauta']}</p>
                </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.subheader("Agendar Nova Reunião")
        
        with st.form("agendar_reuniao"):
            col1, col2 = st.columns(2)
            
            with col1:
                data = st.date_input(
                    "Data",
                    min_value=datetime.now().date(),
                    max_value=datetime.now().date() + timedelta(days=60)
                )
                tipo_reuniao = st.selectbox(
                    "Tipo de Reunião",
                    ["Checkpoint", "Mentoria", "Apresentação", "Outro"]
                )
                participantes = st.multiselect(
                    "Participantes",
                    ["João Silva", "Maria Santos", "Pedro Oliveira", "Ana Costa"]
                )
            
            with col2:
                hora = st.time_input("Horário")
                local = st.selectbox(
                    "Local",
                    ["Online - Google Meet", "Online - Zoom", "Presencial - Sala 1", "Presencial - Sala 2"]
                )
                pauta = st.text_area("Pauta da Reunião")

            documentos = st.file_uploader("Anexar Documentos", accept_multiple_files=True)
            
            submitted = st.form_submit_button("Solicitar Agendamento")
            if submitted:
                st.success("Solicitação de agendamento enviada! Aguardando confirmação.")

    with tab3:
        st.subheader("Histórico de Reuniões")
        
        # Filtros
        col1, col2 = st.columns(2)
        with col1:
            mes = st.select_slider(
                "Período",
                options=["Janeiro", "Fevereiro", "Março", "Abril", "Maio"],
                value="Fevereiro"
            )
        with col2:
            tipo_filtro = st.multiselect(
                "Tipo",
                ["Checkpoint", "Mentoria", "Apresentação"],
                default=["Checkpoint", "Mentoria"]
            )

        # Histórico
        historico_reunioes = [
            {
                "data": "10/01/2024",
                "tipo": "Checkpoint",
                "status": "Realizada",
                "resumo": "Revisão do MVP e definição de próximos passos",
                "acoes": ["Implementar feedback dos usuários", "Preparar apresentação para investidores"]
            },
            {
                "data": "15/01/2024",
                "tipo": "Mentoria",
                "status": "Realizada",
                "resumo": "Mentoria em estratégias de marketing digital",
                "acoes": ["Criar plano de marketing", "Definir KPIs"]
            }
        ]

        for reuniao in historico_reunioes:
            with st.expander(f"{reuniao['data']} - {reuniao['tipo']}"):
                st.write(f"**Status:** {reuniao['status']}")
                st.write(f"**Resumo:** {reuniao['resumo']}")
                st.write("**Ações definidas:**")
                for acao in reuniao['acoes']:
                    st.write(f"- {acao}")
                st.download_button(
                    "📥 Download Ata",
                    data="ata_reuniao",
                    file_name=f"ata_{reuniao['data'].replace('/','')}_{reuniao['tipo']}.pdf",
                    mime="application/pdf"
                )

        # Estatísticas
        st.subheader("Estatísticas de Reuniões")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Reuniões", "15", "↗️ +3 este mês")
        with col2:
            st.metric("Taxa de Presença", "92%", "↗️ +5%")
        with col3:
            st.metric("Ações Concluídas", "28/35", "80%")

if __name__ == "__main__":
    show()