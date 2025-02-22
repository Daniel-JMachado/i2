import streamlit as st
import pandas as pd
from datetime import datetime

def show():
    st.title("Gestão de Startups")

    # Tabs principais
    tab1, tab2 = st.tabs(["📋 Lista de Startups", "➕ Nova Startup"])

    with tab1:
        # Filtros
        col1, col2, col3 = st.columns(3)
        with col1:
            search = st.text_input("🔍 Buscar startup")
        with col2:
            filter_nivel = st.selectbox(
                "Nível de Maturidade",
                ["Todos", "Pré-operação", "Operação", "Tração", "Escala"]
            )
        with col3:
            filter_status = st.selectbox(
                "Status",
                ["Todos", "Ativo", "Graduado", "Desligado"]
            )

        # Lista de startups
        startups = [
            {
                "nome": "Wonder Data Labs",
                "area": "Analytics",
                "nivel": "Operação",
                "status": "Ativo",
                "entrada": "01/2024",
                "progresso": 0.45
            },
            {
                "nome": "Tech Solutions",
                "area": "SaaS",
                "nivel": "Tração",
                "status": "Ativo",
                "entrada": "06/2023",
                "progresso": 0.75
            },
            {
                "nome": "Green Energy",
                "area": "Cleantech",
                "nivel": "Pré-operação",
                "status": "Ativo",
                "entrada": "12/2023",
                "progresso": 0.15
            }
        ]

        for startup in startups:
            with st.expander(f"🚀 {startup['nome']}"):
                col1, col2 = st.columns([3,1])
                with col1:
                    st.write(f"**Área:** {startup['area']}")
                    st.write(f"**Nível de Maturidade:** {startup['nivel']}")
                    st.write(f"**Status:** {startup['status']}")
                    st.write(f"**Data de Entrada:** {startup['entrada']}")
                    st.progress(startup['progresso'])
                with col2:
                    st.button("📊 Dashboard", key=f"dash_{startup['nome']}")
                    st.button("📝 Editar", key=f"edit_{startup['nome']}")
                    st.button("❌ Remover", key=f"del_{startup['nome']}")

    with tab2:
        # Formulário de cadastro
        with st.form("cadastro_startup"):
            st.subheader("Cadastrar Nova Startup")
            
            col1, col2 = st.columns(2)
            with col1:
                nome = st.text_input("Nome da Startup")
                site = st.text_input("Website")
                area = st.selectbox(
                    "Área de Atuação",
                    ["Analytics", "SaaS", "Fintech", "Healthtech", "Cleantech", "Outro"]
                )
            
            with col2:
                email = st.text_input("Email de Contato")
                telefone = st.text_input("Telefone")
                modelo = st.selectbox(
                    "Modelo de Negócio",
                    ["B2B", "B2C", "B2B2C", "D2C", "Marketplace"]
                )

            # Informações dos fundadores
            st.subheader("Fundadores")
            col1, col2, col3 = st.columns(3)
            with col1:
                fundador_nome = st.text_input("Nome")
            with col2:
                fundador_email = st.text_input("Email do Fundador")
            with col3:
                fundador_cargo = st.text_input("Cargo")

            # Descrição e detalhes
            st.subheader("Informações do Negócio")
            descricao = st.text_area("Descrição do Negócio")
            problema = st.text_area("Problema que Resolve")
            solucao = st.text_area("Solução Proposta")

            # Documentos
            st.subheader("Documentos")
            pitch_deck = st.file_uploader("Pitch Deck", type=["pdf", "ppt", "pptx"])
            modelo_negocios = st.file_uploader("Modelo de Negócios", type=["pdf"])
            
            # Configurações iniciais
            st.subheader("Configurações do Programa")
            col1, col2 = st.columns(2)
            with col1:
                data_inicio = st.date_input("Data de Início")
                nivel_inicial = st.selectbox(
                    "Nível de Maturidade Inicial",
                    ["Pré-operação", "Operação", "Tração", "Escala"]
                )
            with col2:
                programa = st.selectbox(
                    "Programa de Incubação",
                    ["Programa Regular", "Programa Acelerado"]
                )
                mentor = st.selectbox(
                    "Mentor Responsável",
                    ["João Silva", "Maria Santos", "Pedro Oliveira"]
                )

            # Botão de submissão
            submitted = st.form_submit_button("Cadastrar Startup")
            if submitted:
                st.success("Startup cadastrada com sucesso!")
                # Aqui entraria a lógica de salvamento no banco de dados

if __name__ == "__main__":
    show()