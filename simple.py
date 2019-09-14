# -*- coding: utf-8 -*-

#Alumno: Aarón Jiménez García

import random

'''
0. Dada una codificación R, construir un diccionario para codificar m2c y otro para decodificar c2m
'''
R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])


'''
1. Definir una función Encode(M, m2c) que, dado un mensaje M y un diccionario 
de codificación m2c, devuelva el mensaje codificado C.
'''

def Encode(M, m2c):
    C = ''
    for x in M:
        if x in m2c:
            C += m2c[x]
        else:
            return 'Palabra no encontrada'
    return C
    
    
''' 
2. Definir una función Decode(C, c2m) que, dado un mensaje codificado C y un diccionario 
de decodificación c2m, devuelva el mensaje original M.
'''
def MayorCodigo(c2m):
    mayor = 0
    for x in c2m:
        if mayor < len(x):
            mayor = len(x)
    return mayor

def Decode(C, c2m):
    mayor = MayorCodigo(c2m)
    M = ''
    prefijo = ''
    for x in C:
        prefijo += x
        if prefijo in c2m:
            M += c2m[prefijo]
            prefijo = ''
        elif len(prefijo) > mayor:
            return "Codificación no encontrada"
    return M
  

#------------------------------------------------------------------------
# Ejemplo 1
#------------------------------------------------------------------------
print("Ejemplo 1")
R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

'''
3. Generar un mensaje aleatorio M de longitud 50 con las frecuencias 
esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e' y codificarlo.
'''

def LetrasProbabilidad():
    probability = random.randint(0, 100)
    if probability < 50:
        return 'a'
    if probability < 70:
        return 'b'
    if probability < 85:
        return 'c'
    if probability < 95:
        return 'd'
    else:
        return 'e'
    
M = [LetrasProbabilidad() for position in range(50)]
C = Encode(M,m2c)
print("Mensaje:")
print(M)
print("Mensaje codificado:")
print(C)

''' 
4. Si 'a', 'b', 'c', 'd', 'e' se codifican inicialmente con un código de 
bloque de 3 bits, hallar la ratio de compresión al utilizar el nuevo código.  
'''

r = (3*50)/len(C)
print("r = ", r, '\n')

#------------------------------------------------------------------------
# Ejemplo 2
#------------------------------------------------------------------------
print("Ejemplo 2")
R = [('a','0'), ('b','10'), ('c','110'), ('d','1110'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
5.
Codificar y decodificar 20 mensajes aleatorios de longitudes también aleatorios.  
Comprobar si los mensajes decodificados coinciden con los originales.
'''
Letras = ['a', 'b', 'c', 'd', 'e']
for i in range(20):
    longitud = random.randint(1, 10)
    M = ''
    for j in range(longitud):
        M += random.choice(Letras)
    print("Mensaje:")
    print(M)
    codificado = Encode(M, m2c)
    print("Mensaje codificado:")
    print(codificado)
    decodificado = Decode(codificado, c2m)
    print("Mensaje decodificado:")
    print(decodificado)
    print('')

print('')
#------------------------------------------------------------------------
# Ejemplo 3 
#------------------------------------------------------------------------
print("Ejemplo 3")
R = [('a','0'), ('b','01'), ('c','011'), ('d','0111'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
6. Codificar y decodificar los mensajes  'ae' y 'be'. 
Comprobar si los mensajes decodificados coinciden con los originales.
'''

C = Encode('ae', m2c)
print("Codificacion mensaje ae")
print(C)
M = Decode(C, c2m)
print("Decodificacion mensaje ae")
print(M)

C = Encode ('be', m2c)
print("Codificacion mensaje be")
print(C)
M = Decode(C, c2m)
print("Decodificacion mensaje be")
print(M, '\n')
print("No coinciden ya que a es prefijo de 01 y por tanto cuando el algoritmo", '\n',
      "detecta que hay un 0 opta directamente por la a sin tener en cuenta que", '\n',
      "b empieza tambien por 0. De igual forma pasaria con c y d.")





  




