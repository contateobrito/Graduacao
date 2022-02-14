from datetime import datetime
import os
import pandas as pd

'''Alterar caminho do diretório'''
os.chdir('C:/Users/danilo.silva/Desktop/Projetos/Gorila')

'''Abrindo o arquivo xlsx'''
dataset = pd.read_excel('Data_Base/Negocios_Hubspot.xlsx')
#print(dataset)   
 
'''Excluir colunas'''
dataset = dataset.drop(['Proprietário do negócio', 'Valor', 'Data de criação',
       'Amount of clients implemented at GorilaPRO', 'Associated Contact',
       'Associated Company IDs','Associated Contact IDs'], axis=1)
colunas = dataset.columns.values
#print(colunas)

'''Criação de Dataframe Churn e Won vazio'''
df_c = dataset[dataset['Closed lost reason'].str.contains('Churn') == True]
df_w = dataset[dataset['Etapa do negócio'].str.contains('Won')]

'''Iterando os Dataframes'''
lista = []
status = 'won'
data = 7

for j in range(2):
    for i in df_w.itertuples(index=False):
        valores = []
        valores.append(i[0]) # Deal ID
        valores.append(i[1]) # Nome do negócio
        valores.append(i[5]) # FundID
        valores.append(i[data]) # Data Closed Won / Data Churn
        valores.append(status)
        lista.append(valores)

    for i in df_c.itertuples(index=False):
        valores = []
        valores.append(i[0]) # Deal ID
        valores.append(i[1]) # Nome do negócio
        valores.append(i[5]) # FundID
        valores.append(i[data]) # Data Closed Won / Data Churn
        valores.append(status)
        lista.append(valores)

    status = 'churn'
    data = 3

df_w2 = pd.DataFrame(data = lista, columns = ['Deal_ID','B2B','FundID','Data','Status'])

'''Salvar em csv'''
df_w2.to_csv('Data_Base/Historico_B2B.csv', encoding = 'utf-8', index = False)
