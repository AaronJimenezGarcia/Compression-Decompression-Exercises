# -*- coding: utf-8 -*-
"""
Aarón Jiménez García
"""
import math
import numpy as np
import matplotlib.pyplot as plt


'''
Dada una lista p, decidir si es una distribución de probabilidad (ddp)
0<=p[i]<=1, sum(p[i])=1.
'''
def es_ddp(p,tolerancia=10**(-5)):
    total = 0
    for i in p:
        if i <= 1 and i >= 0:
            total = total + i
        else:
            return False
    if total >= 1 - tolerancia and total <= 1 + tolerancia:
        return True
    else:
        return False


'''
Dado un código C y una ddp p, hallar la longitud media del código.
'''

def LongitudMedia(C,p):
    longitud = 0
    for i in range(len(p)):
        longitud = longitud + p[i]*len(C[i])
    return longitud
    
'''
Dada una ddp p, hallar su entropía.
'''

def H1(p):
    total = 0
    for i in p:
        if i != 0:
            total = total + i*math.log(1/i, 2)
    return total
        

'''
Dada una lista de frecuencias n, hallar su entropía.
'''

def H2(n):
    sumaFrecuencias = sum(n)
    probabilidades = []
    for i in n:
        probabilidades.append(i/sumaFrecuencias)
    return H1(probabilidades)



'''
Ejemplo 1
'''
C=['001','101','11','0001','000000001','0001','0000000000']
p=[0.5,0.1,0.1,0.1,0.1,0.1,0]
n=[5,2,1,1,1]

print("Ejemplo 1:")
print("Entropia de p: ", H1(p))
print("Entropia de n: ", H2(n))
print("Longitud media del codigo: ", LongitudMedia(C,p), '\n')

'''
Ejemplo 2
'''
C=['001','101','11','0001','000000001','0001','0000000000']
p=[0.2,0.2,0.1,0.1,0.1,0.1,0.2]
n=[1,2,1,5,1]

print("Ejemplo 2:")
print("Entropia de p: ", H1(p))
print("Entropia de n: ", H2(n))
print("Longitud media del codigo: ", LongitudMedia(C,p), '\n')

'''
Ejemplo 3
'''
C=['001','101','11','0001','000000001','0001','0000000000']
p=[0.2,0.2,0,0,0,0.4,0.2]
n=[2,2,2,2]

print("Ejemplo 3:")
print("Entropia de p: ", H1(p))
print("Entropia de n: ", H2(n))
print("Longitud media del codigo: ", LongitudMedia(C,p), '\n')

'''
Dibujar H(p,1-p)
'''
x = []
y = []
for p in np.arange(0, 1.0, 0.01):
    x.append(p)
    y.append(H1([p, 1 - p]))
plt.plot(x, y, 'm-', lw = 2)
plt.show()

print('\n')

'''
Hallar aproximadamente el máximo de  H(p,q,1-p-q)
'''
entropia_maxima = 0
for p in np.arange(0, 1.0, 0.01):
    for q in np.arange(0, 1.0 - p, 0.01):
        entropia = H1([p, q, 1 - p - q])
        if entropia >= entropia_maxima:
            entropia_maxima = entropia
print("Entropia maxima: ", entropia_maxima)


