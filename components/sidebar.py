import streamlit as st
from pathlib import Path

# Carrega o CSS
def load_css():
    try:
        css_file = Path(__file__).parent.parent / "styles" / "sidebar.css"
        with open(css_file, encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Erro ao carregar CSS: {e}")
        # CSS fallback direto no código
        st.markdown("""
            <style>
            .sidebar .sidebar-content {
                background-color: #FFFFFF;
            }
            </style>
        """, unsafe_allow_html=True)

def show_sidebar(user_type: str):
    load_css()
    
    with st.sidebar:
        # Logo
        st.image("images/logo.png", width=150)
        st.divider()

        # Menu específico para cada tipo de usuário
        if user_type == "agente":
            # Dashboard
            if st.sidebar.button("📊 Dashboard", key="dashboard", 
                               help="Visão geral das startups"):
                st.session_state.page = "dashboard"
            
            # Monitoramento
            if st.sidebar.button("📈 Monitoramento", key="monitoring",
                               help="Acompanhamento das startups"):
                st.session_state.page = "monitoring"
            
            # Startups
            if st.sidebar.button("🚀 Startups", key="startups",
                               help="Gerenciar startups"):
                st.session_state.page = "startups"
            
            # Relatórios
            if st.sidebar.button("📑 Relatórios", key="reports",
                               help="Relatórios e análises"):
                st.session_state.page = "reports"
            
            # Recursos
            if st.sidebar.button("🗂️ Recursos", key="resources",
                               help="Materiais e recursos"):
                st.session_state.page = "resources"

        elif user_type == "empreendedor":
            # Minha Startup
            if st.sidebar.button("🏢 Minha Startup", key="my_startup",
                               help="Informações da sua startup"):
                st.session_state.page = "minha_startup"
            
            # Dashboard
            if st.sidebar.button("📊 Dashboard", key="my_dashboard",
                               help="Seu progresso"):
                st.session_state.page = "my_dashboard"
            
            # Material
            if st.sidebar.button("📚 Material", key="material",
                               help="Material de apoio"):
                st.session_state.page = "material"
            
            # Relatório
            if st.sidebar.button("📋 Relatório", key="relatorio",
                               help="Seus relatórios"):
                st.session_state.page = "relatorio"
            
            # Reunião
            if st.sidebar.button("👥 Reunião", key="reuniao",
                               help="Agendamento de reuniões"):
                st.session_state.page = "reuniao"

        st.divider()
        
        # Informações do usuário e logout
        with st.container():
            st.markdown(f"**Usuário:** {st.session_state.get('username', '')}")
            if st.button("🚪 Logout", key="logout"):
                st.session_state.clear()
                st.rerun()

def init_session_state():
    if 'page' not in st.session_state:
        st.session_state.page = "dashboard"  # página default