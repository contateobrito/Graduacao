#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time
import time
import random
from tracemalloc import start
import numpy as np
from scipy.stats import stats
from scipy import integrate

#Escreva seu nome e numero USP
INFO = {10693250:"Danilo Brito da Silva"}
A = 0.442705074  # A = 0.rg
B = 0.35382211892  # B = 0.cpf


def f(x):
    """
    Esta funcao deve receber x e devolver f(x), como especifcado no enunciado
    Escreva o seu codigo nas proximas linhas
    """
    return np.exp(-A*x)*np.cos(B*x)
    
def crude(Seed = 42):
    np.random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo crude
    Escreva o seu codigo nas proximas linhas
    """
    return #Retorne sua estimativa
#np.random.seed(4)
start = time.time()
n = 50000
erro = 1
#Criar matriz de uniforme, 0-1, de tamanho n
matriz = np.random.uniform(0,1,n)
#print(matriz)
#Aplicar a função f(x) em cada elemento da matriz
matriz_a = f(matriz)
#print(matriz_a)
#Estimador chapéu, valor médio
est = 1/n * sum(matriz_a)
print(est)
#Variancia
var = sum(np.square(matriz_a-est))/n
#print(var)


#Integral
def g(x):
    return np.exp(-A*x)*np.cos(B*x)
saida = integrate.quad(g,0,1)
print(saida[0])
erro = abs(est-saida) 
print('erro %.5f' %(erro[0]))
#print(erro)




def hit_or_miss(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo hit or miss
    Escreva o seu codigo nas proximas linhas
    """



    return #Retorne sua estimativa







def control_variate(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo control variate
    Escreva o seu codigo nas proximas linhas
    """



    return #Retorne sua estimativa








def importance_sampling(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo importance sampling
    Escreva o seu codigo nas proximas linhas
    """



    return #Retorne sua estimativa






def main():
    #Coloque seus testes aqui
    print(crude())
    print(hit_or_miss())
    print(control_variate())
    print(importance_sampling())




if __name__ == "___main__":
    main()