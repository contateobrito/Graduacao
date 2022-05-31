#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
import time
import math
import numpy as np
import scipy.stats as stats

#Escreva seus nomes e numeros USP
INFO = {10693250:"Danilo Brito",10801513:"William Veloso"}

#####################################################################
# vetor de observações
x = np.array([4, 6, 4])
# vetor de informação a priori
y = np.array([1, 2, 3])

params = x + y
    
# número de pontos de corte
k = 500000
# número de vetores de paramêtros
n = 3*k

def main():
    t1 = time.time()
    
    # Gerador Dirichlet para gerar n thetas com a distribuição da posteriori
    np_sample = np.random.dirichlet(params, size = n)

    #Calculando os pontos na posteriori
    z1 = np.apply_along_axis(posteriori, 1, np_sample)
    z = np.sort(z1)

    #valores de corte
    vi = cutoff(z, k)

    #definindo a função U
    def U(v):
        result = np.where(vi <= v)[0]
        soma = len(result)
        return soma/k
  
    tempoExec = time.time() - t1
    
    print("\nExemplos da função U")
    print("v = {:3.2f}, U = {:3.3f}".format(0, U(0)))
    print("v = {:3.2f}, U = {:3.3f}".format(0.5, U(0.5)))
    print("v = {:3.2f}, U = {:3.3f}".format(1, U(1)))
    print("v = {:3.2f}, U = {:3.3f}".format(15, U(15)))
    print("v = {:3.2f}, U = {:3.3f}".format(500, U(500)))
    
    #precisão 
    print("\n")
    precisao_norm(k)
    print("\n")
    precisao_t(k)
    
    print("\nTempo de execução: {:3.2f} segundos".format(tempoExec))
    
    return U
#-------------------------------------------------------------
# Função Potencial a posteriori
def posteriori(theta):
    '''Recebe os vetores x, y e theta e
    retorna o valor da função potencial a posteriori'''
    result = theta**(params-1)
    return (1/betaMult()) * np.prod(result)

def betaMult():
    num = 1
    for i in range(3):  
      termo = math.gamma(params[i])
      num *= termo

    den = math.gamma(sum(params))

    return num/den

# Região de Corte            
def cutoff(x, k):
    '''Recebe os valores da função potencial a posteriori
    e número de pontos de corte e retorna os intervalos'''
    n = len(x)
    corte = int(n/k)
    x = np.array(x).reshape((k, corte))
    vi = x[:,-1]
    return vi

def precisao_norm(k):
    valores = stats.norm.rvs(size=n)
    
    norm = stats.norm.pdf(valores)
    norm = np.sort(norm)

    vi = cutoff(norm, k)
      
    quantis = np.array([-2.241403, -1.959964, -1.644854, -1.281552]) # valores para teste com a Normal Padrão
    
    print("Cálculo da precisão usando a distribuição Normal Padrão")
    for i in range(len(quantis)):
        #calculando a estimativa do método
        result = np.where(vi <= stats.norm.pdf(quantis[i]))[0]
        estimado = len(result)/k
        #calculando o valor real e o erro relativo
        real = stats.norm.cdf(quantis[i])*2
        erro = abs(estimado - real)
      
        print("Estimativa: ", round(estimado, 6), "\tValor Real: ", round(real, 3), "\tErro Absoluto: ", round(erro, 6))

def precisao_t(k):
    valores = stats.t.rvs(df = 1, size=n)
    
    t_sample = stats.t.pdf(valores, df = 1)
    t_sample = np.sort(t_sample)
    
    vi = cutoff(t_sample, k)
    
    quantis = np.array([-25.4517, -12.7062, -6.313752, -3.077684]) # valores para teste com a T-student com 1 g.l.
    
    print("Cálculo da precisão usando a distribuição T-student com 1 g.l.")
    for i in range(len(quantis)):
        #calculando a estimativa do método
        result = np.where(vi <= stats.t.pdf(quantis[i], df=1))[0]
        estimado = len(result)/k
        #calculando o valor real e o erro relativo
        real = stats.t.cdf(quantis[i], df = 1)*2
        erro = abs(estimado - real)
          
        print("Estimativa: ", round(estimado, 6), "\tValor Real: ", round(real, 3), "\tErro Absoluto: ", round(erro, 6))  

if __name__ == '__main__':
    main()