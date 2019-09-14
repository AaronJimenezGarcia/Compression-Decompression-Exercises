# -*- coding: utf-8 -*-


import math
import random
from bisect import bisect

"""
Dado x en [0,1) dar su representacion en binario, por ejemplo
dec2bin(0.625)='101'
dec2bin(0.0625)='0001'

Dada la representación binaria de un real perteneciente al intervalo [0,1) 
dar su representación en decimal, por ejemplo

bin2dec('101')=0.625
bin2dec('0001')=0.0625

nb número máximo de bits

"""

def dec2bin(x,nb=100):
    frac, entero = math.modf(x)
    binario = ""#bin(int(whole))[2:]
    while nb != 0 and frac != 1.0 and frac != 0.0:
        nb = nb - 1
        frac, entero = math.modf(frac*2)
        binario = binario + str(int(entero))
    return binario

def bin2dec(xb):
    decimal = 0.0
    potencia = 2
    for valor in xb:
        decimal = decimal + int(valor)/potencia
        potencia = potencia*2
    return decimal

print("Prueba la funcion dec2bin con valor 0.625:")
binario = dec2bin(0.625, 3)
print("Representacion binaria: ", binario)
print("Prueba la funcion bin2dec con valor 0.625:")
print("Representacion decimal: ", bin2dec(binario))

print("Prueba la funcion dec2bin con valor 0.0625:")
binario = dec2bin(0.0625, 4)
print("Representacion binaria: ", binario)
print("Prueba la funcion bin2dec con valor 0.0625:")
print("Representacion decimal: ", bin2dec(binario), '\n')

"""
Dada una distribución de probabilidad p(i), i=1..n,
hallar su función distribución:
f(0)=0
f(i)=sum(p(k),k=1..i).
"""

def cdf(p):
    func_distr = [0]
    for i in range(len(p)):
        func_distr.append(p[i] + func_distr[-1])
    return func_distr

print("Prueba la funcion cdf con p = [0.4, 0.3, 0.2, 0.1]. Resultado esperado: [0, 0.4, 0.7, 0.9, 1.0]")
p = [0.4, 0.3, 0.2, 0.1]
print("Resultado: ", cdf(p), '\n')

"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar el intervalo (l,u) que representa al mensaje.
"""

def Arithmetic(mensaje,alfabeto,probabilidades):
    m = 0.0
    M = 1.0
    func_distr = cdf(probabilidades)
    for letra in mensaje:
        i = alfabeto.index(letra);
        aux = m
        m = m + (M - m)*func_distr[i]
        M = aux + (M - aux)*func_distr[i + 1]
    return m,M

print("Prueba la funcion Arithmetic. Resultado esperado: 0.876 0.8776")
mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
m, M = Arithmetic(mensaje,alfabeto,probabilidades)
print("Resultado: [", m, ", ", M, "]", '\n')

"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar la representación binaria de x/2**(t) siendo t el menor 
entero tal que 1/2**(t)<M-m, x entero (si es posible par) tal 
que m*2**(t)<= x <M*2**(t)
"""

def EncodeArithmetic1(mensaje,alfabeto,probabilidades):
    m, M = Arithmetic(mensaje, alfabeto, probabilidades)
    t = (math.log((1/(M - m))))/math.log(2)
    if not t.is_integer(): t = int(t) + 1
    inferior = pow(2, t)*m
    superior = pow(2, t)*M
    numero = inferior
    if not inferior.is_integer(): numero = int(inferior) + 1
    while numero < superior:
        if numero%2 == 0: return dec2bin(numero/pow(2, t))
        numero = numero + 1
    return dec2bin((numero - 1)/pow(2, t))

print("Prueba la funcion EncodeArithmetic1 con mensaje=ccda, alfabeto=['a','b','c','d'] y probabilidades=[0.4,0.3,0.2,0.1]. Resultado esperado: 111000001")
print("Resultado: ", EncodeArithmetic1(mensaje, alfabeto, probabilidades), '\n')

