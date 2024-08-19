# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:48:14 2024

@author: luish
"""

import matplotlib.pyplot as plt
import numpy as np

# Cargamos los datos
data = np.loadtxt("altura6.dat", float)

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
