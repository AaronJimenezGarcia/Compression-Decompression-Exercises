# -*- coding: utf-8 -*-

import math
import itertools
"""
Aarón Jiménez García
"""

'''
Dada la lista L de longitudes de las palabras de un código 
q-ario, decidir si pueden definir un código.

'''
def  kraft1(L, q=2):
    suma = 0
    for l in L:
        suma += pow(1/q, l)
    return suma <= 1



'''
Dada la lista L de longitudes de las palabras de un código 
q-ario, calcular el máximo número de palabras de longitud 
máxima, max(L), que se pueden añadir y seguir siendo un código.

'''

def  kraft2(L, q=2):
    maximo = max(L)
    suma = 0
    for l in L:
        suma += pow(1/q, l)
    return (1 - suma)/(1 / pow(q, maximo))

'''
Dada la lista L de longitudes de las palabras de un  
código q-ario, calcular el máximo número de palabras 
de longitud Ln, que se pueden añadir y seguir siendo 
un código.
'''

def  kraft3(L, Ln, q=2):
    suma = 0
    for l in L:
        suma += pow(1/q, l)
    return (1 - suma)/(1 / pow(q, Ln))

'''
Dada la lista L de longitudes de las palabras de un  
código q-ario, hallar un código prefijo con palabras 
con dichas longitudes
'''

def codificacionInicial(L, q):
    codificaciones = []
    for i in range(q):
        codificaciones.append(i)
    return list(map(list, itertools.product(codificaciones, repeat = L[0])))

def concatenarDigitos(veces, lista, q):
    listaAuxiliar = []
    listaActualizada = lista
    for i in range(veces):
        for j in listaActualizada:
            for k in range(q):
                digito = list(j)
                digito.append(k)
                listaAuxiliar.append(digito)
        listaActualizada = listaAuxiliar
        listaAuxiliar = []
    return listaActualizada

def Code(L,q=2):
    if not kraft1(L, q): return "No es posible"
    L = sorted(L)
    lista = codificacionInicial(L, q)
    resultado = []
    actual = L[0]
    anterior = L[0]
    for i in L:
        actual = i
        if actual != anterior:
            lista = concatenarDigitos(actual - anterior, lista, q)
            anterior = actual
        resultado.append(lista[0])
        lista.pop(0)
    return resultado
            
            
'''
Ejemplo
'''
print("Ejemplo 1")
L=[1,3,5,5,10,3,5,7,8,9,9,2,2,2]
print(kraft1(L), '\n')

'''
Ejemplo 2
'''
print("Ejemplo 2")
L2 = [5, 5, 6, 7, 8, 2, 4] #es prefijo
print(kraft2(L2))
print(kraft3(L2, 8), '\n')

'''
Ejemplo 3
'''
print("Ejemplo 3")
print(sorted(L), ' codigo final:', Code(L, 3), '\n')

'''
Ejemplo 4
'''
print("Ejemplo 4")
print(sorted(L), ' codigo final:', Code(L, 2), '\n')

'''
Ejemplo 5
'''
L3 = [3, 4, 3, 2]
print("Ejemplo 5")
print(sorted(L3), ' codigo final:', Code(L3, 2), '\n')

'''
Ejemplo 6
'''
L4 = [2, 5, 8]
print("Ejemplo 6")
print(sorted(L4), ' codigo final:', Code(L4, 3), '\n')
