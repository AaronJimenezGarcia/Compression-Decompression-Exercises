# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import scipy
import scipy.ndimage
import math 
import time
from PIL import Image
pi=math.pi




import matplotlib.pyplot as plt




        
"""
Matrices de cuantización, estándares y otras
"""

    
Q_Luminance=np.array([
[16 ,11, 10, 16,  24,  40,  51,  61],
[12, 12, 14, 19,  26,  58,  60,  55],
[14, 13, 16, 24,  40,  57,  69,  56],
[14, 17, 22, 29,  51,  87,  80,  62],
[18, 22, 37, 56,  68, 109, 103,  77],
[24, 35, 55, 64,  81, 104, 113,  92],
[49, 64, 78, 87, 103, 121, 120, 101],
[72, 92, 95, 98, 112, 100, 103, 99]])

Q_Chrominance=np.array([
[17, 18, 24, 47, 99, 99, 99, 99],
[18, 21, 26, 66, 99, 99, 99, 99],
[24, 26, 56, 99, 99, 99, 99, 99],
[47, 66, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99]])

def Q_matrix(r=1):
    m=np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            m[i,j]=(1+i+j)*r
    return m

"""
Implementar la DCT (Discrete Cosine Transform) 
y su inversa para bloques NxN

dct_bloque(p,N)
idct_bloque(p,N)

p bloque NxN

"""

# w = C*P*C^T
def obtenerMatrizC(m, n):
    N = m
    C = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            if(i == 0): 
                C[i, j] = 1/math.sqrt(N)
            else:
                C[i, j] = math.sqrt(2/N)*math.cos(((2*j+1)*i*pi)/(2*N))
    return C

def dct_bloque(p):
    m, n = p.shape
    C = obtenerMatrizC(m, n)
    n = np.tensordot(np.tensordot(C, p, axes=([1][0])), np.transpose(C), axes=([1][0]))
    return n


def idct_bloque(p):
    m, n = p.shape
    C = obtenerMatrizC(m, n)
    n = np.tensordot(np.tensordot(np.transpose(C), p, axes=([1][0])), C, axes=([1][0]))
    return n

"""
Reproducir los bloques base de la transformación para los casos N=4,8
Ver imágenes adjuntas.
"""
"""
N = 4    
fig = plt.figure()
array = np.zeros((N, N))
array = array.astype(int)
for i in range(N):
    for j in range(N):
        array[i][j] = 1
        m = idct_bloque(array)
        fig.add_subplot(N, N, i*N + j + 1).axis('off')
        plt.imshow(np.array(Image.fromarray(m.reshape((N,N)))))
        array[i][j] = 0

N = 8
fig = plt.figure()
array = np.zeros((N, N))
array = array.astype(int)
for i in range(N):
    for j in range(N):
        array[i][j] = 1
        m = idct_bloque(array)
        fig.add_subplot(N, N, i*N + j + 1).axis('off')
        plt.imshow(np.array(Image.fromarray(m.reshape((N,N)))))
        array[i][j] = 0
"""
"""
Implementar la función jpeg_gris(imagen_gray) que: 
1. dibuje el resultado de aplicar la DCT y la cuantización 
(y sus inversas) a la imagen de grises 'imagen_gray' 

2. haga una estimación de la ratio de compresión
según los coeficientes nulos de la transformación: 
(#coeficientes/#coeficientes no nulos).

3. haga una estimación del error
Sigma=np.sqrt(sum(sum((imagen_gray-imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_gray)**2)))


"""

