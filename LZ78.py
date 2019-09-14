# -*- coding: utf-8 -*-

#Aarón Jiménez García

"""
Dado un mensaje dar su codificación  usando el
algoritmo LZ78


mensaje='wabba wabba wabba wabba woo woo woo'
LZ78Code(mensaje)=[[0, 'w'], [0, 'a'], [0, 'b'], [3, 'a'], 
                   [0, ' '], [1, 'a'], [3, 'b'], [2, ' '], 
                   [6, 'b'], [4, ' '], [9, 'b'], [8, 'w'], 
                   [0, 'o'], [13, ' '], [1, 'o'], [14, 'w'], 
                   [13, 'o'], [0, 'EOF']]
  
"""
def LZ78Code(mensaje):
    diccionario = dict()
    indice = 1
    resultado = []
    doblete = []
    i = 0
    while i < len(mensaje):
        if not mensaje[i] in diccionario:
            doblete = [0, mensaje[i]]
            diccionario[mensaje[i]] = indice
            resultado.append(doblete)
        else:
            aux = mensaje[i]
            while i + 1 < len(mensaje) and aux in diccionario:
                i = i + 1
                aux = aux + mensaje[i]
            if i == len(mensaje) - 1 and len(aux) == 1:
                doblete = [diccionario[mensaje[i]], "EOF"]
            else:
                doblete = [diccionario[aux[:-1]], mensaje[i]]
            diccionario[aux] = indice
            resultado.append(doblete)
        i = i + 1
        indice = indice + 1
    if resultado[-1][1]!='EOF': resultado.append([0,'EOF'])
    return resultado
          
    
"""
Dado un mensaje codificado con el algoritmo LZ78 hallar el mensaje 
correspondiente 

code=[[0, 'm'], [0, 'i'], [0, 's'], [3, 'i'], [3, 's'], 
      [2, 'p'], [0, 'p'], [2, ' '], [1, 'i'], [5, 'i'], 
      [10, 'p'], [7, 'i'], [0, ' '], [0, 'r'], [2, 'v'], 
      [0, 'e'], [14, 'EOF']]

LZ78Decode(mensaje)='mississippi mississippi river'
"""    

def LZ78Decode(codigo):
    diccionario = dict()
    resultado = ""
    indice = 1
    for doblete in codigo:
        if doblete[1] != "EOF":
            if not doblete[0]:
                resultado = resultado + doblete[1]
                diccionario[indice] = doblete[1]
            else:
                resultado = resultado + diccionario[doblete[0]] + doblete[1]
                diccionario[indice] = diccionario[doblete[0]] + doblete[1]
            indice = indice + 1
        elif doblete[0]:
            resultado = resultado + diccionario[doblete[0]]
    return resultado
        
    
