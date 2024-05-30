import streamlit as st
import math
import pandas as pd

#Diferença de Reforma - Manutenção - Retrofit
st.title(":orange[Você quer Reformar, Retrofit ou Manutenção?]\n")
st.markdown('Veja aqui!')
#Glossário
st.sidebar.title(
    "Glossário\n"
)
g=st.sidebar.selectbox(
    "Selecione",
    ["", "Anomalia", "Componente", "Conformidade", "Dano", "Deterioração", "Degradação", "Elemento"]
)
if g == "Anomalia":
    st.sidebar.text_area("Irregularidade, anormalidade, exceção à regra.(ABNT NBR 13752).\n")
if g == "Componente":
    st.sidebar.text_area("Unidade integrante de determinado sistema da edificação, com forma definida e destinada a atender funções específicas (por exemplo, bloco de alvenaria, telha, folha de porta). (ABNT NBR 15575-1).\n")
if g == "Conformidade":
    st.sidebar.text_area("Atendimento a requisitos e padrões estabelecidos em projetos, memoriais descritivos, normas técnicas, legislações específicas, manuais técnicos e outros documentos desenvolvidos por fabricantes e prestadores de serviço, boletins técnicos de produtos e procedimentos,dados de fabricantes de produtos / sistemas / equipamentos / máquinas, contratos e material promocional.")
if g == "Dano":
    st.sidebar.text_area("Prejuízo causado a outrem pela ocorrência de vícios, defeitos, sinistros e delitos, entre outros (Glossário IBAPE/SP).")
if g == "Deterioração":
    st.sidebar.text_area("Depreciação de um bem devido ao desgaste de seus componentes ou falhas de funcionamento de sistemas, em razão de uso ou manutenção inadequado. (ABNT NBR 13752).")
if g == "Degradação":
    st.sidebar.text_area("Redução de desempenho devido à atuação de um ou vários agentes de degradação. (ABNT NBR 15575-1)")
if g == "Elemento":
    st.sidebar.text_area("Parte de um sistema com funções específicas. Geralmente é composto por um conjunto de componentes (por exemplo, parede de vedação de alvenaria, painel de vedação pré-fabricado, estrutura de cobertura). (ABNT NBR 15575-1). ")
#introdução de variáveis
name = st.text_input("Nome: \n")
site = st.text_input("Imóvel ou cômodo: \n")
area = st.number_input("Metragem em m²: \n", min_value=10)

#Formulário
st.write("Marque as opções que lhe convém")
s1 = st.checkbox("Alteração do ambiente funcional\n")
s2 = st.checkbox("Recuperação de elementos degradados\n")
s3 = st.checkbox("Renovação e/ou atualização do ambiente\n")
s4 = st.checkbox("Vistoria e avaliação do imóvel\n")
#Resultados
if s1 == True:
    st.write(":blue[Reforma Predial]")
    st.write("Alteração nas condições de edificação existentes com ou sem mudança de função, visando recuperar, melhorar ou ampliar suas condições de habitabilidade, uso ou segurança e que não seja manutenção. (ABNT NBR 16280 Reforma em Edificações)")
    while s1 == True:
        st.write("Faça um orçamento para", area, "m² de seu imóvel")
        st.divider()
        p = st.number_input("Especifique o número de paredes de seu imóvel\n", min_value=1)
        while p > 1:
            a = st.number_input("Especifique a altura da parede em m \n", min_value=1.0)
            st.markdown("Altura mínima: 1,0 metro")
            b = st.number_input("Especifique a largura da parede em m \n", min_value=0.20)
            st.markdown("Largura mínima: 20 cm")
            area_a = round((a*b)*p, 2)
            st.write("área da parede: ", area_a)
            unit = 10.00
            #Armazenamento de dados
            results = pd.DataFrame()
            #loop dos resultados
            for k in range(1, p+1):
                if k == p:
                    #Area inicial igual a area do imovel
                    area_imov = area
                    #numero de paredes
                    num_pare= p
                    #area calculada
                    area_calc = area_a
                    #preço unitario
                    preco_unit = unit
                    #Total
                    preco_total = preco_unit*area_calc
                    #Inserção de Dados
                    results.loc[k, 'Área do Imóvel'] = area_imov
                    results.loc[k, 'Quantidade de Paredes'] = num_pare
                    results.loc[k, 'Área Calculada'] = area_calc
                    results.loc[k, 'Preço Unitário'] = preco_unit
                    results.loc[k, 'Total'] = preco_total
            results.index.name = 'Parede'       
            st.write(results)

        break
        
if s2 == True:
    st.write(":red[Manutenção]")
    st.write("Conjunto de atividades a serem realizadas para conservar ou recuperar a capacidade funcional da edificação e de suas partes constituintes de atender as necessidades e segurança dos usuários. (ABNT NBR 5674:1999-3.5)")
if s3 == True:
    st.write(":green[Retrofit]")
    st.write(" Remodelação ou atualização do edifício ou de sistemas, através da incorporação de novas tecnologias e conceitos, normalmente visando valorização do imóvel, mudança de uso, aumento da vida útil, eficiência operacional e energética. (ABNT NBR 15575-1)")
if s4 == True:
    st.write("***Agende uma vistoria***\n")
    st.write("Contatos")

st.text_input("Observações", max_chars=1000)