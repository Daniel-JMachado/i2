import streamlit as st
from datetime import datetime

def show():
    st.title("Recursos e Materiais")

    # Tabs para diferentes tipos de recursos
    tab1, tab2, tab3, tab4 = st.tabs([
        "📚 Materiais", 
        "📑 Templates", 
        "👥 Mentorias",
        "🔗 Links Úteis"
    ])

    with tab1:
        st.subheader("Biblioteca de Materiais")
        
        # Filtros
        col1, col2 = st.columns([2,1])
        with col1:
            search = st.text_input("🔍 Buscar material")
        with col2:
            categoria = st.selectbox(
                "Categoria",
                ["Todos", "Tecnologia", "Mercado", "Gestão", "Capital", "Empreendedor"]
            )

        # Lista de materiais
        materiais = [
            {
                "titulo": "Guia do Empreendedor Iniciante",
                "categoria": "Empreendedor",
                "tipo": "PDF",
                "data": "2024-01-15",
                "descricao": "Manual completo com dicas para novos empreendedores"
            },
            {
                "titulo": "Template de Pitch Deck",
                "categoria": "Mercado",
                "tipo": "PPT",
                "data": "2024-01-10",
                "descricao": "Modelo de apresentação para investidores"
            },
            {
                "titulo": "Planilha de Métricas",
                "categoria": "Gestão",
                "tipo": "XLS",
                "data": "2024-01-05",
                "descricao": "Planilha para acompanhamento de KPIs"
            }
        ]

        for material in materiais:
            with st.expander(f"{material['titulo']} ({material['tipo']})"):
                col1, col2 = st.columns([3,1])
                with col1:
                    st.write(f"**Categoria:** {material['categoria']}")
                    st.write(f"**Data:** {material['data']}")
                    st.write(f"**Descrição:** {material['descricao']}")
                with col2:
                    st.download_button(
                        "📥 Download",
                        data=b"exemplo",  # Aqui seria o arquivo real
                        file_name=f"{material['titulo']}.{material['tipo'].lower()}",
                        mime="application/octet-stream"
                    )

    with tab2:
        st.subheader("Templates e Documentos")
        
        # Organização por categoria
        categorias_templates = {
            "Documentação": [
                "Modelo de Contrato",
                "Termo de Confidencialidade",
                "Relatório de Progresso"
            ],
            "Apresentações": [
                "Pitch Deck",
                "Apresentação de Resultados",
                "Demo Day"
            ],
            "Planilhas": [
                "Controle Financeiro",
                "Métricas de Crescimento",
                "Plano de Ação"
            ]
        }

        for categoria, templates in categorias_templates.items():
            st.write(f"### {categoria}")
            for template in templates:
                col1, col2 = st.columns([4,1])
                with col1:
                    st.write(template)
                with col2:
                    st.button("📥", key=f"download_{template}")
            st.divider()

    with tab3:
        st.subheader("Programa de Mentorias")

        # Adicionar mentor
        with st.expander("➕ Adicionar Novo Mentor"):
            col1, col2 = st.columns(2)
            with col1:
                mentor_nome = st.text_input("Nome do Mentor")
                mentor_area = st.selectbox(
                    "Área de Expertise",
                    ["Tecnologia", "Mercado", "Gestão", "Capital", "Empreendedor"]
                )
            with col2:
                mentor_email = st.text_input("Email")
                mentor_disponibilidade = st.multiselect(
                    "Disponibilidade",
                    ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
                )
            mentor_bio = st.text_area("Biografia")
            st.button("Cadastrar Mentor")

        # Lista de mentores
        mentores = [
            {
                "nome": "João Silva",
                "area": "Tecnologia",
                "bio": "Especialista em desenvolvimento de software com 15 anos de experiência",
                "disponibilidade": "Segunda e Quarta"
            },
            {
                "nome": "Maria Santos",
                "area": "Mercado",
                "bio": "Consultora de marketing digital e especialista em growth hacking",
                "disponibilidade": "Terça e Quinta"
            }
        ]

        for mentor in mentores:
            with st.container():
                st.markdown(f"""
                    <div style='padding: 10px; border: 1px solid #ddd; border-radius: 5px; margin: 5px 0;'>
                        <h4 style='color: #4CAF50; margin: 0;'>{mentor['nome']} - {mentor['area']}</h4>
                        <p><strong>Disponibilidade:</strong> {mentor['disponibilidade']}</p>
                        <p>{mentor['bio']}</p>
                    </div>
                """, unsafe_allow_html=True)

    with tab4:
        st.subheader("Links Úteis")
        
        links = {
            "Ferramentas": [
                {"nome": "Trello - Gestão de Projetos", "url": "https://trello.com"},
                {"nome": "Notion - Documentação", "url": "https://notion.so"},
                {"nome": "Figma - Design", "url": "https://figma.com"}
            ],
            "Comunidade": [
                {"nome": "Fórum de Startups", "url": "#"},
                {"nome": "Grupo LinkedIn", "url": "#"},
                {"nome": "Canal Discord", "url": "#"}
            ],
            "Aprendizado": [
                {"nome": "Cursos Online", "url": "#"},
                {"nome": "Blog da Incubadora", "url": "#"},
                {"nome": "Eventos Tech", "url": "#"}
            ]
        }

        for categoria, lista_links in links.items():
            st.write(f"### {categoria}")
            for link in lista_links:
                st.markdown(f"- [{link['nome']}]({link['url']})")
            st.divider()

if __name__ == "__main__":
    show()