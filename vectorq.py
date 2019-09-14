# -*- coding: utf-8 -*-
"""
Aarón Jiménez García
"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
from scipy.cluster.vq import vq, kmeans

#%%
#lena=scipy.misc.imread('C:/Users/MIPC/Desktop/lena_gray_512.png')
#(n,m)=lena.shape # filas y columnas de la imagen
#plt.figure()    
#plt.imshow(lena, cmap=plt.cm.gray)
#plt.show()
 

#%%
   
"""
Usando K-means http://docs.scipy.org/doc/scipy/reference/cluster.vq.html
crear un diccionario cuyas palabras sean bloques 8x8 con 512 entradas 
para la imagen de Lena.
"""

lena=scipy.misc.imread('C:/Users/MIPC/Desktop/lena_gray_512.png')
(n,m)=lena.shape

def crear_diccionario(imagen, bloque_i, bloque_j, size_bloque):
    mat_bloque = []
    for i in range(0, bloque_i):
        for j in range(0, bloque_j):
            lista = imagen[size_bloque*i:size_bloque*(i + 1), size_bloque*j:size_bloque*(j + 1)]
            lista = lista.flatten()
            mat_bloque.append(lista)
    dicc, _ = kmeans(mat_bloque, 512)
    return dicc.astype(int), mat_bloque

def añadir_a_imagen(fila, columna, lista, size_bloque, imagen):
    for i in range(size_bloque):
        for j in range(size_bloque):
            imagen[i + fila, j + columna] = lista[i, j]

def dibujar(diccionario, mat_bloque, n, m, size_bloque):
    imagen = np.zeros((n, m), dtype=np.uint8)
    code, _ = vq(mat_bloque, diccionario)
    j = 0
    i = 0
    rango = int((n*m)/(size_bloque*size_bloque))
    for k in range(rango):
        añadir_a_imagen(size_bloque*i, 
                        size_bloque*j, 
                        diccionario[code[k]].reshape(size_bloque, size_bloque),
                        size_bloque,
                        imagen)
        j = j + 1
        if k%64 == 63:
            j = 0
            i = i + 1
    plt.figure()
    plt.imshow(imagen, cmap=plt.cm.gray)
    plt.show()

lena = np.divide(lena, 1.0)
diccionario_lena, mat_bloque = crear_diccionario(lena, 512//8, 512//8, 8)


"""
Dibujar el resultado de codificar Lena con dicho diccionario.
"""

dibujar(diccionario_lena, mat_bloque, 512, 512, 8)

"""
Calcular el error, la ratio de compresión y el número de bits por píxel
"""

"""
Hacer lo mismo con la imagen Peppers (escala de grises)

http://atenea.upc.edu/mod/folder/view.php?id=1577653
http://www.imageprocessingplace.com/downloads_V3/root_downloads/image_databases/standard_test_images.zip
"""

peppers=scipy.misc.imread('C:/Users/MIPC/Desktop/peppers_gray.png')
(n,m)=peppers.shape

peppers = np.divide(peppers, 1.0)
diccionario_peppers, mat_bloque = crear_diccionario(peppers, 512//8, 512//8, 8)
dibujar(diccionario_peppers, mat_bloque, 512, 512, 8)

"""
Dibujar el resultado de codificar Peppers con el diccionarios obtenido
con la imagen de Lena.
"""

dibujar(diccionario_lena, mat_bloque, 512, 512, 8)

"""
Calcular el error.
"""



