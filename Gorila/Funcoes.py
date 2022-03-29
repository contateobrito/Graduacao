from datetime import datetime
import os
from turtle import st
import pandas as pd

'''Alterar caminho do diretório'''
os.chdir('C:/Users/danilo.silva/Desktop/Projetos/Gorila')

'''Abrindo o arquivo xlsx'''
dataset = pd.read_excel('Data_Base/Chamados Hubspot.xlsx')

'''Colunas em lista'''
abertos = dataset.columns.to_list()
#print(abertos)

'''Agrupação dos status considerado fechado'''
closed = ['Canceled','Closed','Feedback','Improvements / New feature']

'''Agrupar por coluna(s)'''
#print(dataset.groupby('Status do tíquete').count())

'''Dicionario com quantidade por coluna'''
#print(dataset.groupby('Status do tíquete').size().to_dict())

'''Linhas e colunas'''
#print(dataset.shape)
