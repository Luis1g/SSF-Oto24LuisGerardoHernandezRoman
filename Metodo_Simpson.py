# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:52:11 2024

@author: luish
"""
from numpy import *
import numpy as np

# Definición de la función a integrar
def f(x):
    return (exp((-x**2)/2)/np.sqrt(2*pi))  # Ejemplo de función

# Implementación del método de Simpson
def simpson(f, a, b, n):
    """
    Calcular la integral de la función f en el intervalo [a, b] usando el método de Simpson.

    :param f: Función a integrar
    :param a: Límite inferior de integración
    :param b: Límite superior de integración
    :param n: Número de subintervalos (debe ser par)
    :return: Aproximación de la integral de f desde a hasta b
    """
    # Verificar que n es par
    if n % 2 == 1:
        raise ValueError("El número de subintervalos 'n' debe ser par.")

    h = (b - a) / n  # Ancho de cada subintervalo
    x = np.linspace(a, b, n + 1)  # Puntos de evaluación
    fx = f(x)  # Evaluación de la función en los puntos

    # Aplicación de la fórmula de Simpson
    integral = fx[0] + fx[-1] + 4 * np.sum(fx[1:-1:2]) + 2 * np.sum(fx[2:-2:2])
    integral *= h / 3

    return integral

# Definición de los límites de integración y el número de subintervalos
a = -1.0  # Límite inferior
b = 1.0  # Límite superior
n = 6   # Número de subintervalos (debe ser par)

# Cálculo de la integral usando el método de Simpson
result = simpson(f, a, b, n)
print("Resultado de la integral con el método de Simpson =", result)

#####################################################################################################

# Definición de la función a integrar
def f(x):
    return (exp((-x**2)/2)/np.sqrt(2*pi))  # Ejemplo de función

# Implementación del método de Simpson
def simpson(f, a, b, n):
    """
    Calcular la integral de la función f en el intervalo [a, b] usando el método de Simpson.

    :param f: Función a integrar
    :param a: Límite inferior de integración
    :param b: Límite superior de integración
    :param n: Número de subintervalos (debe ser par)
    :return: Aproximación de la integral de f desde a hasta b
    """
    # Verificar que n es par
    if n % 2 == 1:
        raise ValueError("El número de subintervalos 'n' debe ser par.")

    h = (b - a) / n  # Ancho de cada subintervalo
    x = np.linspace(a, b, n + 1)  # Puntos de evaluación
    fx = f(x)  # Evaluación de la función en los puntos

    # Aplicación de la fórmula de Simpson
    integral = fx[0] + fx[-1] + 4 * np.sum(fx[1:-1:2]) + 2 * np.sum(fx[2:-2:2])
    integral *= h / 3

    return integral

# Definición de los límites de integración y el número de subintervalos
a = -1.0  # Límite inferior
b = 1.0  # Límite superior
n = 16   # Número de subintervalos (debe ser par)

# Cálculo de la integral usando el método de Simpson
result = simpson(f, a, b, n)
print("Resultado de la integral con el método de Simpson =", result)

###################################################################################


import numpy as np

# Definición de la función a integrar
def f(x):
    return (exp(x) * sin(x)) / (1 + x**2)  # Ejemplo de función

# Implementación del método de Simpson
def simpson(f, a, b, n):
    """
    Calcula la integral de la función f en el intervalo [a, b] usando el método de Simpson.

    :param f: Función a integrar
    :param a: Límite inferior de integración
    :param b: Límite superior de integración
    :param n: Número de subintervalos (debe ser par)
    :return: Aproximación de la integral de f desde a hasta b
    """
    # Verificar que n es par
    if n % 2 == 1:
        raise ValueError("El número de subintervalos 'n' debe ser par.")

    h = (b - a) / n  # Ancho de cada subintervalo
    x = np.linspace(a, b, n + 1)  # Puntos de evaluación
    fx = f(x)  # Evaluación de la función en los puntos

    # Aplicación de la fórmula de Simpson
    integral = fx[0] + fx[-1] + 4 * np.sum(fx[1:-1:2]) + 2 * np.sum(fx[2:-2:2])
    integral *= h / 3

    return integral

# Definición de los límites de integración y el número de subintervalos
a = 0.0  # Límite inferior
b = 3.0  # Límite superior
n = 6   # Número de subintervalos (debe ser par)

# Cálculo de la integral usando el método de Simpson
result = simpson(f, a, b, n)
print("Resultado de la integral con el método de Simpson =", result)


######################################################################################

# Definición de la función a integrar
def f(x):
    return (exp(x) * sin(x)) / (1 + x**2)  # Ejemplo de función

# Implementación del método de Simpson
def simpson(f, a, b, n):
    """
    Calcula la integral de la función f en el intervalo [a, b] usando el método de Simpson.

    :param f: Función a integrar
    :param a: Límite inferior de integración
    :param b: Límite superior de integración
    :param n: Número de subintervalos (debe ser par)
    :return: Aproximación de la integral de f desde a hasta b
    """
    # Verificar que n es par
    if n % 2 == 1:
        raise ValueError("El número de subintervalos 'n' debe ser par.")

    h = (b - a) / n  # Ancho de cada subintervalo
    x = np.linspace(a, b, n + 1)  # Puntos de evaluación
    fx = f(x)  # Evaluación de la función en los puntos

    # Aplicación de la fórmula de Simpson
    integral = fx[0] + fx[-1] + 4 * np.sum(fx[1:-1:2]) + 2 * np.sum(fx[2:-2:2])
    integral *= h / 3

    return integral

# Definición de los límites de integración y el número de subintervalos
a = 0.0  # Límite inferior
b = 3.0  # Límite superior
n = 16   # Número de subintervalos (debe ser par)

# Cálculo de la integral usando el método de Simpson
result = simpson(f, a, b, n)
print("Resultado de la integral con el método de Simpson =", result)
