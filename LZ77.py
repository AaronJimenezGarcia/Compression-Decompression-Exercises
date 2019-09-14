# -*- coding: utf-8 -*-


"""
Dado un mensaje, el tamaño de la ventana de trabajo W, y el tamaño
del buffer de búsqueda S dar la codificación del mensaje usando el
algoritmo LZ77


mensaje='cabracadabrarrarr'
LZ77Code(mensaje,12,18)=[[0, 0, 'c'], [0, 0, 'a'], 
  [0, 0, 'b'], [0, 0, 'r'], [3, 1, 'c'], [2, 1, 'd'], 
  [7, 4, 'r'], [3, 4, 'EOF']]
  
"""

def buscaCadenaBuffer(ventana, buffer):
    i = 0
    cadenaBusqueda = ""
    long_res = 0
    indice_res = 0
    while i < len(buffer) and i < len(ventana):
        cadenaBusqueda = cadenaBusqueda + ventana[i]
        indice = buffer.rfind(cadenaBusqueda)
        if indice != -1:
            long_res = len(cadenaBusqueda)
            indice_res = len(buffer) - indice
        else: break
        i = i + 1
    return cadenaBusqueda, long_res, indice_res

def vaciar(S, W, buffer, ventana, controlW, longm):
    while len(buffer) > S:
        buffer = buffer[1:]
    while len(ventana) < W and controlW < longm:
        ventana = ventana + mensaje[controlW]
        controlW = controlW + 1
    return ventana, buffer, controlW

def LZ77Code(mensaje,S=12,W=18):
    resultado = []
    controlW = W
    buffer = ""
    ventana = mensaje[:W]
    while ventana:
        cadenaBusqueda, long_res, indice_res = buscaCadenaBuffer(ventana, buffer)
        if cadenaBusqueda:
            if long_res == len(ventana): 
                tripleta = [indice_res, long_res, "EOF"]
            elif long_res + 1 == len(ventana) and ventana[-1] == buffer[long_res + 1]:
                tripleta = [indice_res, long_res + 1, "EOF"]
            else:
                tripleta = [indice_res, long_res, ventana[long_res]]
            buffer = buffer + ventana[:long_res + 1]
            ventana = ventana[long_res + 1:]
        else:
            tripleta = [0, 0, ventana[0]]
            buffer = buffer + ventana[0]
            ventana = ventana[1:]
        resultado.append(tripleta)
        ventana, buffer, controlW = vaciar(S, W, buffer, ventana, controlW, len(mensaje))
    return resultado

"""
Dado un mensaje codificado con el algoritmo LZ77 hallar el mensaje 
correspondiente 

code=[[0, 0, 'p'], [0, 0, 'a'], [0, 0, 't'], [2, 1, 'd'], 
      [0, 0, 'e'], [0, 0, 'c'], [4, 1, 'b'], [0, 0, 'r'], [3, 1, 'EOF']]

LZ77Decode(mensaje)='patadecabra'
"""   

def LZ77Decode(codigo):
    resultado = ""
    for i in range(len(codigo)):
        tripleta = codigo[i]
        if tripleta[1] == 0:
            resultado = resultado + tripleta[2]
        else:
            indice = len(resultado) - tripleta[0]
            indice2 = indice + tripleta[1]
            letras = resultado[indice:indice2]
            resultado = resultado + letras
            if tripleta[0] < tripleta[1]:
                resultado = resultado + letras[-1]
            if tripleta[2] == "EOF":
                break
            resultado = resultado + tripleta[2]
    return resultado

