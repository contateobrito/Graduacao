#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np
from scipy.stats import norm

#Escreva seu nome e numero USP
INFO = {10693250:"Danilo Brito da Silva"}

def estima_pi(Seed = None):

    np.random.seed(Seed)
    #random.random() gera um numero com distribuicao uniforme em (0,1)
    """
    Esta funcao deve retornar a sua estimativa para o valor de PI
    Escreva o seu codigo nas proximas linhas
    """

    """ Tamanho da Amostra """
    #Tamanho da amostra
    z = norm.ppf(0.975)
    erro = 0.0005
    n = (z**2 * 0.25)/erro**2

    """ Criação da Matriz """
    matriz = np.random.rand(int(n),2)
    #print(matriz)

    """ Dados da Simulação """
    contador = 0
    for i in matriz:
        distancia = math.dist((0,0),i)
        if distancia <= 1:
            contador += 1
    pi = (contador/matriz.shape[0])*4

    return pi
