# -*- coding: utf-8 -*-
"""
Aarón Jiménez García
"""

import math
import collections
#%%----------------------------------------------------

class Nodo:
    def __init__(self, probabilidad, letra, hijo_izq=None, hijo_der=None):
        self.letra = letra
        self.probabilidad = probabilidad
        self.hijo_izq = hijo_izq
        self.hijo_der = hijo_der
    
    def __lt__(self, other):
        return self.probabilidad < other.probabilidad

'''
Dada una distribucion de probabilidad, hallar un código de Huffman asociado
'''

def crear_arbol(p):
    nodos = list()
    for letra, probabilidad in p:
        nodos.append(Nodo(probabilidad, letra, None, None))
    while len(nodos) > 1:
        nodo_padre = Nodo(nodos[0].probabilidad + nodos[1].probabilidad, 
                          nodos[0].letra + nodos[1].letra, nodos[0], nodos[1])
        nodos.append(nodo_padre)
        nodos.pop(0)
        nodos.pop(0)
        nodos = sorted(nodos)
    return nodo_padre

def crear_codigo(arbol, codigo, huffman):
    if arbol.hijo_izq == None and arbol.hijo_der == None:
        huffman[arbol.letra] = codigo
        return codigo
    else:
        codigo_izq = crear_codigo(arbol.hijo_izq, codigo + "0", huffman)
        codigo_der = crear_codigo(arbol.hijo_der, codigo + "1", huffman)
        return codigo_izq + codigo_der
    
def Huffman(p): 
    p = sorted(p.items(), key=lambda value: value[1])
    arbol = crear_arbol(p)
    codigo = {}
    crear_codigo(arbol, "", codigo)
    return codigo

def H(p):
    total = 0
    for i in p:
        if i != 0:
            total = total + i*math.log(1/i, 2)
    return total

def LongitudMedia(huff,dic):
    longitud = 0
    for letra, prob in dic.items():
        longitud = longitud + prob*len(huff[letra])
    return longitud
#%%----------------------------------------------------

'''
Dada la ddp p=[0.80,0.1,0.05,0.05], hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''

def crear_dic(p):
    letra = "a"
    dic = {}
    for i in p:
        dic[letra] = i
        letra = letra + "a"
    return dic

p=[0.8,0.1,0.05,0.05]
print("Ejercicio 1:")
print("Ejemplo con p: ", p)
dic = crear_dic(p)
print("Diccionario utilizado con p como ejemplo: ", dic)
print("Codigo de Huffman: ", [y for(x, y) in sorted((Huffman(dic)).items(), key=lambda value: value[0])])
print("Entropia de p: ", H(p))
print("Longitud media de p: ", LongitudMedia(Huffman(dic), dic), '\n')

q=[0.1, 0.2, 0.3, 0.4]
print("Ejemplo con q: ", q)
dic = crear_dic(q)
print("Diccionario utilizado con q como ejemplo: ", dic)
print("Codigo de Huffman: ",[y for(x, y) in sorted((Huffman(dic)).items(), key=lambda value: value[0])])
print("Entropia de q: ", H(q))
print("Longitud media de q: ", LongitudMedia(Huffman(dic), dic), '\n')

r=[0.1, 0.1, 0.2, 0.2, 0.2, 0.2]
print("Ejemplo con r: ", r)
dic = crear_dic(r)
print("Diccionario utilizado con r como ejemplo: ", dic)
print("Codigo de Huffman: ", [y for(x, y) in sorted((Huffman(dic)).items(), key=lambda value: value[0])])
print("Entropia de r: ", H(r))
print("Longitud media de r: ", LongitudMedia(Huffman(dic), dic), '\n')

#%%----------------------------------------------------

'''
Dada la ddp p=[1/n,..../1/n] con n=2**8, hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''
print("Ejercicio 2:")
n=2**8
p=[1/n for _ in range(n)]
dic = crear_dic(p)

print("Codigo de Huffman: ", [y for(x, y) in sorted((Huffman(dic)).items(), key=lambda value: value[0])])
print("Entropia de p: ", H(p))
print("Longitud media de p: ", LongitudMedia(Huffman(dic), dic), '\n')

#%%----------------------------------------------------

'''
Dado un mensaje hallar la tabla de frecuencia de los caracteres que lo componen
'''

print("Ejercicio 3:")
def tablaFrecuencias(mensaje):
    counter = collections.Counter(mensaje)
    tabla_freq = {}
    for key, value in counter.items():
        tabla_freq[key] = value/len(mensaje)
    return tabla_freq

print("Ejemplo tabla frecuencias:")
mensaje = ["a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "d", "e", "e"]
print("Tabla de frecuencias: ", tablaFrecuencias(mensaje), '\n')

#%%----------------------------------------------------
'''
Definir una función que codifique un mensaje utilizando un código de Huffman 
obtenido a partir de las frecuencias de los caracteres del mensaje.

Definir otra función que decodifique los mensajes codificados con la función 
anterior.
'''

def EncodeHuffman(mensaje_a_codificar):
    m2c = Huffman(tablaFrecuencias(mensaje_a_codificar))
    mensaje_codificado = ""
    for letra in mensaje_a_codificar:
        mensaje_codificado = mensaje_codificado + m2c[letra]
    return mensaje_codificado, m2c
    
 
def DecodeHuffman(mensaje_codificado,m2c):
    mensaje_decodificado = ""
    c2m={v: k for k, v in m2c.items()}
    palabra = ""
    for cod in mensaje_codificado:
        palabra = palabra + cod
        if c2m.get(palabra) is not None:
            mensaje_decodificado = mensaje_decodificado + c2m.get(palabra)
            palabra = ""
    return mensaje_decodificado
  
#%%----------------------------------------------------

'''
Ejemplo
'''
print("Ejercicio 4:")
mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'
mensaje_codificado, m2c=EncodeHuffman(mensaje)
#print("Mensaje codificado: ", mensaje_codificado)
#print("Codigo utilizado: ", m2c)
mensaje_recuperado=DecodeHuffman(mensaje_codificado,m2c)
print(mensaje_recuperado)
ratio_compresion=8*len(mensaje)/len(mensaje_codificado)
print(ratio_compresion)

'''
Si tenemos en cuenta la memoria necesaria para almacenar el diccionario, 
¿cuál es la ratio de compresión?
'''