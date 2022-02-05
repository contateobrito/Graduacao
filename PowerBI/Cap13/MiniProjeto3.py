'''
Qual a correlação entre os atributos dos funcinários?
Qual o tempo de serviço da maioria dos funcionários?
Qual avaliação do ano anterior foi mais comum?
Qual a distribuição das idades dos funcinários?
Qual o número de treinamentos mais frequente?
Qual a proporção dos funcionários por canal de recrutamento?
Qual a relação entre a promoação e a avaiação do ano anterior?
'''

'''Imports'''
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

'''Chamando o arquivo com pandas'''
dadosRH = pd.read_csv('dadosRH.csv')

'''Mostrar as 5 primeiras linhas'''
#print(dadosRH.head())
'''Quantidade de linha e colunas'''
#print(dadosRH.shape)
'''Somar quantas informações em branco cada coluna tem'''
#print(dadosRH.isnull().sum())
'''Dados agrupados por coluna '''
#print(dadosRH.groupby(['educacao']).count())
#print(dadosRH.groupby(['aval_ano_anterior']).count())

'''Criação de gráfico da coluna educação'''
#sns.countplot(dadosRH['educacao'])
#plt.show()

#sns.countplot(dadosRH['aval_ano_anterior'])
#plt.show()

'''Preencher os espaços ausentes '''
#usando a moda
#print(dadosRH['educacao'].fillna(dadosRH['educacao'].mode()[0], inplace = True))
#usando a mediana
#print(dadosRH['aval_ano_anterior'].fillna(dadosRH['aval_ano_anterior'].median(), inplace = True))
#print(dadosRH.isnull().sum())

'''Criação de gráfico da coluna promovido'''
#print(dadosRH.groupby(['promovido']).count())
#sns.countplot(dadosRH['promovido'])
#plt.show()

'''Desbalanceamento de classe'''
#criando exemplos da classe minoritária
df_classe_maj = dadosRH[dadosRH.promovido==0]
df_classe_min = dadosRH[dadosRH.promovido==1]
(df_classe_maj.shape)
(df_classe_min.shape)

from sklearn.utils import resample
df_classe_min_upsampled = resample(df_classe_min, replace = True, n_samples = 50140, random_state = 150)

dadosRH_balanceados = pd.concat([df_classe_maj, df_classe_min_upsampled])
(dadosRH_balanceados)
(dadosRH_balanceados.promovido.value_counts())
sns.countplot(dadosRH_balanceados['promovido'])
plt.show()

'''Salvar em csv'''
dadosRH_balanceados.to_csv('dadosRH_modificado.csv', encoding = 'utf-8', index = False)


