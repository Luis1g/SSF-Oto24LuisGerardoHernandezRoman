# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:55:18 2024

@author: luish
"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la ecuación del oscilador armónico
def harmonic_eq(x, t, k):
    return x[1], -k * x[0]

# Método de Euler para la integración
def euler_2var(x, func, t, k, dt):
    y = func(x, t, k)
    return x[0] + dt * y[0], x[1] + dt * y[1]

# Función que realiza el cálculo y grafica los resultados
def calc_plot2var(method, equation, k, dt, n_steps):
    t = np.arange(0, n_steps * dt, dt)
    x = np.zeros((n_steps, 2))
    x[0][0] = 2.0  # Posición inicial

    # Iteración del método de Euler
    for i in range(n_steps - 1):
        x[i + 1] = method(x[i], harmonic_eq, t[i], k, dt)

    # Graficar resultados
    fig = plt.figure(figsize=(12, 5))

    # Gráfica de x(t) y v(t)
    axes = fig.add_subplot(1, 2, 1)
    axes.plot(t, x[:, 0], 'r', label="$x(t)$")
    axes.plot(t, x[:, 1], 'b', label="$v(t)$")
    axes.set_xlabel("$t$")
    plt.legend(loc='upper left')

    # Gráfica de la trayectoria en el espacio fase x-v
    axes = fig.add_subplot(1, 2, 2)
    axes.plot(x[:, 0], x[:, 1], '#ff8800')
    axes.set_xlabel("$x(t)$")
    axes.set_ylabel("$v(t)$")
    plt.show()

# Parámetros y ejecución
if __name__ == "__main__":
    dt = 0.01  # Paso de tiempo
    n_steps = 5000  # Número de pasos
    k = 0.5  # Constante de la ecuación
    calc_plot2var(euler_2var, harmonic_eq, k, dt, n_steps)
