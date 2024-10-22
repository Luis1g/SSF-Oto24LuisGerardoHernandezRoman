# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:35:06 2024

@author: luish
"""
# Repositorio Original en  https://colab.research.google.com/github/leflores-fisi/lorenz-attractor/blob/main/LorenzSystem.ipynb#scrollTo=q4nZdzYJjmN0
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint  # Para resolver ecuaciones diferenciales ordinarias (EDOs)
# In[1]:
# Definimos la función para resolver las ecuaciones del atractor de Lorenz
def solve_lorenz(state, t, σ, ρ, β):
    """
    Calcula las derivadas dx, dy y dz según el modelo Lorenz.
    
    Parámetros:
    - state: Tupla (x, y, z) representando el estado actual
    - t: Tiempo actual (necesario para odeint)
    - σ, ρ, β: Parámetros del sistema Lorenz

    Retorna:
    - dx, dy, dz: Derivadas en cada dirección
    """
    x, y, z = state
    dx = σ * (y - x)
    dy = x * (ρ - z) - y
    dz = (x * y) - (β * z)
    return dx, dy, dz

# Ejemplo de uso de la función solve_lorenz con un estado inicial dado
solve_lorenz((1, 1, 1), t=1, σ=10, ρ=28, β=8/3)

# Definimos el estado inicial y los parámetros del sistema
initial_state = (1., 1., 1.)  # Estado inicial (x, y, z)
σ, ρ, β = 10, 28, 8/3  # Parámetros del atractor de Lorenz

# Generamos una secuencia de tiempo entre 0 y 100 con 3000 puntos
t = np.linspace(0, 100, 3000)
print('Valores equidistantes de t:', t.size)

# Resolvemos las EDOs para obtener la trayectoria del sistema
states = odeint(solve_lorenz, initial_state, t, args=(σ, ρ, β))

# Extraemos las coordenadas x, y, z de la solución
xs = states[:, 0]
ys = states[:, 1]
zs = states[:, 2]

# Creamos una figura 3D para graficar el atractor de Lorenz
ax = plt.figure().add_subplot(projection='3d')
ax.plot(xs, ys, zs, lw=0.5, c='#7B86B2')  # Trazo de la trayectoria en 3D
ax.set_title("Lorenz Attractor with odeint")  # Título del gráfico
plt.show()  # Mostramos la figura
# In[2]:
    
# Exploramos la estructura del colormap 'plasma'
cmap = plt.cm.plasma
print("Tipo del objeto colormap:", type(cmap))
print("Elemento indexado:", cmap(0))  # Accedemos a un color por índice

# Definimos una función para visualizar el atractor de Lorenz con colores segmentados
def lorenz_attractor(state0, parameters, ax=None, text_offset=0.01):
    """
    Visualiza el atractor de Lorenz en 3D usando segmentos coloreados.

    Parámetros:
    - state0: Estado inicial (x, y, z)
    - parameters: Parámetros del sistema (σ, ρ, β)
    - ax: Eje 3D opcional para graficar
    - text_offset: Desplazamiento del texto en el gráfico
    """
    σ, ρ, β = parameters
    n = 3000  # Número de puntos en la simulación
    t = np.linspace(0, 100, n)  # Secuencia de tiempo

    # Resolvemos las EDOs para obtener la trayectoria
    states = odeint(solve_lorenz, state0, t, args=(σ, ρ, β))
    xs, ys, zs = states[:, 0], states[:, 1], states[:, 2]

    if ax is None:
        ax = plt.figure(figsize=(7, 8)).add_subplot(projection='3d')

    s = 10  # Intervalo de segmentación para los colores

    # Graficamos segmentos coloreados de la trayectoria
    for i in range(0, n - s, s):
        ax.plot(xs[i:i+s+1], ys[i:i+s+1], zs[i:i+s+1], color=cmap(i/n), alpha=0.5, lw=1)

    ax.text2D(0.44, text_offset, f"ρ={ρ}", transform=ax.transAxes)
    ax.figure.tight_layout()
    return ax.figure

# Visualizamos el atractor para los parámetros iniciales
lorenz_attractor((1, 1, 1), (10, 28, 8/3)).show()
# In[3]:
# Probamos la visualización para diferentes valores de ρ
rho_values = [-42, 15, 28, 100]
solutions = [lorenz_attractor((1, 1, 1), (10, rho, 8/3)) for rho in rho_values]

for solution in solutions:
    solution.show()

# Creamos una figura 2x2 para visualizar diferentes atractores
rows, cols = 2, 2
size = (10, 10)
fig, axs = plt.subplots(rows, cols, figsize=size, subplot_kw=dict(projection='3d'))

# Ajustamos los valores de rho en una cuadrícula 2x2
rho_values2d = np.array(rho_values).reshape(rows, cols)

# Graficamos cada atractor en su respectivo sub-eje
for row, col in np.ndindex((rows, cols)):
    rho = rho_values2d[row, col]
    lorenz_attractor((1, 1, 1), (10, rho, 8/3), ax=axs[row, col], text_offset=-0.03)

fig.show()  # Mostramos la figura
# In[4]:
# Definimos una función para visualizar la "mariposa de Lorenz"
def butterfly(ax, colormap, rho, angle):
    """
    Visualiza una curva de Lorenz estilizada como 'mariposa'.

    Parámetros:
    - ax: Eje 3D para graficar
    - colormap: Nombre del colormap a utilizar
    - rho: Parámetro ρ del sistema
    - angle: Ángulo de vista
    """
    tmax = 100
    n = 10000  # Número de puntos
    sigma, beta = 10, 2.667
    u0, v0, w0 = (0, 1, 1.05)  # Estado inicial
    t = np.linspace(0, tmax, n)

    # Resolución de la trayectoria
    soln = odeint(solve_lorenz, (u0, v0, w0), t, args=(sigma, rho, beta))
    x, y, z = soln[:, 0], soln[:, 1], soln[:, 2]

    ax.set_facecolor('k')  # Fondo negro

    # Graficamos segmentos con color según el colormap
    s = 10
    cmap = getattr(plt.cm, colormap)
    for i in range(0, n - s, s):
        ax.plot(x[i:i+s+1], y[i:i+s+1], z[i:i+s+1], color=cmap(i/n), alpha=0.4)

    ax.set_axis_off()  # Ocultamos los ejes
    ax.view_init(angle, angle)  # Establecemos el ángulo de vista

# Creamos una figura para mostrar múltiples "mariposas"
fsize = (10, 10)
ndim = 5
axs = plt.figure(facecolor='k', figsize=fsize).subplots(ndim, ndim, subplot_kw=dict(projection='3d'))

# Generamos las visualizaciones en una cuadrícula ndim×ndim
for i, (row, col) in enumerate(np.ndindex((ndim, ndim))):
    butterfly(axs[row, col], plt.colormaps()[i], rho=2.5 * i, angle=10 * i)
