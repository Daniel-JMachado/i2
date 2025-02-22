def init_session_state():
    if 'page' not in st.session_state:
        if st.session_state.get('user_type') == 'empreendedor':
            st.session_state.page = "minha_startup"
        else:
            st.session_state.page = "dashboard"