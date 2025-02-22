
import sys
sys.dont_write_bytecode = True
import streamlit as st
from utils.auth import check_authentication
from pages.agente.dashboard import show as show_agent_dashboard
from pages.empreendedor.minha_startup import show as show_entrepreneur_dashboard
from components.sidebar import show_sidebar, init_session_state
from pages.agente.monitoring import show as show_monitoring 
from pages.agente.reports import show as show_reports
from pages.agente.resources import show as show_resources
from pages.agente.startups import show as show_startups
from pages.empreendedor.minha_startup import show as show_minha_startup
from pages.empreendedor.my_dashboard import show as show_my_dashboard
from pages.empreendedor.material import show as show_material
from pages.empreendedor.relatorio import show as show_relatorio
from pages.empreendedor.reuniao import show as show_reuniao


# Configuração inicial da página
st.set_page_config(
    page_title="Sistema de Incubação",
    page_icon="./images/logo2.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Função para aplicar CSS customizado
def load_css():
    st.markdown("""
        <style>
        /* CSS para customizar a página de login */
        .stApp {
            background: linear-gradient(to bottom, #FFFFFF,  #2E7D32);
        }
        .stButton>button {
            background-color: #2E7D32;
            color: white;
            border-radius: 20px;
            padding: 10px 25px;
            border: none;
            width: 100%;
        }
        
        .stButton>button:hover {
            background-color: #1B5E20;
        }
        </style>
    """, unsafe_allow_html=True)

def login_page():
    if 'login_status' not in st.session_state:
        st.session_state['login_status'] = False
        st.session_state['user_type'] = None

    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.image("images/logo.png", width=500)
        
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("Agente", use_container_width=True):
                if username and password:
                    if check_authentication(username, password, "agente"):
                        st.session_state['login_status'] = True
                        st.session_state['user_type'] = 'agente'
                        st.session_state['username'] = username
                        st.rerun()
                    else:
                        st.error("Credenciais inválidas")
                else:
                    st.error("Por favor, preencha todos os campos")

        with col_btn2:
            if st.button("Empreendedor", use_container_width=True):
                if username and password:
                    if check_authentication(username, password, "empreendedor"):
                        st.session_state['login_status'] = True
                        st.session_state['user_type'] = 'empreendedor'
                        st.session_state['username'] = username
                        st.session_state.page = "minha_startup"
                        st.rerun()
                    else:
                        st.error("Credenciais inválidas")
                else:
                    st.error("Por favor, preencha todos os campos")
        
        st.markdown("<div style='text-align: center'><a href='#'>Esqueci minha senha</a></div>", 
                   unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center'>
            <a href='#'>Contato</a> | 
            <a href='#'>Suporte</a> | 
            <a href='#'>FAQs</a>
        </div>
        """, unsafe_allow_html=True)

def main():
    load_css()
    init_session_state()
    
    if st.session_state.get('login_status', False):
        # Mostrar sidebar apenas após o login
        show_sidebar(st.session_state['user_type'])
        
        # Roteamento para as páginas corretas
        if st.session_state['user_type'] == 'agente':
            if st.session_state.page == "dashboard":
                show_agent_dashboard()
            elif st.session_state.page == "monitoring":  # Adicionar este caso
                from pages.agente.monitoring import show
                show()
            elif st.session_state.page == "reports":
                from pages.agente.reports import show
                show()
            elif st.session_state.page == "resources":
                from pages.agente.resources import show
                show()
            elif st.session_state.page == "startups":
                from pages.agente.startups import show
                show()
            # Adicionar outros casos conforme necessário
            
        elif st.session_state['user_type'] == 'empreendedor':
            if st.session_state.page == "minha_startup":
                show_minha_startup()
            elif st.session_state.page == "my_dashboard":
                show_my_dashboard()
            elif st.session_state.page == "material":
                show_material() 
            elif st.session_state.page == "relatorio":
                show_relatorio()
            elif st.session_state.page == "reuniao":
                show_reuniao()
            # Adicionar outros casos conforme necessário
    else:
        login_page()

#sumir com deploy nativo do streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()