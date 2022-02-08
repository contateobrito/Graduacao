import os
import pandas as pd

'''Alterar caminho do diretório'''
os.chdir('C:/Users/danilo.silva/Desktop/Projetos/Gorila')

'''Abrindo o arquivo csv'''
dataset = pd.read_csv('Patrimonios/b2b_patrimonios.2022.01.31.csv')
print(type(dataset))
print(dataset)