mensaje='wabba wabba wabba wabba woo woo woo' 
codigo=LZ78Code(mensaje)
decode = LZ78Decode(codigo)
print("EJEMPLO 1:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')

mensaje='mississipi mississipi'
codigo=LZ78Code(mensaje)
decode = LZ78Decode(codigo)
print("EJEMPLO 2:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')

mensaje='mississippi mississippi river'
codigo=LZ78Code(mensaje)
decode = LZ78Decode(codigo)
print("EJEMPLO 3:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')

mensaje='cabracadabrarrarr'
codigo = LZ78Code(mensaje)
decode = LZ78Decode(codigo)
print("EJEMPLO 4:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')

mensaje = "abracadabrad"
codigo = LZ78Code(mensaje)
decode = LZ78Decode(codigo)
print("EJEMPLO 5:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')

mensaje = "patadecabra"
codigo = LZ78Code(mensaje)
decode = LZ78Decode(codigo)
print("EJEMPLO 6:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')

mensaje = "aaaaaaaaaaa"
codigo = LZ78Code(mensaje)
decode = LZ78Decode(codigo)
print("EJEMPLO 7:")
print("CODIGO: ", codigo)
print("DECODE: ", decode)
print("¿IGUALES?: ", mensaje==decode, '\n')


mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'

print("EJEMPLO 8:")
import time
bits_indice=12
start_time = time.clock()
mensaje_codificado=LZ78Code(mensaje)
print (time.clock() - start_time, "seconds CODE")
start_time = time.clock()
mensaje_recuperado=LZ78Decode(mensaje_codificado)
print (time.clock() - start_time, "seconds DECODE")
ratio_compresion=8*len(mensaje)/((bits_indice+8)*len(mensaje_codificado))
print(len(mensaje_codificado),ratio_compresion)
print("¿IGUALES?: ", mensaje_recuperado==mensaje, '\n')

mensaje = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus porttitor dignissim eros molestie volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Vestibulum at tristique lectus. Quisque interdum vehicula commodo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras pulvinar mauris non tellus dignissim laoreet. Donec ex enim, tempor eget mauris ac, condimentum tincidunt elit. Proin in porta urna, id accumsan est. Integer nibh ligula, rutrum a dui a, iaculis dignissim mauris. Vestibulum eleifend ex augue, ac lobortis lacus condimentum et. Ut pulvinar laoreet fringilla. Etiam at mi arcu. Sed porttitor rhoncus erat eget dapibus. Sed fringilla arcu a turpis bibendum ultrices. Sed pellentesque erat ut nisi sagittis, id ultrices nulla sagittis. Donec ac massa quis est maximus sodales. Integer non convallis turpis. Mauris ullamcorper, lacus rutrum euismod varius, elit turpis interdum libero, a posuere urna mi eget elit. Praesent non nulla nisi. Quisque euismod, arcu ut ultrices convallis, lorem purus tristique augue, elementum feugiat eros eros in quam. In aliquet dapibus tellus in pellentesque. Nulla facilisi. Suspendisse id imperdiet odio, nec pellentesque dui. Sed ullamcorper libero neque, ut lobortis nisl condimentum nec. Curabitur ornare dapibus semper. Sed pellentesque venenatis arcu id efficitur. Nunc suscipit nibh ac elit interdum tincidunt. Nunc sit amet placerat metus. Integer elementum enim ut quam lacinia elementum. Praesent fermentum urna in velit bibendum, sit amet ullamcorper nunc tincidunt. Pellentesque laoreet risus ut nibh suscipit, eget convallis sem dictum. Aliquam erat volutpat. Integer tristique maximus porttitor. Integer molestie vel nulla in mattis. Duis nunc magna, tempus in purus quis, pretium fermentum nibh. Donec id risus ac nisi porta viverra. Cras ut nunc sit amet magna facilisis aliquam. Nunc orci eros, rhoncus sed bibendum sed, viverra a odio. Donec pretium vitae dui eu volutpat. Duis fringilla semper nunc, eu aliquet ante rutrum eget. Aenean in nibh quis nibh auctor ullamcorper at vitae nibh. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin facilisis eget risus pretium pretium. Nullam sit amet viverra risus, porttitor dapibus justo. Morbi vestibulum laoreet libero placerat euismod. Nulla sit amet sem cursus velit sagittis posuere. Sed commodo euismod odio, a viverra nibh gravida at. Cras viverra convallis fringilla. Quisque placerat ipsum nisl, eget euismod mi auctor cursus. Aliquam erat volutpat. Quisque pretium ultrices enim vitae scelerisque. Etiam egestas euismod turpis sed feugiat. Aliquam feugiat tempor consectetur. Maecenas massa nibh, ultrices ac auctor quis, aliquet eu nibh. Vestibulum sed risus nisi. Donec risus leo, pharetra id libero quis, ullamcorper tristique sem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Phasellus imperdiet et mi ut molestie. Fusce sollicitudin odio quis nisl venenatis posuere. Donec id odio sed augue venenatis varius. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.'
print("EJEMPLO 9:")
import time
bits_indice=12
start_time = time.clock()
mensaje_codificado=LZ78Code(mensaje)
print (time.clock() - start_time, "seconds CODE")
start_time = time.clock()
mensaje_recuperado=LZ78Decode(mensaje_codificado)
print (time.clock() - start_time, "seconds DECODE")
ratio_compresion=8*len(mensaje)/((bits_indice+8)*len(mensaje_codificado))
print(len(mensaje_codificado),ratio_compresion)
print("¿IGUALES?: ", mensaje_recuperado==mensaje, '\n')

mensaje = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in placerat mauris. Aliquam mollis diam vitae lectus fermentum, quis ullamcorper urna volutpat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed enim risus, mattis ac ex viverra, scelerisque commodo felis. Sed a lacus lobortis, vulputate nulla eget, pharetra ante. Nullam ut felis non mauris interdum egestas vitae nec ante. Mauris eget lacus sit amet eros feugiat auctor. Suspendisse sit amet feugiat justo. Phasellus interdum venenatis quam, vitae finibus quam congue in. Cras non odio dictum erat faucibus luctus nec a leo. Ut nibh diam, hendrerit non magna ultrices, vehicula facilisis turpis. In condimentum sodales felis.Sed dapibus justo et velit ultricies, ut pharetra orci vulputate. Vivamus tempor dui sit amet pulvinar fringilla. Cras id tincidunt ligula. Maecenas hendrerit purus leo, nec elementum arcu finibus a. Praesent fringilla, mauris ut cursus fringilla, nisi metus euismod lacus, ac viverra velit urna eget tellus. Donec non sagittis felis, non vulputate massa. Proin efficitur, lectus eu volutpat cursus, dui arcu fringilla tortor, nec condimentum justo elit a velit. Fusce porttitor, sem et posuere ullamcorper, velit tortor elementum odio, vitae mollis mi arcu in lorem. Donec dictum neque nibh, vel ullamcorper est ullamcorper ac. Mauris eu lectus mauris. Morbi imperdiet pellentesque accumsan.Proin vel tincidunt lorem. In et nibh sit amet orci pulvinar elementum hendrerit a sapien. Quisque porttitor lorem dolor, in malesuada nulla lacinia id. In dignissim venenatis velit, sit amet dapibus odio commodo eu. Maecenas nec dolor mattis, vehicula dui et, sagittis mi. Aliquam in tortor imperdiet, mattis odio in, ultricies mauris. Vivamus eu dapibus odio. Nunc hendrerit lacus ac euismod fermentum. Vivamus dui mauris, porttitor a enim mattis, pretium maximus tellus.Nullam et enim interdum, mattis turpis blandit, eleifend ipsum. Suspendisse sed ipsum nec mi eleifend mattis. Morbi vitae elementum metus. Sed id molestie urna, non aliquet ante. Proin mattis accumsan dui sit amet egestas. Vestibulum posuere faucibus urna, id congue nisl efficitur at. Fusce tincidunt sed nisl ut varius. Pellentesque ac lacus non elit lacinia commodo. Fusce suscipit ligula a neque ultricies, ut vulputate elit tristique. Cras euismod ante tellus, a elementum ipsum faucibus ut. Quisque hendrerit non leo eu commodo. Pellentesque elementum sodales felis sed cursus. Phasellus mattis commodo tellus, nec molestie ligula interdum eu. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla facilisi. Aliquam ac mauris aliquet, vulputate odio id, ornare massa. Ut rutrum felis erat, vitae ornare tortor euismod non. Cras euismod, libero non eleifend dapibus, elit est sollicitudin tortor, id feugiat purus mi quis nulla. Morbi vulputate vehicula fringilla. Nam egestas posuere nulla, a fermentum nunc sagittis non. Nullam mollis mauris id ornare dignissim. Praesent gravida sollicitudin dui, sed fringilla mauris dictum in. Nullam gravida aliquet ipsum in tempor. Praesent auctor a purus eu finibus. Sed cursus metus sed rhoncus molestie. Suspendisse nec magna vel elit sollicitudin tristique eget quis felis. In sit amet ex vel elit viverra tincidunt quis vel sapien. Praesent urna urna, imperdiet ac pharetra a, luctus quis nisi. Vivamus hendrerit justo nulla, vitae malesuada leo posuere sed. Vivamus magna nibh, malesuada id nisi aliquam, gravida iaculis dui. Morbi tristique risus sed nibh ullamcorper, in vulputate ligula egestas. Vestibulum tincidunt massa mi, scelerisque luctus sapien consequat eu. Phasellus volutpat, tellus sed suscipit bibendum, est ligula ornare ipsum, vel ultrices enim risus non leo. Nunc volutpat, metus a venenatis vulputate, mi ligula scelerisque mi, vitae pretium velit odio sit amet felis. Praesent convallis porttitor diam, nec facilisis ex. Proin mattis, magna in ullamcorper eleifend, sem tortor dictum quam, et pulvinar purus massa quis odio. Vivamus vitae efficitur orci. Cras est velit, finibus id massa nec, mattis tristique diam. Pellentesque non cursus augue, a efficitur massa. Curabitur ut nibh malesuada justo cursus volutpat. Vivamus dictum purus et dolor rhoncus tristique. Nulla commodo odio sit amet massa tincidunt, aliquam scelerisque ex facilisis. Donec sed mattis sapien. Aliquam vel ex felis. In auctor lectus orci, et porta nibh ullamcorper accumsan. Morbi dapibus, risus sit amet interdum imperdiet, ligula enim commodo libero, eu sodales sapien massa vel arcu. Nulla facilisis quam magna, non blandit erat sollicitudin sed. Quisque ullamcorper nulla pulvinar lorem dictum dictum. Suspendisse potenti. Nulla posuere lobortis tellus, id malesuada urna ullamcorper at. Proin elementum arcu ultrices felis placerat, in semper felis aliquet. Donec volutpat tortor ligula, eget eleifend arcu bibendum id. Maecenas pulvinar, urna nec placerat mollis, lectus massa congue libero, quis finibus tellus tellus non augue. Ut malesuada ipsum nec lacus elementum varius. Maecenas consequat iaculis nisl ut pretium. Morbi sit amet suscipit nibh. Aliquam dapibus, metus ac imperdiet feugiat, lacus quam sodales quam, vitae laoreet augue nisi quis sem. In nec metus fringilla, sagittis tellus ut, imperdiet eros. Sed pellentesque quam quis luctus mollis. Donec mattis, leo sit amet mattis gravida, mi quam lacinia tortor, quis egestas justo turpis pulvinar diam. Aliquam eu mi est. Etiam at odio mi. Nunc et eros in augue congue ultrices a vitae quam. Curabitur sed pharetra nibh. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla blandit, felis quis volutpat scelerisque, ex mauris tempus neque, quis accumsan tellus metus quis risus. Suspendisse iaculis auctor pulvinar. Suspendisse dignissim metus velit, eget pulvinar nisl tempor sit amet. Phasellus consectetur quam erat, vel dictum risus pellentesque a. Curabitur hendrerit eleifend risus, eu elementum urna consectetur nec. Quisque sagittis molestie placerat. Vivamus vel tellus tincidunt, viverra sapien vitae, fermentum diam. Nullam faucibus enim eros, vitae sollicitudin massa venenatis in. Etiam et nibh vitae magna faucibus imperdiet. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed in laoreet tellus. Pellentesque et elit ut eros fermentum bibendum ac ac lorem. Cras ultrices sit amet velit laoreet tincidunt. Suspendisse feugiat mauris molestie, mattis risus in, faucibus sem. Praesent mauris enim, tincidunt id consectetur id, scelerisque vel eros. In scelerisque arcu ut tincidunt laoreet. Nulla vitae turpis bibendum, pretium lectus sit amet, bibendum ex. Donec ut nunc et metus volutpat egestas id a felis. Ut tristique lorem eu vulputate egestas. Nam neque nisl, laoreet eu tortor vitae, pretium bibendum neque. Proin tincidunt, nibh at lacinia faucibus, libero erat volutpat magna, nec accumsan arcu libero id orci. Maecenas consequat accumsan tempor. Fusce hendrerit semper luctus. Donec in auctor ligula. Cras ultrices dui sagittis, malesuada felis non, tristique lorem. Vivamus imperdiet metus libero, eget elementum mi pharetra id. Proin et fermentum metus. Pellentesque lacinia enim vitae nunc tempus, auctor tincidunt tellus congue. Nullam elementum nisl tincidunt maximus egestas. In malesuada consequat pulvinar. Phasellus odio erat, cursus eget bibendum nec, euismod in erat. Aliquam erat volutpat. Nulla facilisi. Curabitur non blandit libero. Vestibulum convallis dui laoreet ultrices elementum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec commodo aliquam felis, vel bibendum enim consequat ut. Pellentesque lacinia, tortor vitae pellentesque mattis, velit nisi ornare ante, sit amet vestibulum ligula arcu interdum ex. Phasellus in tempor nisi, vel congue orci. Mauris sollicitudin nunc non odio facilisis, sit amet rhoncus nunc auctor. Proin sagittis commodo orci, in elementum quam commodo sodales. Etiam rutrum, mi ut consequat volutpat, neque metus hendrerit odio, et porta tellus mauris in mi. In hac habitasse platea dictumst. Praesent vehicula massa vitae lectus lobortis dictum. Vestibulum risus metus, eleifend in arcu vitae, egestas porttitor arcu. Nullam sit amet nisi ac mauris rhoncus blandit. Duis accumsan, leo a venenatis pretium, dui nulla rhoncus metus, at aliquet orci risus et nunc. Cras ultricies euismod purus, ut sollicitudin ipsum. Vivamus eu diam ut neque suscipit egestas ac sed justo. Vivamus quis metus sed massa imperdiet pulvinar. Nullam elementum tristique maximus. Fusce arcu urna, eleifend non suscipit eget, placerat ut nibh. Donec convallis ultricies eros, sit amet eleifend lorem. Maecenas scelerisque eros nec felis ultricies lobortis. Curabitur varius, nulla sed luctus pretium, felis enim commodo dolor, ut sagittis ipsum ligula id libero. Aliquam vel ligula eget tellus mollis convallis. Nulla vitae eros tortor. Quisque tempus id erat id fermentum. Etiam non velit mauris. Sed eget eleifend augue, porttitor rutrum dolor. Quisque sed egestas orci, ac tristique risus. Sed pretium sapien lacus, vel sollicitudin felis lacinia fringilla. Phasellus in ultricies lacus. Ut tincidunt nisi a ex efficitur, nec mollis purus congue. Maecenas varius diam nulla, vel commodo dolor rhoncus gravida. Praesent posuere magna odio, id rutrum nibh convallis a. Praesent gravida interdum orci, quis tincidunt mauris fringilla vel. Mauris lobortis neque ex, eget vehicula nisi condimentum eu. Praesent mi augue, luctus quis euismod nec, fringilla nec quam. Aliquam sed efficitur felis. Etiam scelerisque vehicula ex, in imperdiet nisl pulvinar vitae. Aenean et lorem id felis tincidunt ornare in et nunc. Fusce lobortis eu nisl ut ultricies. Nulla tristique ac turpis eu vestibulum. Mauris posuere ultrices leo, ut lacinia ligula convallis at. Etiam sit amet cursus tortor, id iaculis massa. Nam finibus tincidunt enim, sit amet condimentum sem elementum id. Quisque lacus orci, sodales non gravida ac, semper sed ex. Suspendisse non posuere purus, a facilisis ipsum. Etiam auctor turpis in libero dapibus, quis blandit nibh tristique. Vestibulum ornare pharetra maximus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris vel lectus at eros pretium placerat. In risus sapien, ullamcorper vel nisi eleifend, vehicula maximus metus. Quisque eros enim, consequat vitae nibh sed, accumsan ornare augue. Curabitur vehicula ornare luctus. Phasellus urna tortor, laoreet quis turpis id, feugiat pellentesque nibh. Aenean malesuada neque id lectus aliquet rhoncus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus nec purus nec turpis malesuada tempus eu eu mi. In elementum accumsan risus nec placerat. Donec ultricies scelerisque eros non ornare. Aenean mauris erat, blandit vel est ut, lobortis suscipit justo. Sed luctus nunc eget finibus ultricies. Aenean pharetra libero sem, non imperdiet nisi consectetur non. Nulla ornare mi ut risus ultrices, sed lobortis ipsum volutpat. Mauris dui ante, rutrum sit amet dapibus sit amet, varius ac velit. Integer cursus mollis sodales. Vivamus suscipit neque ipsum, sit amet vestibulum eros interdum at. Aliquam at tempor lectus. In hac habitasse platea dictumst. Curabitur quis sagittis mi. Etiam nunc massa, aliquam in porttitor at, luctus eu tortor. Curabitur tempus aliquam euismod. Aenean fringilla augue eu ultrices dignissim. Nullam scelerisque turpis ut nulla condimentum, eget cursus enim hendrerit. Proin mollis pretium euismod. In blandit bibendum purus vitae blandit. In ac lorem vitae mauris rutrum consequat. Etiam fringilla turpis ante, vel pretium libero laoreet ut. Nunc a rhoncus nibh. Vivamus porta ut ex eget pellentesque. Donec lacinia iaculis molestie. Mauris hendrerit efficitur gravida. Duis hendrerit, urna in finibus congue, mauris est cursus dolor, nec faucibus magna enim sed diam. In nec malesuada ligula, et dapibus justo. Ut sagittis massa a lorem consectetur, sit amet condimentum orci iaculis. Praesent vitae dictum diam. Donec sed auctor purus. Quisque venenatis cursus congue. Pellentesque pharetra, ligula eu dictum feugiat, metus justo rutrum arcu, eget malesuada libero arcu scelerisque est. Morbi dignissim est eget pretium vestibulum. '
print("EJEMPLO 10:")
import time
bits_indice=12
start_time = time.clock()
mensaje_codificado=LZ78Code(mensaje)
print (time.clock() - start_time, "seconds CODE")
start_time = time.clock()
mensaje_recuperado=LZ78Decode(mensaje_codificado)
print (time.clock() - start_time, "seconds DECODE")
ratio_compresion=8*len(mensaje)/((bits_indice+8)*len(mensaje_codificado))
print(len(mensaje_codificado),ratio_compresion)
print("¿IGUALES?: ", mensaje_recuperado==mensaje, '\n')



    
