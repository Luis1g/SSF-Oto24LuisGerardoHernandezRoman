# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:04:24 2024

@author: luish
"""
import numpy as np

# Configuración de la simulación
num_alumnos = 100   # 100 alumnos por curso
num_cursos = 10     # 10 cursos

# Inicialización de listas para almacenar resultados de cada curso
promedios = []
varianzas = []

# Simulación de calificaciones y cálculo de promedio y varianza para cada curso
for _ in range(num_cursos):
    calificaciones = np.random.randint(5, 11, num_alumnos)  # Calificaciones aleatorias entre 5 y 10
    promedio = np.mean(calificaciones)                      # Promedio
    varianza = np.var(calificaciones, ddof=1)               # Varianza (muestral)
    
    promedios.append(promedio)
    varianzas.append(varianza)

# Cálculo del promedio y desviación estándar de los promedios de los 10 cursos
promedio_final = np.mean(promedios)
desviacion_estandar = np.std(promedios, ddof=1)

promedios, varianzas, promedio_final, desviacion_estandar
