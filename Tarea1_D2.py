# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:49:31 2024

@author: luish
"""

import matplotlib.pyplot as plt
import numpy as np

# Genera 10000 datos aleatorios 
data = np.random.randn(10000)

# Escalar los datos para que estén dentro del rango deseado 1.60 y 1.80
media = 1.70
Desv_Estan = 0.05
data = media + Desv_Estan * data  # Ahora los datos tendrán una media de 1.70 y estarán en un rango aproximado de 1.60 a 1.80

# Se calcula la media y la desviacion estandar
media = np.mean(data)
Desv_Estan = np.std(data)

# Creamos el histograma
plt.hist(data, bins=10, edgecolor='black', alpha=0.7)

# Se dibuja la línea de la media
plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media: {media:.2f}')

# Se dibujan las líneas de la desviación estándar
plt.axvline(media - Desv_Estan, color='blue', linestyle='dashed', linewidth=2, label=f'-1σ: {media - Desv_Estan:.2f}')
plt.axvline(media + Desv_Estan, color='blue', linestyle='dashed', linewidth=2, label=f'+1σ: {media + Desv_Estan:.2f}')

# Etiquetas y título
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma con Media y Desviación Estándar')

# Para agregar las etiquetas
plt.legend()

# Mostramos el histograma
plt.show()
