# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:40:18 2024

@author: luish
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros
omega_0 = 1.0  # Frecuencia angular natural
alpha = 0.1    # Parámetro de no linealidad
x0 = 10       # Condición inicial de posición
v0 = 1.0       # Condición inicial de velocidad

# Ecuación diferencial de segundo orden convertida en sistema de primer orden
def oscilador_armonico_no_lineal(t, y):
    x, v = y
    dxdt = v
    dvdt = -omega_0**2 * x - alpha * x**3
    return [dxdt, dvdt]

# Tiempo de integración
t_span = (0, 20)  # Tiempo total
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Puntos de evaluación del tiempo

# Condiciones iniciales [posición, velocidad]
y0 = [x0, v0]

# Resolución del sistema usando el método de Runge-Kutta de orden 5(4)
sol = solve_ivp(oscilador_armonico_no_lineal, t_span, y0, t_eval=t_eval, method='RK45')

# Gráfica de la solución
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], label='Posición $x(t)$')
plt.plot(sol.t, sol.y[1], label='Velocidad $v(t)$', linestyle='--')
plt.title('Oscilador Armónico No Lineal (x^3)')
plt.xlabel('Tiempo $t$')
plt.ylabel('Posición y Velocidad')
plt.legend()
plt.grid(True)
plt.show()
