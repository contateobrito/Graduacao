from scipy import integrate
import numpy as np
A = 0.442705074
B = 0.35382211892

#Integral
def g(x):
    return np.exp(-A*x)*np.cos(B*x)


saida = integrate.quad(g,0,1)
print(saida[0])