import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

def show():
    st.title("Relatório da Startup")

    # Seletor de Startup
    selected_startup = st.selectbox(
        "Selecione a Startup",
        ["Wonder Data Labs", "Startup B", "Startup C"]
    )

    # Layout em 2 colunas
    col1, col2 = st.columns([2, 1])

    with col1:
        # Informações básicas
        st.image("images/logo.png", width=100)  # Logo da startup
        
        st.markdown("""
        **Site:** www.wonderdatalabs.com  
        **Grau de Inovação:** Incremental  
        **Modelo de negócio:** B2B  
        **Área de Atuação:** Analytics  
        **Nível de Maturidade:** Operação  
        **Referência:** 21/2024  
        """)

        # Tempo de Incubação
        st.subheader("Tempo de Incubação")
        meses_incubacao = 8  # exemplo
        total_meses = 36
        progress = meses_incubacao / total_meses
        st.progress(progress)
        st.write(f"{meses_incubacao} meses de {total_meses}")

        # Parecer Técnico
        st.subheader("Parecer Técnico")
        areas = {
            "TECNOLOGIA": "A empresa está registrando 3 marcas no Brasil e tem todos seus produtos no mercado atualizado. Além disso, terá seu próprio servidor até o final de 2024.",
            "MERCADO": "A empresa está coletando indicadores de funil de vendas e mapeando os processos de atração de clientes. Além disso, está consolidando parcerias estratégicas com outras empresas.",
            "GESTÃO": "A empresa definiu sua estrutura organizacional através de um organograma além da criação da matriz de competências.",
            "CAPITAL": "Atualizando o Cap Table da empresa, juntamente com um contador nos EUA. Além disso, está desenvolvendo um BI para analisar os indicadores.",
            "EMPREENDEDOR": "Os empreendedores estão se empenhando em desenvolver o pensamento estratégico juntamente com mentorias e ampliando seu networking empresarial."
        }
        
        for area, parecer in areas.items():
            with st.expander(area):
                st.write(parecer)

    with col2:
        # Descrição
        st.subheader("Descrição")
        st.markdown("""
        Plataforma para manutenção preditiva, utilizando técnicas avançadas de confiabilidade e inteligência artificial (IA). Permite que as empresas prevejam falhas de equipamentos, otimizem os cronogramas de manutenção e minimizem o tempo de individade dispendioso.
        """)

        # Destaques
        st.subheader("Destaques")
        st.markdown("""
        Wonder Data Labs participa do EXPO MAG 2024, um espaço multinível voltado às demandas dos mais diversos setores da economia para a realização de eventos.
        """)

        # Desempenho
        st.subheader("Desempenho")
        # Gráfico de radar para áreas de conhecimento
        areas_valores = {
            'Área': ['Tecnologia', 'Mercado', 'Gestão', 'Capital', 'Empreendedor'],
            'Valor': [80, 65, 45, 55, 70]
        }
        df_areas = pd.DataFrame(areas_valores)
        fig = px.line_polar(df_areas, r='Valor', theta='Área', line_close=True)
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

        # Indicador de crescimento
        st.subheader("Indicador de crescimento")
        # Dados de exemplo para o gráfico de crescimento
        dates = ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06']
        valores = [0, 20, 35, 45, 60, 80]
        df_crescimento = pd.DataFrame({
            'Data': dates,
            'Valor': valores
        })
        fig_crescimento = px.line(df_crescimento, x='Data', y='Valor')
        st.plotly_chart(fig_crescimento, use_container_width=True)

if __name__ == "__main__":
    show()