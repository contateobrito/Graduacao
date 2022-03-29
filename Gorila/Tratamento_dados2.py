from datetime import datetime
import os
import pandas as pd

'''Alterar caminho do diretório'''
os.chdir('C:/Users/danilo.silva/Desktop/Projetos/Gorila')

'''Abrindo o arquivo xlsx'''
dataset = pd.read_excel('Data_Base/Chamados Hubspot.xlsx')

coluna = dataset.columns.to_list()
print(coluna)



#dataset = dataset.drop(['Resolução Ticket','Descrição do tíquete'],axis=1)
colunas = dataset.columns.to_list()

df = pd.DataFrame(data = dataset, columns = colunas)
df = df.drop(['Data de fechamento'], axis=1)

colunas = dataset.columns.to_list()
colunas2 = df.columns.to_list()

'''Incluir Coluna'''
df.insert(loc = len(colunas2), column = 'Condição', value = 'Churn')

df.rename(columns={'Data de criação':'Data'},inplace=True)
dataset.rename(columns={'Data de fechamento':'Data'},inplace=True) 

colunas4 = dataset.columns.to_list()
colunas5 = df.columns.to_list()


#print(colunas4)
#print(colunas5)

#df_f = pd.DataFrame(data=pd.concat([dataset, df]), columns = df.columns.to_list())

'''Salvar em csv'''
#df_f.to_csv('Data_Base/chamados2.csv', encoding = 'utf-8', index = False,sep="#")
