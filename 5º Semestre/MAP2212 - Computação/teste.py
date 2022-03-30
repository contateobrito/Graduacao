import random
import math
import time
import pandas as pd
import numpy as np
from scipy.stats import norm

def pi(n, Seed = None):
    random.seed(Seed)
    base = np.random.random(size=(int(n),2))

    contador = 0
    for i in base:
        distancia = math.dist((0,0),i)
        if distancia <= 1:
            contador += 1
    simulacao = base.shape[0]
    pi = (contador/simulacao)*4
    return pi

inicio = time.time()

""" Dados da Amostra """
#Tamanho da amostra
z = norm.ppf(0.99)
erro = 0.0005
amostra = (z**2 * 0.25)/erro**2

#Pi estimado
pi_est = pi(amostra)

""" Dados da Simulação """
#Pi calculado
pi_calc = pi(amostra*1.2)

""" Erro Metido """
erro = (abs(pi_est - pi_calc)/pi_est)*100

""" Tempo de Simulação """
fim = time.time()
tempo = fim-inicio

print("\nSimulações = %i \nTamanho da amostra = %i \nPi_calculado = %7.5f \nPi_estimado = %7.5f \nErro pecentual = %5.3f \nTempo de simulação = %4.2f seg.\n" % (amostra*1.2, amostra, pi_est, pi_calc, erro, tempo))




