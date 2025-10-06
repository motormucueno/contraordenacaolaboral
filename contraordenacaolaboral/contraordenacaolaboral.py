import streamlit as st
from contraordenacaolaboral.decreto import contra_ordenacao_leves, contra_ordenacao_graves, contra_ordenacao_muito_graves

st.subheader("Pesquisa de Contra-Ordenações Laborais\nDecreto 50/25 de 19 de Fevereiro")
contraordenacao_input = st.text_input(label="Digite aqui:")
if st.button(label="Pesquisar", use_container_width=True):
    lista_contra_ordenacao_leves = []
    lista_contra_ordenacao_graves = []
    lista_contra_ordenacao_muito_graves = []
    if len(contraordenacao_input)>0:
        for ordenacao in contra_ordenacao_leves:
            if contraordenacao_input.lower() in ordenacao.lower():
                    lista_contra_ordenacao_leves.append(ordenacao)
        if len(lista_contra_ordenacao_leves) > 0:
            with st.container(border=True):
                if len(lista_contra_ordenacao_leves) == 1:
                    st.markdown("**Contra-Ordenação Leve (Artigo 8º)**")
                else:
                    st.markdown("**Contra-Ordenações Leve (Artigo 8º)**")
                for ordenacao in lista_contra_ordenacao_leves:
                    ordenacao_negritado = ordenacao.lower().replace(contraordenacao_input.lower(), f"**{contraordenacao_input.lower()}**")
                    st.write(f"{ordenacao_negritado};")
        for ordenacao in contra_ordenacao_graves:
            if contraordenacao_input.lower() in ordenacao.lower():
                lista_contra_ordenacao_graves.append(ordenacao)
        if len(lista_contra_ordenacao_graves) > 0:
            with st.container(border=True):
                if len(lista_contra_ordenacao_graves) == 1:
                    st.markdown("**Contra-Ordenação Grave (Artigo 9º)**")
                else:
                    st.markdown("**Contra-Ordenações Graves (Artigo 9º)**")
                for ordenacao in lista_contra_ordenacao_graves:
                    ordenacao_negritado = ordenacao.lower().replace(contraordenacao_input.lower(), f"**{contraordenacao_input.lower()}**")
                    st.write(f"{ordenacao_negritado};")
        for ordenacao in contra_ordenacao_muito_graves:
            if contraordenacao_input.lower() in ordenacao.lower():
                    lista_contra_ordenacao_muito_graves.append(ordenacao)
        if len(lista_contra_ordenacao_muito_graves) > 0:
            with st.container(border=True):
                if len(lista_contra_ordenacao_muito_graves) == 1:
                    st.markdown("**Contra-Ordenação Muito Grave (Artigo 9º)**")
                else:
                    st.markdown("**Contra-Ordenações Muito Graves (Artigo 9º)**")
                for ordenacao in lista_contra_ordenacao_muito_graves:
                    ordenacao_negritado = ordenacao.lower().replace(contraordenacao_input.lower(), f"**{contraordenacao_input.lower()}**")
                    st.write(f"{ordenacao_negritado};")
    else:
        with st.container(border=True):
            st.markdown("**Contra-Ordenações Leves (Artigo 8º)**")
            for ordenacao in contra_ordenacao_leves:
                st.write(f"{ordenacao};")
        with st.container(border=True):
            st.markdown("**Contra-Ordenações Graves (Artigo 9º)**")
            for ordenacao in contra_ordenacao_graves:
                st.write(f"{ordenacao};")
        with st.container(border=True):
            st.markdown("**Contra-Ordenações Muito Graves (Artigo 9º)**")
            for ordenacao in contra_ordenacao_muito_graves:
                st.write(f"{ordenacao};")
    if len(contraordenacao_input)>0:
        if len(lista_contra_ordenacao_leves)==0:
            if len(lista_contra_ordenacao_graves)==0:
                if len(lista_contra_ordenacao_muito_graves)==0:
                    st.info("Resultado não encontrado!")
















