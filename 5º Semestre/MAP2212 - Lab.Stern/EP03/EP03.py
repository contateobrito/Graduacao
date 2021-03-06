#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import numpy as np
from scipy.stats import beta
from scipy.stats import qmc

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

    erro = n = 10000
    while erro > 0.0005:

        #Criação da matriz uniforme de tamanho n com a função f(x) em cada termo
        matriz = f(qmc.Halton(d=1, scramble = False).random(n)) 
        #Média das variaveis observadas
        estimador = np.mean(matriz)
        #A média das distancias em relação ao valor central 
        var = np.var(matriz)
        #Erro padrão do estimador
        erro = np.sqrt(var/n)
        #Incremento do tamanho da amostra
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
        matriz = qmc.Halton(d=2, scramble = False).random(n)
        #Aplicação da função f em x
        matriz[:,0] = f(matriz[:,0])
        #Contador de tuplas que tem valor 1 na função indicadora, "y <= f(x)"
        contador = matriz[np.where(matriz[:,1] <= matriz[:,0])][:,0].size
        #Estimador que representa a area
        estimador = contador / n
        #Variancia da distribuição binomial
        var = (estimador*(1-estimador))
        #Erro padrão do estimador
        erro = np.sqrt(var/n)
        #Incremento do tamanho da amostra
        n += 1000

    return estimador

def control_variate(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo control variate
    Escreva o seu codigo nas proximas linhas
    """

    erro = n = 10000

    while erro > 0.0005:

        #Gerador de variavel aleatória
        va = qmc.Halton(d=n, scramble = True).random(1)
        #Criação de um vetor com va uniforme de tamanho n com a função f(x) em cada termo
        vetor_x = f(va)
        #Criação de um vetor com va uniforme de tamanho n com a função g(x) = 1 - 0.4x em cada termo
        vetor_g = va[np.where(1 - va * 0.4)]  
        #Estimador do vetor g, média dos pontos observados
        estimador_g = np.mean(vetor_g)
        #Estimador final, média dos pontos observados
        estimador_final = np.mean(vetor_x - vetor_g + estimador_g)
        #Variancia do vetor de distribuição f(x) 
        var_x, var_g = np.var(vetor_x), np.var(vetor_g)
        #Covariancia dos vetores de distribuições f(x) e g(x)
        cov = np.cov(vetor_x, vetor_g)[0][1]
        #Variancia final
        var_final = np.sqrt(abs(var_g + var_x - 2 * cov)/n)
        #Erro padrão do estimador
        erro = np.sqrt(var_final/n)
        #Incremento no tamanho da amostra
        n += 1000

    return estimador_final

def importance_sampling(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo importance sampling
    Escreva o seu codigo nas proximas linhas
    """

    a, b  = 1, 2
    ant = erro = n = 10000
    
    while erro > 0.0005:

        #Criação de um vetor com va uniforme de tamanho n com a função f(x) em cada termo
        vetor_x = f(qmc.Halton(d=1, scramble = False).random(n)) 
        #Criação de um vetor com distribuição beta de tamanho n
        vetor_g = beta.pdf(np.random.beta(a, b, n) ,a ,b)
        #Estimador, média dos pontos observados
        matriz_estimador = np.divide(vetor_x, vetor_g)
        estimador = np.mean(matriz_estimador)
        #Variancia
        var = np.var(matriz_estimador)
        #Erro padrão do estimador
        erro = abs(ant - estimador) / ant
        #erro = np.sqrt(var/n)
        ant = estimador
        #Incremedo no tamanho da amostra
        n += 1000

    return estimador

def main():
    inicio = time.time()
    print("\nBem-vido!\nAnalise dos métodos de Monte Carlo para estimar a integração.\nPara início das simulações foi utilizado n inicial igual a 10.000 com incrementos de 1.000.\n")
    
    dic = {"Crude":crude(),"Hit or Miss": hit_or_miss(), "Control Variate":control_variate(),"Importance Sampling":importance_sampling()}
    print(dic)
    """
    for i in sorted(dic, key = dic.get):
        print("- %s com n = %d, estimador %.5f e erro = %.5f" % (i, dic[i][0], dic[i][1], dic[i][2]))
    fim = time.time() - inicio
    print("\nTempo gasto na simulação: %.2fseg.\n" % (fim))
    """
if __name__ == "__main__":
    main()
