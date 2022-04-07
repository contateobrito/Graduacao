#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
#Escreva seu nome e numero USP
INFO = {12345678:"Fulano Junior"}
A = 0.442705074  # A = 0.rg
B = 0.35382211892  # B = 0.cpf




def f(x):
    """
    Esta funcao deve receber x e devolver f(x), como especifcado no enunciado
    Escreva o seu codigo nas proximas linhas
    """
    
    
    
    return 





def crude(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo crude
    Escreva o seu codigo nas proximas linhas
    """



    return #Retorne sua estimativa





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