"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar el código que representa el mensaje obtenido a partir de la 
representación binaria de M y m
"""
    
def EncodeArithmetic2(mensaje,alfabeto,probabilidades):
     m, M = Arithmetic(mensaje, alfabeto, probabilidades)
     m = dec2bin(m)
     M = dec2bin(M)
     i = 0
     while m[i] == M[i]:
         i = i + 1
     if m[i] == '1':
         return m[:i + 1]
     else:
         return M[:i + 1]
     
print("Prueba la funcion EncodeArithmetic2 con mensaje=ccda, alfabeto=['a','b','c','d'] y probabilidades=[0.4,0.3,0.2,0.1]. Resultado esperado: 111000001")
print("Resultado: ", EncodeArithmetic2(mensaje, alfabeto, probabilidades), '\n')

"""
Dada la representación binaria del número que representa un mensaje, la
longitud del mensaje y el alfabeto con su distribución de probabilidad 
dar el mensaje original
"""

def DecodeArithmetic(code,n,alfabeto,probabilidades):
    func_distr = cdf(probabilidades)
    numero = bin2dec(code)
    resultado = ""
    for i in range(n):
        indice = bisect(func_distr, numero)
        resultado = resultado + alfabeto[indice - 1]
        numero = (numero - func_distr[indice - 1])/(func_distr[indice] - func_distr[indice - 1])
    return resultado
    
print("Prueba la funcion DecodeArithmetic con code=0, longitud=4, alfabeto=['a','b','c','d'] y probabilidades=[0.4,0.3,0.2,0.1]. Resultado esperado: aaaa")
code='0'
longitud=4
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
print("Resultado: ", DecodeArithmetic(code,longitud,alfabeto,probabilidades), '\n')

print("Prueba la funcion DecodeArithmetic con code='111000001', longitud=4, alfabeto=['a','b','c','d'] y probabilidades=[0.4,0.3,0.2,0.1]. Resultado esperado: ccda ")
code='111000001'
print("Resultado: ", DecodeArithmetic(code,4,alfabeto,probabilidades), '\n')

print("Prueba la funcion DecodeArithmetic con code='111000001', longitud=5, alfabeto=['a','b','c','d'] y probabilidades=[0.4,0.3,0.2,0.1]. Resultado esperado: ccdab ")
print("Resultado: ", DecodeArithmetic(code,5,alfabeto,probabilidades), '\n')

'''
Función que compara la longitud esperada del 
mensaje con la obtenida con la codificación aritmética
'''

def comparacion(mensaje,alfabeto,probabilidades):
    p=1.
    indice=dict([(alfabeto[i],i+1) for i in range(len(alfabeto))])
    for i in range(len(mensaje)):
        p=p*probabilidades[indice[mensaje[i]]-1]
    aux=-math.log(p,2), len(EncodeArithmetic1(mensaje,alfabeto,probabilidades)), len(EncodeArithmetic2(mensaje,alfabeto,probabilidades))
    print('Información y longitudes:',aux)    
    return aux
        
        
'''
Generar 10 mensajes aleatorios de longitud 10<=n<=20 aleatoria 
con las frecuencias esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e', codificarlo y compararlas longitudes 
esperadas con las obtenidas.
'''

print("Primero ejemplo de generar mensajes aleatorios:")

alfabeto=['a','b','c','d','e']
probabilidades=[0.5,0.2,0.15,0.1,.05]
U = 50*'a'+20*'b'+15*'c'+10*'d'+5*'e'
def rd_choice(X,k = 1):
    Y = []
    for _ in range(k):
        Y +=[random.choice(X)]
    return Y

l_max=20

for _ in range(10):
    n=random.randint(10,l_max)
    L = rd_choice(U, n)
    mensaje = ''
    for x in L:
        mensaje += x
    print('---------- ',mensaje)    
    C=comparacion(mensaje,alfabeto,probabilidades)
    print(C)

'''
Generar 10 mensajes aleatorios de longitud 10<=n<=100 aleatoria 
con las frecuencias esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e' y codificarlo.
'''
print('\n')
alfabeto=['a','b','c','d','e']
probabilidades=[0.5,0.2,0.15,0.1,.05]
U = 50*'a'+20*'b'+15*'c'+10*'d'+5*'e'
def rd_choice(X,k = 1):
    Y = []
    for _ in range(k):
        Y +=[random.choice(X)]
    return Y

l_max=100

for _ in range(10):
    n=random.randint(10,l_max)
    L = rd_choice(U, n)
    mensaje = ''
    for x in L:
        mensaje += x
    print('---------- ',mensaje)    
    C = EncodeArithmetic1(mensaje,alfabeto,probabilidades)
    print(C)
