# -*- coding: utf-8 -*-

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
from math import log2
from bisect import bisect


import scipy.ndimage
from scipy.cluster.vq import vq, kmeans

#%%
imagen = misc.ascent()#Leo la imagen
(n,m)=imagen.shape # filas y columnas de la imagen
#plt.imshow(imagen, cmap=plt.cm.gray) 
#plt.xticks([])
#plt.yticks([])
#plt.show() 
        
"""
Mostrar la imagen habiendo cuantizado los valores de los píxeles en
2**k niveles, k=1..8

Para cada cuantización dar la ratio de compresión y Sigma

Sigma=np.sqrt(sum(sum((imagenOriginal-imagenCuantizada)**2)))/(n*m)

"""

def ratio(pix1, escala, entradas, pix2):
    num = pix1*pix1*log2(escala)
    den = (pix1/pix2)*(pix1/pix2)*log2(entradas) + entradas*pix2*pix2*log2(escala)
    return num/den

def cuantizar():
    imagen = misc.ascent()
    (n,m)=imagen.shape
    imagen_original = imagen[::]
    for k in range(1, 9):
        rango = int(256/pow(2, k))
        imagen = np.floor(np.divide(imagen, rango))
        imagen = np.floor(np.multiply(imagen, rango))
        imagen = np.add(imagen, rango/2)
        plt.imshow(imagen, cmap=plt.cm.gray) 
        plt.xticks([])
        plt.yticks([])
        plt.show() 
        print("Ratio: ", ratio(n, rango, 256, k*3))
        print("Sigma: ", np.sqrt(sum(sum((imagen_original - imagen)**2)))/(n*m))
        imagen = imagen_original[::]
cuantizar()



#%%
"""
Mostrar la imagen cuantizando los valores de los pixeles de cada bloque
n_bloque x n_bloque en 2^k niveles, siendo n_bloque=8 y k=2

Calcular Sigma y la ratio de compresión (para cada bloque 
es necesario guardar 16 bits extra para los valores máximos 
y mínimos del bloque, esto supone 16/n_bloque**2 bits más por pixel).
"""

      
            



           
