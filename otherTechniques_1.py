# -*- coding: utf-8 -*-




"""
Dado un mensaje y un alfabeto, dar su codificación usando la técnica 
de 'Move to Front'.


mensaje='mi mama me mima mucho'
alfabeto=[' ', 'a', 'c', 'e', 'h', 'i', 'm', 'o', 'u']
MtFCode(mensaje,alfabeto)=[6, 6, 2, 2, 3, 1, 1, 2, 2, 5, 2, 
                           2, 4, 1, 4, 3, 2, 8, 6, 7, 8]

"""

def MtFCode(mensaje,alfabeto):
    secuencia = []
    lista = list(alfabeto)
    for i in mensaje:
        index = lista.index(i)
        lista.remove(i)
        lista.insert(0, i)
        secuencia.append(index)
    return secuencia

"""
Dado un mensaje codificado usando la técnica de 'Move to Front'
y el alfabeto usado, dar el mensaje original.

code=[8, 2, 5, 1, 4, 7, 7, 1, 6, 6, 5, 6, 1, 9, 8, 9, 1, 7, 8, 
      8, 8, 7, 8, 1, 1, 1]     
alfabeto=[' ', 'e', 'f', 'i', 'l', 'n', 'o', 's', 't', 'v']
MtFDecode(code,alfabeto)='telefono television telele'

"""

def MtFDecode(code,alfabeto):
    resultado = ""
    lista = list(alfabeto)
    for i in code:
        letra = lista[i]
        resultado = resultado + letra
        lista.remove(letra)
        lista.insert(0, letra)
    return resultado

print("EJEMPLOS MTF: ", '\n')
mensaje='mi mama me mima mucho'
alfabeto=[' ', 'a', 'c', 'e', 'h', 'i', 'm', 'o', 'u']
code = MtFCode(mensaje, alfabeto)
decode = MtFDecode(code, alfabeto)
print("MENSAJE: ", mensaje)
print("ALFABETO: ", alfabeto)
print("CODE: ", code)
print("IGUALES CODE? :", code ==[6, 6, 2, 2, 3, 1, 1, 2, 2, 5, 2, 2, 4, 1, 4, 3, 2, 8, 6, 7, 8])
print("DECODE: ", decode)
print("IGUALES DECODE? :", decode == 'mi mama me mima mucho', '\n')
    
mensaje='telefono television telele'
alfabeto=[' ', 'e', 'f', 'i', 'l', 'n', 'o', 's', 't', 'v']
code = MtFCode(mensaje, alfabeto)
decode = MtFDecode(code, alfabeto)
print("MENSAJE: ", mensaje)
print("ALFABETO: ", alfabeto)
print("CODE: ", code)
print("IGUALES CODE? :", code ==[8, 2, 5, 1, 4, 7, 7, 1, 6, 6, 5, 6, 1, 9, 8, 9, 1, 7, 8, 8, 8, 7, 8, 1, 1, 1])
print("DECODE: ", decode)
print("IGUALES DECODE? :", decode == 'telefono television telele', '\n')

"""
Dada una lista, dar su codificación usando 'Run Length Encoding'.

lista=[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'c', 'e', 'h', 'i', 
       'i', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'o', 'u']    
RLE(lista)=[[' ', 4], ['a', 3], ['c', 1], ['e', 1], ['h', 1], 
            ['i', 2], ['m', 7], ['o', 1], ['u', 1]]




lista=[8, 2, 5, 1, 4, 7, 7, 1, 6, 6, 5, 6, 1, 9, 8, 9, 1, 7, 8, 
      8, 8, 7, 8, 1, 1, 1]
RLE(lista)=[[8, 1], [2, 1], [5, 1], [1, 1], [4, 1], [7, 2], 
              [1, 1], [6, 2], [5, 1], [6, 1], [1, 1], [9, 1], 
              [8, 1], [9, 1], [1, 1], [7, 1], [8, 3], [7, 1], 
              [8, 1], [1, 3]]


"""

def RLE(lista):
    resultado = []
    anterior = lista[0]
    total = 0
    for i in lista:
        if anterior == i:
            total = total + 1
        else:
            resultado.append([anterior, total])
            total = 1
        anterior = i
    resultado.append([anterior, total])
    return resultado
        

"""
Dada una lista codificada usando 'Run Length Encoding', 
dar la lista original.

code=[[' ', 4], ['a', 3], ['c', 1], ['e', 1], ['h', 1], 
            ['i', 2], ['m', 7], ['o', 1], ['u', 1]]           
RLD(code)=[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'c', 'e', 'h', 'i', 
       'i', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'o', 'u']
       

code=[[8, 1], [2, 1], [5, 1], [1, 1], [4, 1], [7, 2], 
              [1, 1], [6, 2], [5, 1], [6, 1], [1, 1], [9, 1], 
              [8, 1], [9, 1], [1, 1], [7, 1], [8, 3], [7, 1], 
              [8, 1], [1, 3]]
RLD(code)=[8, 2, 5, 1, 4, 7, 7, 1, 6, 6, 5, 6, 1, 9, 8, 9, 1, 7, 8, 
      8, 8, 7, 8, 1, 1, 1]
      
"""

