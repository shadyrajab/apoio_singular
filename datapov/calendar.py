import pandas as pd

'''Transformando a base de dados em um dataframe'''
calendario = pd.read_excel('calendario.xlsx').set_index('Processo Seletivo')

'''Formatando as datas do calendário'''
calendario['Fim'] = calendario['Fim'].dt.strftime('%d/%m/%Y')
calendario['Início'] = calendario['Início'].dt.strftime('%d/%m/%Y')
calendario['Data Final de Pagamento'] = calendario['Data Final de Pagamento'].dt.strftime('%d/%m/%Y')
calendario['Data da prova fase 1'] = calendario['Data da prova fase 1'].dt.strftime('%d/%m/%Y')
calendario['Data da prova fase 2'] = calendario['Data da prova fase 2'].dt.strftime('%d/%m/%Y')
calendario['Data da prova discursiva'] = calendario['Data da prova discursiva'].dt.strftime('%d/%m/%Y')
calendario['Edital'] = calendario['Edital'].dt.strftime('%d/%m/%Y')
calendario['Resultado'] = calendario['Resultado'].dt.strftime('%d/%m/%Y')
calendario['Divulgação gabarito'] = calendario['Divulgação gabarito'].dt.strftime('%d/%m/%Y')

'''Preenchendo os valores nulos como Não informado'''
calendario = calendario.fillna('Não informado')