def dividirBloques(m ,n, imagen):
    matriz = np.zeros(((m*n)//64, 8, 8))
    z = 0
    for n1 in range(n//8):
        for n2 in range(m//8):		
            pos1 = n2*8
            pos2 = pos1 + 8
            pos3 = n1*8
            pos4 = pos3 + 8
            matriz[z]= imagen[pos1:pos2, pos3:pos4].reshape(8, 8)
            z = z + 1
    return matriz

def juntarBloques(m, n, imagen):
    matriz = np.zeros((m,n))
    z = 0
    for n1 in range(n//8):
        for n2 in range(m//8):		
            pos1 = n2*8
            pos2 = pos1 + 8
            pos3 = n1*8
            pos4 = pos3 + 8
            matriz[pos1:pos2, pos3:pos4] = imagen[z]
            z = z + 1
    return matriz

def aplicar2DCT(imagen, bloques):
    for i in range(bloques):
        imagen[i]=dct_bloque(imagen[i])
    for i in range(bloques):
        for j in range(8):
            for k in range(8):
                imagen[i, j, k] /= Q_Luminance[j, k]
                imagen[i, j, k] = round(imagen[i, j, k], 0)
                
def aplicar2IDCT(imagen, bloques):
    for i in range(bloques):
        for j in range(8):
            for k in range(8):
                imagen[i, j, k] *= Q_Luminance[j, k]
                imagen[i, j, k] = round(imagen[i, j, k], 0)
    for i in range(bloques):
        imagen[i]=idct_bloque(imagen[i])
    imagen += 128

def ratio(m, n, imagen):
    imagen_cuantizada = juntarBloques(m ,n, imagen)
    coef_nulo= (imagen_cuantizada == 0.).sum()
    return m*n/(m*n - coef_nulo)

def jpeg_gris(imagen_gray):
    fil, col = imagen_gray.shape
    
    """
    Hacer particiones 8x8
    """
    bloques_imagen = np.subtract(dividirBloques(fil, col, imagen_gray), 128)
    
    """
    Aplicar 2-DCT
    """
    bloques = (fil*col)//(8*8)
    
    aplicar2DCT(bloques_imagen, bloques)
    
    """
    Ratio
    """
    r = ratio(fil, col, bloques_imagen)
    
    """
    DECOMPRESION
    Aplicar 2-IDCT
    """    
    aplicar2IDCT(bloques_imagen, bloques)
    
    """
    Juntar bloques
    """
    imagen_jpeg = juntarBloques(fil, col, bloques_imagen).astype(np.uint8)
    
    """
    Error
    """
    imagen_error = imagen_jpeg[::]
    imagen_error = imagen_error.astype(np.int64)
    sigma = np.sqrt(sum(sum((imagen_gray - imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_gray)**2)))    
    return r, sigma, imagen_jpeg


"""
Implementar la función jpeg_color(imagen_color) que: 
1. dibuje el resultado de aplicar la DCT y la cuantización 
(y sus inversas) a la imagen RGB 'imagen_color' 

2. haga una estimación de la ratio de compresión
según los coeficientes nulos de la transformación: 
(#coeficientes/#coeficientes no nulos).

3. haga una estimación del error para cada una de las componentes RGB
Sigma=np.sqrt(sum(sum((imagen_color-imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_color)**2)))

"""

"""
Compresion
"""

def rgb2ycbcr(imagen):
    fil, col, color = imagen.shape
    imagenY = np.zeros((fil, col))
    imagenCb = np.zeros((fil, col))
    imagenCr = np.zeros((fil, col))
    for i in range(fil):
        for j in range(col):
            R = imagen[i, j, 0]
            G = imagen[i, j, 1]
            B = imagen[i, j, 2]
            Y = (75/256)*R + (150/256)*G + (29/256)*B
            Cb = -(44/256)*R - (87/256)*G + (131/256)*B + 128
            Cr = (131/256)*R - (110/256)*G - (21/256)*B + 128
            imagenY[i, j] = Y
            imagenCb[i, j] = Cb
            imagenCr[i, j] = Cr
    return imagenY, imagenCb, imagenCr

def aplicar2DCT_Y(imagen, bloques):
    for i in range(bloques):
        imagen[i]=dct_bloque(imagen[i])
    for i in range(bloques):
        for j in range(8):
            for k in range(8):
                imagen[i, j, k] /= Q_Luminance[j, k]
                imagen[i, j, k] = round(imagen[i, j, k], 0)
                
def aplicar2DCT_Cb(imagen, bloques):
    Q = Q_matrix()
    for i in range(bloques):
        imagen[i]=dct_bloque(imagen[i])
    for i in range(bloques):
        for j in range(8):
            for k in range(8):
                imagen[i, j, k] /= Q[j, k]
                imagen[i, j, k] = round(imagen[i, j, k], 0)
                
def aplicar2DCT_Cr(imagen, bloques):
    for i in range(bloques):
        imagen[i]=dct_bloque(imagen[i])
    for i in range(bloques):
        for j in range(8):
            for k in range(8):
                imagen[i, j, k] /= Q_Chrominance[j, k]
                imagen[i, j, k] = round(imagen[i, j, k], 0)
    
    
"""
Descompresion
"""

def ycbcr2rgb(imagenY, imagenCb, imagenCr, fil, col, color):
    imagen = np.zeros((fil, col, color))
    for i in range(fil):
        for j in range(col):
            Y = imagenY[i, j]
            Cb = imagenCb[i, j]
            Cr = imagenCr[i, j]
            R = Y + (1.371*(Cr - 128))
            G = Y - (0.698*(Cr - 128)) - (0.336*(Cb - 128))
            B = Y + (1.732*(Cb - 128))
            imagen[i, j, 0] = R
            imagen[i, j, 1] = G
            imagen[i, j, 2] = B
    return imagen

def aplicar2IDCT_Y(imagen, bloques):
    for i in range(bloques):
        for j in range(8):
            for k in range(8):
                imagen[i, j, k] *= Q_Luminance[j, k]
                imagen[i, j, k] = round(imagen[i, j, k], 0)
    for i in range(bloques):
        imagen[i]=idct_bloque(imagen[i])
    imagen += 128
        
def aplicar2IDCT_Cb(imagen, bloques):
    Q = Q_matrix()
    for i in range(bloques):
        for j in range(8):
            for k in range(8):
                imagen[i, j, k] *= Q[j, k]
                imagen[i, j, k] = round(imagen[i, j, k], 0)
    for i in range(bloques):
        imagen[i]=idct_bloque(imagen[i])
    imagen += 128
        
def aplicar2IDCT_Cr(imagen, bloques):
    for i in range(bloques):
        for j in range(8):
            for k in range(8):
                imagen[i, j, k] *= Q_Chrominance[j, k]
                imagen[i, j, k] = round(imagen[i, j, k], 0)
    for i in range(bloques):
        imagen[i]=idct_bloque(imagen[i])
    imagen += 128

def ratio2(fil, col, color, imagenY, imagenCb, imagenCr):
    coef_nulo = (imagenY == 0).sum() + (imagenCb == 0).sum() + (imagenCr == 0).sum()
    return (fil*col*color)/((fil*col*color) - coef_nulo)

def jpeg_color(imagen_color):
    fil, col, color = imagen_color.shape
    
    """
    COMPRESION
    Pasar de rgb a ycbcr
    """
    y, cb, cr = rgb2ycbcr(imagen_color)
    
    """
    Hacer particiones 8x8
    """
    bloquesY = np.subtract(dividirBloques(fil, col, y), 128)
    bloquesCb = np.subtract(dividirBloques(fil, col, cb), 128)
    bloquesCr = np.subtract(dividirBloques(fil, col, cr), 128)
    
    """
    Aplicar 2-DCT
    """
    bloques = (fil*col)//(8*8)
    
    aplicar2DCT_Y(bloquesY, bloques)
    aplicar2DCT_Cb(bloquesCb, bloques)
    aplicar2DCT_Cr(bloquesCr, bloques)
    
    """
    Ratio
    """
    
    r = ratio2(fil, col, color, bloquesY, bloquesCb, bloquesCr)
    
    """
    DECOMPRESION
    Aplicar 2-IDCT
    """    
    aplicar2IDCT_Y(bloquesY, bloques)
    aplicar2IDCT_Cb(bloquesCb, bloques)
    aplicar2IDCT_Cr(bloquesCr, bloques)
    
    """
    Juntar bloques
    """
    bloquesY = juntarBloques(fil, col, bloquesY)
    bloquesCb = juntarBloques(fil, col, bloquesCb)
    bloquesCr = juntarBloques(fil, col, bloquesCr)
    
    """
    Pasar de ycbcr a rgb
    """
    imagen_jpeg = ycbcr2rgb(bloquesY, bloquesCb, bloquesCr, fil, col, color).astype(np.uint8)
    
    """
    Error
    """
    imagen_error = imagen_jpeg[::]
    imagen_error = imagen_error.astype(np.int64)
    sigma=np.sqrt(sum(sum((imagen_color-imagen_error)**2)))/np.sqrt(sum(sum((imagen_color)**2)))
    
    return r, sigma, imagen_jpeg
    
    
    
   
"""
#--------------------------------------------------------------------------
Imagen de GRISES

#--------------------------------------------------------------------------
"""


### .astype es para que lo lea como enteros de 32 bits, si no se
### pone lo lee como entero positivo sin signo de 8 bits uint8 y por ejemplo al 
### restar 128 puede devolver un valor positivo mayor que 128


mandril_gray=scipy.ndimage.imread('mandril_gray.png').astype(np.int32)

start= time.clock()
r, sigma, mandril_jpeg=jpeg_gris(mandril_gray)  
fig = plt.figure()
plt.imshow(mandril_jpeg, cmap=plt.cm.gray) 
plt.xticks([])
plt.yticks([])
plt.show() 
end= time.clock()
print('\n')
print("Error:", sigma)
print("Ratio:", r)
print("Tiempo",(end-start))


"""
#--------------------------------------------------------------------------
Imagen COLOR
#--------------------------------------------------------------------------
"""
## Aplico.astype pero después lo convertiré a 
## uint8 para dibujar y a int64 para calcular el error

mandril_color=scipy.misc.imread('./mandril_color.png').astype(np.int32)

start= time.clock()
r, sigma, mandril_jpeg=jpeg_color(mandril_color)   
fig = plt.figure()
plt.imshow(mandril_jpeg) 
plt.xticks([])
plt.yticks([])
plt.show() 
end= time.clock()
print('\n')
print("Error:", sigma)
print("Ratio:", r)
print("Tiempo",(end-start))
       









