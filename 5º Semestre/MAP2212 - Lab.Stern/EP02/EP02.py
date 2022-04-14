#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    #Função polinomial indicada pelo enuciado
    funcao = np.exp(-A*x)*np.cos(B*x)
    return funcao
    
def crude(Seed = None):
    np.random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo crude
    Escreva o seu codigo nas proximas linhas
    """

    anterior = erro = n = 1000
    while erro > 0.0005:

        #Criação da matriz uniforme de tamanho n com a função f(x) em cada termo
        matriz = f(np.random.uniform(0,1,n))
        #Média das variaveis observadas
        estimador = 1/n * sum(matriz)
        #A média das distancias em relação ao valor central 
        var = sum(np.square(matriz-estimador))/n 
        #Comparativo do erro padrão do estimador anterior com o atual
        erro = np.sqrt(var/n)
        #Aumento do tamanho da amostra
        n += 1000

    return estimador   

def hit_or_miss(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo hit or miss
    Escreva o seu codigo nas proximas linhas
    """
    erro = n = 10000
    while erro > 0.0005:

        #Criação dos pontos aleatórios
        matriz = np.random.rand(n,2)
        #Aplicação da função f em x
        matriz[:,0] = f(matriz[:,0])
        #Contador de tuplas que tem valor 1 na função indicadora, "y <= f(x)"
        contador = matriz[np.where(matriz[:,1] <= matriz[:,0])][:,0].size
        #Estimador que representa a area
        estimador = contador / n
        #Variancia da distrinuição binomial
        var = (estimador*(1-estimador))
        #Comparativo do erro padrão do estimador anterior com o atual
        erro = np.sqrt(var/n)
        #Aumento do tamanho da amostra
        n += 10000

    return estimador


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