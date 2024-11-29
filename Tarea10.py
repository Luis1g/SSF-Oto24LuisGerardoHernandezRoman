# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:47:22 2024

@author: luish
"""

# Ejemplo 6.1.1
from random import random 
from math import sqrt

N = 1000000
count = 0
for j in range(N):
    point = (random(), random(), random())
    if point[0]*point[0]+point[1]*point[1]+point[2]*point[2]<1:
        count = count+1
Answer = float(count)/float(N)
Answer = Answer * 4

print('''The volume of a hemisphere of radius 1 is %0.4f +/- %0.4f.'''%(Answer, 4*sqrt(N)/float(N)))

# In[1] Problema 6.0

from random import random
from math import sin, sqrt, pi

N = 1000000  # Número de puntos

# Contador para el promedio acumulado de sin(x)
sum_values = 0

# Generar puntos aleatorios y calcular sin(x)
for _ in range(N):
    x = random() * pi  # x en el intervalo [0, pi]
    sum_values += sin(x)  # Acumular sin(x)

# Calcular el valor promedio de sin(x)
average_value = sum_values / N

# Escalar por el rango de integración (pi - 0)
result = pi * average_value

# Calcular la incertidumbre (desviación estándar)
uncertainty = pi / sqrt(N)  # Incertidumbre típica para Monte Carlo

print('''La integral de sin(x) de 0 a es %0.4f +/- %0.4f.''' % (result, uncertainty))

# In[2] Problema 6.2
from random import random
from math import sqrt, pi

# Número de puntos para Monte Carlo
N = 1000000

# Contador de puntos dentro de la 4-esfera
count_inside = 0

# Generar puntos aleatorios en 4 dimensiones
for _ in range(N):
    x, y, z, w = random(), random(), random(), random()  # Coordenadas en [0,1)
    if x**2 + y**2 + z**2 + w**2 <= 1:
        count_inside += 1

# Volumen estimado de la 4-esfera de radio 1
volume_4sphere = (2**4) * (count_inside / N)  # Escala por el volumen del hipercubo [0,2]^4

# Relación entre volumen y alpha
alpha = volume_4sphere / pi

# Incertidumbre (estimación del error estándar)
uncertainty = (2**4) * sqrt(count_inside * (N - count_inside)) / (N * sqrt(N))

print('''El valor estimado de alpha es  %0.4f +/- %0.4f.''' % (alpha, uncertainty))

