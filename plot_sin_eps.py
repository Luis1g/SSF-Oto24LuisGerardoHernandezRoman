# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:29:17 2024

@author: luish
"""
import numpy as np
import matplotlib.pyplot as plt

def graficar_funcion(epsilon, n):
    # Se definen los nodos en el intervalo [0, 1]
    x = np.linspace(0, 1, n + 1)
    
    # Se define la función f(x) = sin(1 / (x + epsilon))
    # Evitamos la singularidad en x = -epsilon al agregar un valor muy pequeño a epsilon
    f = np.sin(1 / (x + epsilon))
    
    # Se crea la gráfica
    plt.plot(x, f, label=r'$f(x) = \sin\left(\frac{1}{x + \epsilon}\right)$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Gráfica de f(x) con ε = {epsilon} y n = {n}')
    plt.grid(True)
    plt.legend()
    plt.show()
ε=0.1
n=100

graficar_funcion(1/5, 100)

###############################################################################

def graficar_funcion_seno_doble(ε, n):
    x_n = np.linspace(0, 1, n + 1)
    x_n10 = np.linspace(0, 1, n + 11)
    
    # Calculamos f(x) = sin(1 / (x + ε)) para ambos conjuntos de nodos
    y_n = np.sin(1 / (x_n + ε))
    y_n10 = np.sin(1 / (x_n10 + ε))
    
    # Graficamos ambas funciones
    plt.plot(x_n, y_n, marker='o', label=f'n = {n}')
    plt.plot(x_n10, y_n10, marker='x', label=f'n = {n + 10}')
    plt.xlabel('x')
    plt.ylabel('f(x) = sin(1 / (x + ε))')
    plt.title(f'Gráfica de f(x) = sin(1 / (x + ε)), con ε = {ε}')
    plt.grid(True)
    plt.legend()
    plt.show()

# Parámetros de entrada
ε = 0.01
n = 100

graficar_funcion_seno_doble(ε, n)

###############################################################################



def graficar_funcion_seno_doble(ε, n):
    x_n = np.linspace(0, 1, n + 1)
    x_n10 = np.linspace(0, 1, n + 11)
    
    # Calculamos f(x) = sin(1 / (x + ε)) para ambos conjuntos de nodos
    y_n = np.sin(1 / (x_n + ε))
    y_n10 = np.sin(1 / (x_n10 + ε))
    
    # Graficamos ambas funciones
    plt.plot(x_n, y_n, marker='o', label=f'n = {n}')
    plt.plot(x_n10, y_n10, marker='x', label=f'n = {n + 10}')
    plt.xlabel('x')
    plt.ylabel('f(x) = sin(1 / (x + ε))')
    plt.title(f'Gráfica de f(x) = sin(1 / (x + ε)), con ε = {ε}')
    plt.grid(True)
    plt.legend()
    plt.show()

def encontrar_n(ε):
    n = 1  # Iniciamos con n = 1
    diferencia_maxima = float('inf')  # Inicializamos con un valor grande
    
    while diferencia_maxima >= 0.1:
        # Definir nodos y calcular la función para n y n + 10
        x_n = np.linspace(0, 1, n + 1)
        x_n10 = np.linspace(0, 1, n + 11)
        
        y_n = np.sin(1 / (x_n + ε))
        y_n10 = np.sin(1 / (x_n10 + ε))
        
        # Redimensionamos la función de n+10 a n usando slicing (solo los primeros n+1 valores)
        diferencia_maxima = np.max(np.abs(y_n - y_n10[:n+1]))

        if diferencia_maxima >= 0.1:
            n += 1

    return n

# Parámetros de entrada
ε = 1/20
n = encontrar_n(ε)

print(f"El valor mínimo de n para que la diferencia sea menor que 0.1 es: {n}")

# Graficar para el valor de n encontrado
graficar_funcion_seno_doble(ε, n)
