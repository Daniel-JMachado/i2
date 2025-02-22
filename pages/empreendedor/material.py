import streamlit as st
from datetime import datetime

def show():
    # Estilo personalizado
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to bottom, #FFFFFF, #af69cd);
        }
        .material-card {
            background-color: #FFFFFF;
            border: 1px solid #673AB7;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .tag {
            background-color: #673AB7;
            color: white;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 12px;
            margin-right: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Materiais de Apoio")

    # Barra de pesquisa e filtros
    col1, col2 = st.columns([3,1])
    with col1:
        search = st.text_input("🔍 Buscar material")
    with col2:
        categoria = st.selectbox(
            "Categoria",
            ["Todos", "Tecnologia", "Mercado", "Gestão", "Capital", "Empreendedor"]
        )

    # Tabs principais
    tab1, tab2, tab3, tab4 = st.tabs([
        "📚 Biblioteca", 
        "📝 Templates", 
        "🎥 Vídeos",
        "🔗 Links Úteis"
    ])

    with tab1:
        st.subheader("Biblioteca de Materiais")
        
        materiais = [
            {
                "titulo": "Guia de Desenvolvimento MVP",
                "categoria": "Tecnologia",
                "tipo": "PDF",
                "data": "2024-01-15",
                "tags": ["MVP", "Desenvolvimento", "Produto"],
                "descricao": "Guia completo sobre como desenvolver um MVP eficiente"
            },
            {
                "titulo": "Planilha de Métricas de Marketing",
                "categoria": "Mercado",
                "tipo": "XLS",
                "data": "2024-01-10",
                "tags": ["Marketing", "Métricas", "Analytics"],
                "descricao": "Template para acompanhamento de métricas de marketing"
            },
            {
                "titulo": "Manual de Pitch para Investidores",
                "categoria": "Capital",
                "tipo": "PDF",
                "data": "2024-01-05",
                "tags": ["Pitch", "Investimento", "Apresentação"],
                "descricao": "Dicas e técnicas para criar um pitch efetivo"
            }
        ]

        for material in materiais:
            st.markdown(f"""
                <div class='material-card'>
                    <h4 style='color: #673AB7;'>{material['titulo']}</h4>
                    <p>
                        {''.join([f"<span class='tag'>{tag}</span>" for tag in material['tags']])}
                    </p>
                    <p><strong>Categoria:</strong> {material['categoria']}</p>
                    <p><strong>Tipo:</strong> {material['tipo']}</p>
                    <p><strong>Data:</strong> {material['data']}</p>
                    <p>{material['descricao']}</p>
                </div>
            """, unsafe_allow_html=True)
            col1, col2 = st.columns([6,1])
            with col2:
                st.download_button(
                    "📥 Download",
                    data=b"exemplo",
                    file_name=f"{material['titulo']}.{material['tipo'].lower()}",
                    mime="application/octet-stream"
                )

    with tab2:
        st.subheader("Templates e Modelos")
        
        templates = {
            "Documentação": [
                "Template de Pitch Deck",
                "Modelo de Plano de Negócios",
                "Canvas de Modelo de Negócios"
            ],
            "Planilhas": [
                "Controle Financeiro",
                "Métricas de Crescimento",
                "Plano de Ação"
            ],
            "Apresentações": [
                "Apresentação para Investidores",
                "Demo Day",
                "Reunião de Checkpoint"
            ]
        }

        for categoria, items in templates.items():
            st.markdown(f"### {categoria}")
            for item in items:
                col1, col2 = st.columns([6,1])
                with col1:
                    st.write(item)
                with col2:
                    st.download_button(
                        "📥",
                        data=b"exemplo",
                        file_name=f"{item}.pdf",
                        key=f"download_{item}"
                    )
            st.divider()

    with tab3:
        st.subheader("Vídeos e Treinamentos")
        
        videos = [
            {
                "titulo": "Como Validar seu MVP",
                "duracao": "45min",
                "instrutor": "João Silva",
                "nivel": "Iniciante",
                "url": "https://exemplo.com/video1"
            },
            {
                "titulo": "Estratégias de Growth Hacking",
                "duracao": "60min",
                "instrutor": "Maria Santos",
                "nivel": "Intermediário",
                "url": "https://exemplo.com/video2"
            }
        ]

        for video in videos:
            st.markdown(f"""
                <div class='material-card'>
                    <h4 style='color: #673AB7;'>{video['titulo']}</h4>
                    <p><strong>Duração:</strong> {video['duracao']}</p>
                    <p><strong>Instrutor:</strong> {video['instrutor']}</p>
                    <p><strong>Nível:</strong> {video['nivel']}</p>
                    <a href='{video['url']}' target='_blank'>Assistir vídeo</a>
                </div>
            """, unsafe_allow_html=True)

    with tab4:
        st.subheader("Links Úteis")
        
        links = {
            "Ferramentas": [
                {"nome": "Trello - Gestão de Projetos", "url": "https://trello.com"},
                {"nome": "Figma - Design", "url": "https://figma.com"},
                {"nome": "GitHub - Desenvolvimento", "url": "https://github.com"}
            ],
            "Comunidade": [
                {"nome": "Comunidade INCIT", "url": "#"},
                {"nome": "Fórum de Startups", "url": "#"},
                {"nome": "Grupo LinkedIn", "url": "#"}
            ],
            "Recursos": [
                {"nome": "Blog da INCIT", "url": "#"},
                {"nome": "Newsletter de Inovação", "url": "#"},
                {"nome": "Calendário de Eventos", "url": "#"}
            ]
        }

        for categoria, lista_links in links.items():
            st.markdown(f"### {categoria}")
            for link in lista_links:
                st.markdown(f"- [{link['nome']}]({link['url']})")
            st.divider()

        # Sugestão de material
        st.subheader("Sugerir Material")
        with st.form("sugerir_material"):
            titulo = st.text_input("Título do Material")
            descricao = st.text_area("Descrição")
            categoria_sugestao = st.selectbox(
                "Categoria",
                ["Tecnologia", "Mercado", "Gestão", "Capital", "Empreendedor"]
            )
            tipo_material = st.selectbox(
                "Tipo de Material",
                ["Documento", "Vídeo", "Template", "Link", "Outro"]
            )
            url = st.text_input("URL (se aplicável)")
            comentarios = st.text_area("Comentários Adicionais")
            
            submitted = st.form_submit_button("Enviar Sugestão")
            if submitted:
                st.success("Sugestão enviada com sucesso! Nossa equipe irá avaliar.")

if __name__ == "__main__":
    show()