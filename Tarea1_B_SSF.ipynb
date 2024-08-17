# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 00:54:43 2024

@author: luish
"""
import math
import pandas as pd
import matplotlib.pyplot as plt

def cos_taylor_series(x, tolerancia, max_iteraciones=120):
    termi = 1  # Primer término de la serie (n=0), que es 1
    sum_series = termi  # Inicializa la suma con el primer término
    cos_exact = math.cos(x)  # Calcula el valor exacto de cos(x) usando la función de Python
    iteraciones = []  # Lista para almacenar los resultados de cada iteración

    # Ciclo para calcular los términos de la serie de Taylor hasta que converja o se 
    # alcance el máximo de iteraciones
    for n in range(1, max_iteraciones + 1):
        # Calcula el siguiente término de la serie de Taylor
        termi *= -x**2 / (2*n * (2*n - 1))
        sum_series += termi  # Suma el término a la serie parcial
        # Calcula el error relativo comparando con el valor exacto de cos(x)
        error_relativo = abs(sum_series - cos_exact) / abs(cos_exact)
        # Almacena los resultados de esta iteración
        iteraciones.append((x, n, sum_series, error_relativo))
        # Si el error relativo es menor que la tolerancia, se detiene la iteración
        if error_relativo < tolerancia:
            break
    
    return iteraciones  # Retorna los resultados de todas las iteraciones

def create_comparison_table(x_valores, tolerancia, max_iteraciones=120):
    todas_iteraciones = []  # Lista para almacenar los resultados de todas las series
    # Para cada valor de x, calcula la serie de Taylor y almacena los resultados
    for x in x_valores:
        iteraciones = cos_taylor_series(x, tolerancia, max_iteraciones)
        todas_iteraciones.extend(iteraciones)
    
    # Crea un DataFrame con los resultados y columnas específicas
    df = pd.DataFrame(todas_iteraciones, columns=['x', 'Iteración', 'Suma', 'Error Relativo'])
    return df  # Retorna la tabla de comparación

# Valores de x para evaluar
x_valores = [1, 10, 100, 120]

## Tablas de comparación

# Tolerancia 10^-4
df_1e4 = create_comparison_table(x_valores, 1e-4)
print("Resultados con Tolerancia 10^-4")
print(df_1e4)  # Muestra los resultados en consola

# Tolerancia 10^-8
df_1e8 = create_comparison_table(x_valores, 1e-8)
print("\nResultados con Tolerancia 10^-8")
print(df_1e8)  # Muestra los resultados en consola



def plot_convergence(x_values, tolerancia, max_iteraciones=120):
    plt.figure(figsize=(12, 8))  # Crea una figura de tamaño específico

    # Para cada valor de x, calcula los errores relativos y los grafica
    for x in x_values:
        iteraciones = cos_taylor_series(x, tolerancia, max_iteraciones)
        iter_nums = [iter[1] for iter in iteraciones]  # Número de iteración
        errors = [iter[3] for iter in iteraciones]  # Error relativo
        plt.plot(iter_nums, errors, label=f"x={x}")  # Grafica error relativo vs iteraciones

    plt.yscale('log')  # Escala logarítmica para el eje Y (error relativo). Para mejor visualización
    plt.xlabel('Iteración')  # Etiqueta del eje X
    plt.ylabel('Error Relativo')  # Etiqueta del eje Y
    plt.title(f'Convergencia de la Serie de Taylor para cos(x) con Tolerancia {tolerancia}')  # Título de la gráfica
    plt.legend()  # Muestra la leyenda con los valores de x
    plt.xlim(0, 120)  # Limita el eje X para ver mejor la convergencia
    plt.grid(True, which='both', linestyle=':', linewidth=0.5)  # Activa la cuadrícula en ambos ejes
    plt.show()  # Muestra la gráfica

# Gráfica de convergencia con Tolerancia 10^-4
print("Gráfica de convergencia con Tolerancia 10^-4")
plot_convergence(x_valores, 1e-4)

# Gráfica de convergencia con Tolerancia 10^-8
print("\nGráfica de convergencia con Tolerancia 10^-8")
plot_convergence(x_valores, 1e-8)
