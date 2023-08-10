import streamlit as st
from datapov.calendar import calendario

filter_options = ['Nenhum', 'Status', 'Forma de ingresso']
status_options = ['Nenhum', 'Inscrições Encerradas', 'Inscrições Abertas', 'Inscrições Fechadas']
form_options = ['Nenhum', 'Vestibular', 'Nota ENEM', 'Vestibular/ Nota ENEM']
filter_selected, status_selected, form_selected = '', '', ''

st.title('Calendário Apoio Singular')
st.write('----------')
st.write('#### Filtros')

filter_selected = st.selectbox('Filtrar por:', options=filter_options)

if filter_selected != 'Nenhum': 
    calendario = calendario
    if filter_selected == 'Status':
        status_selected = st.selectbox('Selecione o filtro desejado', options=status_options)
        match status_selected:
            case 'Inscrições Encerradas':
                calendario = calendario[calendario['Status'] == 'Inscrições Encerradas']
            case 'Inscrições Abertas':
                calendario = calendario[calendario['Status'] == 'Inscrições Abertas']
            case 'Inscrições Fechadas':
                calendario = calendario[calendario['Status'] == 'Inscrições Fechadas']
    elif filter_selected == 'Forma de ingresso':
        form_selected = st.selectbox('Selecione o filtro desejado', options=form_options)
        match form_selected:
            case 'Vestibular':
                calendario = calendario[calendario['Forma de ingresso'] == 'Vestibular']
            case 'Nota ENEM':
                calendario = calendario[calendario['Forma de ingresso'] == 'Nota ENEM']
            case 'Vestibular/ Nota ENEM':
                calendario = calendario[calendario['Forma de ingresso'] == 'Vestibular/ Nota ENEM']

calend = st.dataframe(calendario)