mensaje='cabracadabrarrarr'
codigo = LZ77Code(mensaje)
decode = LZ77Decode(codigo)
print("EJEMPLO 1:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')

mensaje = "abracadabrad"
codigo = LZ77Code(mensaje)
decode = LZ77Decode(codigo)
print("EJEMPLO 2:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')

mensaje = "patadecabra"
codigo = LZ77Code(mensaje)
decode = LZ77Decode(codigo)
print("EJEMPLO 3:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')

mensaje = "aaaaaaaaaaa"
codigo = LZ77Code(mensaje)
decode = LZ77Decode(codigo)
print("EJEMPLO 4:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')

"""
Jugar con los valores de S y W (bits_o y bits_l)
para ver sus efectos (tiempo, tamaño...)
"""

mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'
bits_o=12
bits_l=4
S=2**bits_o
W=2**bits_o+2**bits_l

print("EJEMPLO 5:")
#print("MENSAJE: ", mensaje)
import time
start_time = time.clock()
mensaje_codificado=LZ77Code(mensaje,S,W)
#print("CODIGO: ", mensaje_codificado)
print (time.clock() - start_time, "seconds code")
start_time = time.clock()
mensaje_recuperado=LZ77Decode(mensaje_codificado)
#print("DECODE: ", mensaje_recuperado)
print (time.clock() - start_time, "seconds decode")
ratio_compresion=8*len(mensaje)/((bits_o+bits_l+8)*len(mensaje_codificado))
print('Longitud de mensaje codificado:', len(mensaje_codificado))
print('Ratio de compresión:', ratio_compresion)
print("¿IGUALES?: ", mensaje_recuperado==mensaje, '\n')

print("EJEMPLO 6:")
mensaje = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus porttitor dignissim eros molestie volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Vestibulum at tristique lectus. Quisque interdum vehicula commodo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras pulvinar mauris non tellus dignissim laoreet. Donec ex enim, tempor eget mauris ac, condimentum tincidunt elit. Proin in porta urna, id accumsan est. Integer nibh ligula, rutrum a dui a, iaculis dignissim mauris. Vestibulum eleifend ex augue, ac lobortis lacus condimentum et. Ut pulvinar laoreet fringilla. Etiam at mi arcu. Sed porttitor rhoncus erat eget dapibus. Sed fringilla arcu a turpis bibendum ultrices. Sed pellentesque erat ut nisi sagittis, id ultrices nulla sagittis. Donec ac massa quis est maximus sodales. Integer non convallis turpis. Mauris ullamcorper, lacus rutrum euismod varius, elit turpis interdum libero, a posuere urna mi eget elit. Praesent non nulla nisi. Quisque euismod, arcu ut ultrices convallis, lorem purus tristique augue, elementum feugiat eros eros in quam. In aliquet dapibus tellus in pellentesque. Nulla facilisi. Suspendisse id imperdiet odio, nec pellentesque dui. Sed ullamcorper libero neque, ut lobortis nisl condimentum nec. Curabitur ornare dapibus semper. Sed pellentesque venenatis arcu id efficitur. Nunc suscipit nibh ac elit interdum tincidunt. Nunc sit amet placerat metus. Integer elementum enim ut quam lacinia elementum. Praesent fermentum urna in velit bibendum, sit amet ullamcorper nunc tincidunt. Pellentesque laoreet risus ut nibh suscipit, eget convallis sem dictum. Aliquam erat volutpat. Integer tristique maximus porttitor. Integer molestie vel nulla in mattis. Duis nunc magna, tempus in purus quis, pretium fermentum nibh. Donec id risus ac nisi porta viverra. Cras ut nunc sit amet magna facilisis aliquam. Nunc orci eros, rhoncus sed bibendum sed, viverra a odio. Donec pretium vitae dui eu volutpat. Duis fringilla semper nunc, eu aliquet ante rutrum eget. Aenean in nibh quis nibh auctor ullamcorper at vitae nibh. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin facilisis eget risus pretium pretium. Nullam sit amet viverra risus, porttitor dapibus justo. Morbi vestibulum laoreet libero placerat euismod. Nulla sit amet sem cursus velit sagittis posuere. Sed commodo euismod odio, a viverra nibh gravida at. Cras viverra convallis fringilla. Quisque placerat ipsum nisl, eget euismod mi auctor cursus. Aliquam erat volutpat. Quisque pretium ultrices enim vitae scelerisque. Etiam egestas euismod turpis sed feugiat. Aliquam feugiat tempor consectetur. Maecenas massa nibh, ultrices ac auctor quis, aliquet eu nibh. Vestibulum sed risus nisi. Donec risus leo, pharetra id libero quis, ullamcorper tristique sem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Phasellus imperdiet et mi ut molestie. Fusce sollicitudin odio quis nisl venenatis posuere. Donec id odio sed augue venenatis varius. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.'
bits_o=12
bits_l=4
S=2**bits_o
W=2**bits_o+2**bits_l

import time
start_time = time.clock()
mensaje_codificado=LZ77Code(mensaje,S,W)
#print("CODIGO: ", mensaje_codificado)
print (time.clock() - start_time, "seconds code")
start_time = time.clock()
mensaje_recuperado=LZ77Decode(mensaje_codificado)
#print("DECODE: ", mensaje_recuperado)
print (time.clock() - start_time, "seconds decode")
ratio_compresion=8*len(mensaje)/((bits_o+bits_l+8)*len(mensaje_codificado))
print('Longitud de mensaje codificado:', len(mensaje_codificado))
print('Ratio de compresión:', ratio_compresion)
print("¿IGUALES?: ", mensaje_recuperado==mensaje)
