
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

dataset = pd.read_csv('dadosRH_modificado.csv')
dataset.head()
dataset.shape

'''Qual a correlação entre os atributos dos funcinários?
corr = dataset.corr()
sns.heatmap(corr, cmap = "YlOrRd", linewidths = 0.1)
plt.show()
'''

'''Qual o tempo de serviço da maioria dos funcionários?
sns.displot(dataset['tempo_servico'],color = 'green')
plt.title('Distribuição do tempo de serviço dos funcionários', fontsize = 15)
plt.xlabel('Tempo de serviço em anos', fontsize = 15)
plt.ylabel('Total')
plt.show()
'''

'''Qual avaliação do ano anterior foi mais comum?
dataset['aval_ano_anterior'].value_counts().sort_values().plot.bar(color = 'blue', figsize=(10,5))
plt.title('Distribuição da Avaliação do Ano Anterior dos funcionários',fontsize = 15)
plt.xlabel('Avalizações', fontsize = 15)
plt.ylabel('Total')
plt.show()
'''
'''Qual a distribuição das idades dos funcinários?
sns.displot(dataset['idade'],color = 'magenta')
plt.title('Distribuição da idade dos funcionários', fontsize = 15)
plt.xlabel('Idade', fontsize = 15)
plt.ylabel('Total')
plt.show()
'''

'''Qual o número de treinamentos mais frequente?
sns.violinplot(dataset['numero_treinamentos'], color = 'red')
plt.title('Número de treinamentos feitos pelos funcionários', fontsize = 15)
plt.xlabel('Número de treinamento', fontsize = 15)
plt.ylabel('Frequência')
plt.show()
'''
'''Qual a proporção dos funcionários por canal de recrutamento?
a = dataset['canal_recrutamento'].value_counts()
fatias = [a[0], a[1], a[2]]
labels = 'Outro', 'Outsourcing','Indicação'
colors = ['purple', 'lime', 'yellow']
explode = [0,0,0]
plt.pie(fatias, labels = labels, colors = colors, explode = explode, shadow=True, autopct='%.2f%%')
plt.title('Percuentual de funcionários por canal de recrutamento', fontsize=15)
plt.axis('off')
#plt.legend()
plt.show()
'''

'''Qual a relação entre a promoação e a avaiação do ano anterior?'''
data = pd.crosstab(dataset['aval_ano_anterior'], dataset['promovido'])
data.div(data.sum(1).astype(float), axis = 0).plot(kind = 'bar', stacked = True, figsize = (16,9), color = ['blue', 'magenta'])
plt.title('Relação entre avaliação do ano anterior e a promocao', fontsize = 15)
plt.xlabel('avaliação do ano anterior', fontsize = 15)
plt.legend()
plt.show()