def RLD(code):
    resultado = []
    for i in code:
        veces = i[1]
        for j in range(veces):
            resultado.append(i[0])
    return resultado

print("EJEMPLOS RLE, RLD:", '\n')
lista=[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'c', 'e', 'h', 'i', 
       'i', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'o', 'u'] 
code = RLE(lista)
decode = RLD(code)
print("LISTA: ", lista)
print("CODE: ", code)
print("IGUALES CODE? :", code ==[[' ', 4], ['a', 3], ['c', 1], ['e', 1], ['h', 1], ['i', 2], ['m', 7], ['o', 1], ['u', 1]])
print("DECODE: ", decode)
print("IGUALES DECODE? :", decode == [' ', ' ', ' ', ' ', 'a', 'a', 'a', 'c', 'e', 'h', 'i', 'i', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'o', 'u'] , '\n')

lista=[8, 2, 5, 1, 4, 7, 7, 1, 6, 6, 5, 6, 1, 9, 8, 9, 1, 7, 8, 
      8, 8, 7, 8, 1, 1, 1]
code = RLE(lista)
decode = RLD(code)
print("LISTA: ", lista)
print("CODE: ", code)
print("IGUALES CODE? :", code == [[8, 1], [2, 1], [5, 1], [1, 1], [4, 1], [7, 2], 
              [1, 1], [6, 2], [5, 1], [6, 1], [1, 1], [9, 1], 
              [8, 1], [9, 1], [1, 1], [7, 1], [8, 3], [7, 1], 
              [8, 1], [1, 3]])
print("DECODE: ", decode)
print("IGUALES DECODE? :", decode ==[8, 2, 5, 1, 4, 7, 7, 1, 6, 6, 5, 6, 1, 9, 8, 9, 1, 7, 8, 
      8, 8, 7, 8, 1, 1, 1], '\n')

"""
Dado un mensaje, aplicar la transformación de Burrows-Wheeler
devolviendo la última columna y la posición.

mensaje='cadacamacasapasa'
BWT(mensaje)=('sdmccspcaaaaaaaa', 8)

"""

def permutar(mensaje):
    permutaciones = []
    posicion_original = -1
    for i in range(len(mensaje)):
        mensaje = mensaje[1:] + mensaje[0]
        permutaciones.append(mensaje)
    return permutaciones, posicion_original

def BWT(mensaje):
    mensaje_original = mensaje
    permutaciones, posicion = permutar(mensaje)
    ultima_columna = ''
    permutaciones = sorted(permutaciones, key=str.lower)
    for p in permutaciones:
        ultima_columna = ultima_columna + p[-1]
    posicion = permutaciones.index(mensaje_original)
    return ultima_columna, posicion    

print("EJEMPLOS BW: ", '\n')
mensaje='cadacamacasapasa'
code, posicion = BWT(mensaje)
print("MENSAJE: ", mensaje)
print("CODE: ", code)
print("POSICION: ", posicion)
print("IGUALES CODE? :", code == 'sdmccspcaaaaaaaa', posicion == 8)

"""
Dado el resultado (ultima_columna y posición) de aplicar 
la transformación de Burrows-Wheeler a un mensaje, dar el mensaje
original.

ultima_columna='pssmipissii'
posicion=4
iBWT(ultima_columna,posicion)=mississippi

"""
"""

def iBWT(ultima_columna, posicion):

"""



"""
Dado un mensaje (y un alfabeto) BWCode aplica sucesivamente al
mensaje BWT, MtF y RLE.

BWDecode aplica las transformaciones inversas para recuperar 
el mensaje original

"""
"""
def BWCode(mensaje,alfabeto=[]):
    alfa=alfabeto[:]
    if alfa==[]:
        alfa=[chr(i) for i in range(1,255)]
    codeBW,posicion=BWT(mensaje)
    codeMtF=MtFCode(codeBW,alfa)
    codeRLE=RLE(codeMtF)
    return codeRLE, posicion
    
def BWDecode(codeRLE,posicion,alfabeto=[]):
    alfa=alfabeto[:]
    if alfa==[]:
        alfa=[chr(i) for i in range(1,255)]
    codeRLE_recuperado=RLD(codeRLE)
    codeMtF_recuperado=MtFDecode(codeRLE_recuperado,alfa)
    mensaje_recuperado=iBWT(codeMtF_recuperado,posicion)
    return mensaje_recuperado
"""






"""

#########################################################
import time

alfabeto=[chr(i) for i in range(1,255)]

#mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'
#mensaje='a'*10000 #10000 como máximo (dependerá de la máquina)
#mensaje='abc'*5000 #10000 como máximo (dependerá de la máquina)

start_time = time.clock()
code, posicion=BWCode(mensaje,alfabeto)
print (time.clock() - start_time, "seconds CODE")


start_time = time.clock()
mensaje_recuperado=BWDecode(code,posicion)
print (time.clock() - start_time, "seconds DECODE")

ratio_compresion=8*len(mensaje)/((8+16)*len(code))
print("ratio_compresion=",ratio_compresion)


if (mensaje!=mensaje_recuperado):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(len(mensaje),len(mensaje_recuperado))
        print(mensaje[-5:],mensaje_recuperado[-5:])

"""
