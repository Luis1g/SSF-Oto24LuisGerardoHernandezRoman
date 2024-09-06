# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:55:38 2024

@author: luish
"""
from numpy import *
import numpy as np
from sys import version
import math
from scipy.integrate import quad
# Definición de parámetros iniciales
max_in = 6  # Número máximo de intervalos para la integración
vmin = -1.0  # Valor mínimo del rango de integración
vmax = 1.0  # Valor máximo del rango de integración

# Inicialización de arrays para almacenar los puntos de integración (x) y los pesos (w)
w = zeros((2001), float)  # Array de pesos de la cuadratura de Gauss
x = zeros((2001), float)  # Array de puntos de la cuadratura de Gauss

# Definición de la función a integrar: f(x) = e^(-x)
def f(x):
    return (exp((-x**2)/2)/np.sqrt(2*pi))

# Función para calcular los puntos y pesos de la cuadratura de Gauss
def gauss(npts, job, a, b, x, w):
    m = i = j = t = t1 = pp = p1 = p2 = p3 = 0.0
    eps = 3E-14  # Precisión deseada para el cálculo de los puntos y pesos
    m = int((npts + 1) / 2)  # Número de puntos necesarios

    # Bucle para calcular los puntos y pesos usando la fórmula de Gauss-Legendre
    for i in range(1, m + 1):
        # Estimación inicial del punto usando la aproximación coseno
        t = cos(math.pi * (float(i) - 0.25) / (float(npts) + 0.5))
        t1 = 1.0  # Inicialización para el bucle iterativo
        
        # Bucle iterativo para refinar la estimación de los puntos
        while (abs(t - t1) >= eps):
            p1 = 1.0  # Inicialización del polinomio de Legendre
            p2 = 0.0
            for j in range(1, npts + 1):
                p3 = p2  # Cambio de valores anteriores
                p2 = p1
                # Calculo del valor actual del polinomio de Legendre
                p1 = ((2.0 * float(j) - 1) * t * p2 - (float(j) - 1.0) * p3) / float(j)
            
            # Derivada del polinomio de Legendre en el punto t
            pp = npts * (t * p1 - p2) / (t * t - 1.0)
            t1 = t  # Almacena el valor previo
            t = t1 - p1 / pp  # Nuevo valor de t usando el método de Newton-Raphson
        
        # Asignación de los puntos de integración y sus simétricos
        x[i - 1] = -t
        x[npts - i] = t

        # Cálculo de los pesos asociados a los puntos
        w[i - 1] = 2.0 / ((1.0 - t * t) * pp * pp)
        w[npts - i] = w[i - 1]

    # Ajuste de los puntos y pesos según el tipo de intervalo (job)
    if (job == 0):  # Intervalo estándar (a, b)
        for i in range(0, npts):
            x[i] = x[i] * (b - a) / 2.0 + (b + a) / 2.0  # Escalamiento de los puntos
            w[i] = w[i] * (b - a) / 2.0  # Escalamiento de los pesos
    elif (job == 1):  # Intervalo (a, inf)
        for i in range(0, npts):
            xi = x[i]
            x[i] = a * b * (1.0 + xi) / (b + a - (b - a) * xi)
            w[i] = w[i] * 2.0 * a * b * b / ((b + a - (b - a) * xi) ** 2)
    elif (job == 2):  # Intervalo (-inf, inf)
        for i in range(0, npts):
            xi = x[i]
            x[i] = (b * xi + b + a + a) / (1.0 - xi)
            w[i] = w[i] * 2.0 * (a + b) / ((1.0 - xi) ** 2)

# Función para realizar la integración usando los puntos y pesos calculados
def gaussint(no, min, max):
    quadra = 0.0  # Inicialización del valor de la integral
    gauss(no, 0, min, max, x, w)  # Llama a la función gauss para obtener los puntos y pesos

    # Calcula la integral sumando la función evaluada en los puntos por sus respectivos pesos
    for n in range(0, no):
        quadra += f(x[n]) * w[n]
    return quadra  # Devuelve el valor calculado de la integral

# Realiza la integral
result = gaussint(max_in, vmin, vmax)  # Calcula la integral con i puntos
print("Resultado de la integral=", result)  # Mensaje final al usuario

## Calcula el valor de referencia usando la función de integración numérica de scipy
ref_value, _ = quad(f, vmin, vmax)
print("Valor de referencia de la integral con scipy =", ref_value)

# Calcula el error absoluto
error_abs = abs(result - ref_value)
print("Error absoluto =", error_abs)

# Calcula el error relativo
error_rel = error_abs / abs(ref_value)
print("Error relativo =", error_rel)

########################################################################################
# Definición de parámetros iniciales
max_in = 15  # Número máximo de intervalos para la integración
vmin = -1.0  # Valor mínimo del rango de integración
vmax = 1.0  # Valor máximo del rango de integración

# Inicialización de arrays para almacenar los puntos de integración (x) y los pesos (w)
w = zeros((2001), float)  # Array de pesos de la cuadratura de Gauss
x = zeros((2001), float)  # Array de puntos de la cuadratura de Gauss

# Definición de la función a integrar: f(x) = e^(-x)
def f(x):
    return (exp((-x**2)/2)/np.sqrt(2*pi))

# Función para calcular los puntos y pesos de la cuadratura de Gauss
def gauss(npts, job, a, b, x, w):
    m = i = j = t = t1 = pp = p1 = p2 = p3 = 0.0
    eps = 3E-14  # Precisión deseada para el cálculo de los puntos y pesos
    m = int((npts + 1) / 2)  # Número de puntos necesarios

    # Bucle para calcular los puntos y pesos usando la fórmula de Gauss-Legendre
    for i in range(1, m + 1):
        # Estimación inicial del punto usando la aproximación coseno
        t = cos(math.pi * (float(i) - 0.25) / (float(npts) + 0.5))
        t1 = 1.0  # Inicialización para el bucle iterativo
        
        # Bucle iterativo para refinar la estimación de los puntos
        while (abs(t - t1) >= eps):
            p1 = 1.0  # Inicialización del polinomio de Legendre
            p2 = 0.0
            for j in range(1, npts + 1):
                p3 = p2  # Cambio de valores anteriores
                p2 = p1
                # Calculo del valor actual del polinomio de Legendre
                p1 = ((2.0 * float(j) - 1) * t * p2 - (float(j) - 1.0) * p3) / float(j)
            
            # Derivada del polinomio de Legendre en el punto t
            pp = npts * (t * p1 - p2) / (t * t - 1.0)
            t1 = t  # Almacena el valor previo
            t = t1 - p1 / pp  # Nuevo valor de t usando el método de Newton-Raphson
        
        # Asignación de los puntos de integración y sus simétricos
        x[i - 1] = -t
        x[npts - i] = t

        # Cálculo de los pesos asociados a los puntos
        w[i - 1] = 2.0 / ((1.0 - t * t) * pp * pp)
        w[npts - i] = w[i - 1]

    # Ajuste de los puntos y pesos según el tipo de intervalo (job)
    if (job == 0):  # Intervalo estándar (a, b)
        for i in range(0, npts):
            x[i] = x[i] * (b - a) / 2.0 + (b + a) / 2.0  # Escalamiento de los puntos
            w[i] = w[i] * (b - a) / 2.0  # Escalamiento de los pesos
    elif (job == 1):  # Intervalo (a, inf)
        for i in range(0, npts):
            xi = x[i]
            x[i] = a * b * (1.0 + xi) / (b + a - (b - a) * xi)
            w[i] = w[i] * 2.0 * a * b * b / ((b + a - (b - a) * xi) ** 2)
    elif (job == 2):  # Intervalo (-inf, inf)
        for i in range(0, npts):
            xi = x[i]
            x[i] = (b * xi + b + a + a) / (1.0 - xi)
            w[i] = w[i] * 2.0 * (a + b) / ((1.0 - xi) ** 2)

# Función para realizar la integración usando los puntos y pesos calculados
def gaussint(no, min, max):
    quadra = 0.0  # Inicialización del valor de la integral
    gauss(no, 0, min, max, x, w)  # Llama a la función gauss para obtener los puntos y pesos

    # Calcula la integral sumando la función evaluada en los puntos por sus respectivos pesos
    for n in range(0, no):
        quadra += f(x[n]) * w[n]
    return quadra  # Devuelve el valor calculado de la integral

# Realiza la integral
result = gaussint(max_in, vmin, vmax)  # Calcula la integral con i puntos
print("Resultado de la integral=", result)  # Mensaje final al usuario

## Calcula el valor de referencia usando la función de integración numérica de scipy
ref_value, _ = quad(f, vmin, vmax)
print("Valor de referencia de la integral con scipy =", ref_value)

# Calcula el error absoluto
error_abs = abs(result - ref_value)
print("Error absoluto =", error_abs)

# Calcula el error relativo
error_rel = error_abs / abs(ref_value)
print("Error relativo =", error_rel)

########################################################################################

from numpy import *
from sys import version
import math
from scipy.integrate import quad
# Definición de parámetros iniciales
max_in = 6  # Número máximo de intervalos para la integración
vmin = 0.0  # Valor mínimo del rango de integración
vmax = 3.0  # Valor máximo del rango de integración

# Inicialización de arrays para almacenar los puntos de integración (x) y los pesos (w)
w = zeros((2001), float)  # Array de pesos de la cuadratura de Gauss
x = zeros((2001), float)  # Array de puntos de la cuadratura de Gauss

# Definición de la función a integrar: f(x) = e^(-x)
def f(x):
    return (exp(x)*sin(x))/(1+x**2)

# Función para calcular los puntos y pesos de la cuadratura de Gauss
def gauss(npts, job, a, b, x, w):
    m = i = j = t = t1 = pp = p1 = p2 = p3 = 0.0
    eps = 3E-14  # Precisión deseada para el cálculo de los puntos y pesos
    m = int((npts + 1) / 2)  # Número de puntos necesarios

    # Bucle para calcular los puntos y pesos usando la fórmula de Gauss-Legendre
    for i in range(1, m + 1):
        # Estimación inicial del punto usando la aproximación coseno
        t = cos(math.pi * (float(i) - 0.25) / (float(npts) + 0.5))
        t1 = 1.0  # Inicialización para el bucle iterativo
        
        # Bucle iterativo para refinar la estimación de los puntos
        while (abs(t - t1) >= eps):
            p1 = 1.0  # Inicialización del polinomio de Legendre
            p2 = 0.0
            for j in range(1, npts + 1):
                p3 = p2  # Cambio de valores anteriores
                p2 = p1
                # Calculo del valor actual del polinomio de Legendre
                p1 = ((2.0 * float(j) - 1) * t * p2 - (float(j) - 1.0) * p3) / float(j)
            
            # Derivada del polinomio de Legendre en el punto t
            pp = npts * (t * p1 - p2) / (t * t - 1.0)
            t1 = t  # Almacena el valor previo
            t = t1 - p1 / pp  # Nuevo valor de t usando el método de Newton-Raphson
        
        # Asignación de los puntos de integración y sus simétricos
        x[i - 1] = -t
        x[npts - i] = t

        # Cálculo de los pesos asociados a los puntos
        w[i - 1] = 2.0 / ((1.0 - t * t) * pp * pp)
        w[npts - i] = w[i - 1]

    # Ajuste de los puntos y pesos según el tipo de intervalo (job)
    if (job == 0):  # Intervalo estándar (a, b)
        for i in range(0, npts):
            x[i] = x[i] * (b - a) / 2.0 + (b + a) / 2.0  # Escalamiento de los puntos
            w[i] = w[i] * (b - a) / 2.0  # Escalamiento de los pesos
    elif (job == 1):  # Intervalo (a, inf)
        for i in range(0, npts):
            xi = x[i]
            x[i] = a * b * (1.0 + xi) / (b + a - (b - a) * xi)
            w[i] = w[i] * 2.0 * a * b * b / ((b + a - (b - a) * xi) ** 2)
    elif (job == 2):  # Intervalo (-inf, inf)
        for i in range(0, npts):
            xi = x[i]
            x[i] = (b * xi + b + a + a) / (1.0 - xi)
            w[i] = w[i] * 2.0 * (a + b) / ((1.0 - xi) ** 2)
            
           
# Función para realizar la integración usando los puntos y pesos calculados
def gaussint(no, min, max):
    quadra = 0.0  # Inicialización del valor de la integral
    gauss(no, 0, min, max, x, w)  # Llama a la función gauss para obtener los puntos y pesos

    # Calcula la integral sumando la función evaluada en los puntos por sus respectivos pesos
    for n in range(0, no):
        quadra += f(x[n]) * w[n]
    return quadra  # Devuelve el valor calculado de la integral

# Realiza la integral
result = gaussint(max_in, vmin, vmax)  # Calcula la integral con i puntos
print("Resultado de la integral=", result)  # Mensaje final al usuario

## Calcula el valor de referencia usando la función de integración numérica de scipy
ref_value, _ = quad(f, vmin, vmax)
print("Valor de referencia de la integral con scipy =", ref_value)

# Calcula el error absoluto
error_abs = abs(result - ref_value)
print("Error absoluto =", error_abs)

# Calcula el error relativo
error_rel = error_abs / abs(ref_value)
print("Error relativo =", error_rel)

#####################################################################################################


from numpy import *
from sys import version
import math
from scipy.integrate import quad
# Definición de parámetros iniciales
max_in = 15  # Número máximo de intervalos para la integración
vmin = 0.0  # Valor mínimo del rango de integración
vmax = 3.0  # Valor máximo del rango de integración

# Inicialización de arrays para almacenar los puntos de integración (x) y los pesos (w)
w = zeros((2001), float)  # Array de pesos de la cuadratura de Gauss
x = zeros((2001), float)  # Array de puntos de la cuadratura de Gauss

# Definición de la función a integrar: f(x) = e^(-x)
def f(x):
    return (exp(x)*sin(x))/(1+x**2)

# Función para calcular los puntos y pesos de la cuadratura de Gauss
def gauss(npts, job, a, b, x, w):
    m = i = j = t = t1 = pp = p1 = p2 = p3 = 0.0
    eps = 3E-14  # Precisión deseada para el cálculo de los puntos y pesos
    m = int((npts + 1) / 2)  # Número de puntos necesarios

    # Bucle para calcular los puntos y pesos usando la fórmula de Gauss-Legendre
    for i in range(1, m + 1):
        # Estimación inicial del punto usando la aproximación coseno
        t = cos(math.pi * (float(i) - 0.25) / (float(npts) + 0.5))
        t1 = 1.0  # Inicialización para el bucle iterativo
        
        # Bucle iterativo para refinar la estimación de los puntos
        while (abs(t - t1) >= eps):
            p1 = 1.0  # Inicialización del polinomio de Legendre
            p2 = 0.0
            for j in range(1, npts + 1):
                p3 = p2  # Cambio de valores anteriores
                p2 = p1
                # Calculo del valor actual del polinomio de Legendre
                p1 = ((2.0 * float(j) - 1) * t * p2 - (float(j) - 1.0) * p3) / float(j)
            
            # Derivada del polinomio de Legendre en el punto t
            pp = npts * (t * p1 - p2) / (t * t - 1.0)
            t1 = t  # Almacena el valor previo
            t = t1 - p1 / pp  # Nuevo valor de t usando el método de Newton-Raphson
        
        # Asignación de los puntos de integración y sus simétricos
        x[i - 1] = -t
        x[npts - i] = t

        # Cálculo de los pesos asociados a los puntos
        w[i - 1] = 2.0 / ((1.0 - t * t) * pp * pp)
        w[npts - i] = w[i - 1]

    # Ajuste de los puntos y pesos según el tipo de intervalo (job)
    if (job == 0):  # Intervalo estándar (a, b)
        for i in range(0, npts):
            x[i] = x[i] * (b - a) / 2.0 + (b + a) / 2.0  # Escalamiento de los puntos
            w[i] = w[i] * (b - a) / 2.0  # Escalamiento de los pesos
    elif (job == 1):  # Intervalo (a, inf)
        for i in range(0, npts):
            xi = x[i]
            x[i] = a * b * (1.0 + xi) / (b + a - (b - a) * xi)
            w[i] = w[i] * 2.0 * a * b * b / ((b + a - (b - a) * xi) ** 2)
    elif (job == 2):  # Intervalo (-inf, inf)
        for i in range(0, npts):
            xi = x[i]
            x[i] = (b * xi + b + a + a) / (1.0 - xi)
            w[i] = w[i] * 2.0 * (a + b) / ((1.0 - xi) ** 2)
            
            

# Función para realizar la integración usando los puntos y pesos calculados
def gaussint(no, min, max):
    quadra = 0.0  # Inicialización del valor de la integral
    gauss(no, 0, min, max, x, w)  # Llama a la función gauss para obtener los puntos y pesos

    # Calcula la integral sumando la función evaluada en los puntos por sus respectivos pesos
    for n in range(0, no):
        quadra += f(x[n]) * w[n]
    return quadra  # Devuelve el valor calculado de la integral

# Realiza la integral
result = gaussint(max_in, vmin, vmax)  # Calcula la integral con i puntos
print("Resultado de la integral=", result)  # Mensaje final al usuario

## Calcula el valor de referencia usando la función de integración numérica de scipy
ref_value, _ = quad(f, vmin, vmax)
print("Valor de referencia de la integral con scipy =", ref_value)

# Calcula el error absoluto
error_abs = abs(result - ref_value)
print("Error absoluto =", error_abs)

# Calcula el error relativo
error_rel = error_abs / abs(ref_value)
print("Error relativo =", error_rel)
