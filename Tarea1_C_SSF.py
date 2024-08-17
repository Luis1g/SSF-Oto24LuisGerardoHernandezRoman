#!/usr/bin/env python
from __future__ import print_function,division
### http://www-personal.umich.edu/~mejn/computational-physics/

from pylab import scatter,xlabel,ylabel,xlim,ylim,show
from numpy import loadtxt

data = loadtxt("stars.dat",float)
x = data[:,0]
y = data[:,1]

scatter(x,y)
xlabel("Temperature")
ylabel("Magnitude")
xlim(0,13000)
ylim(-5,20)
show()



# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17

@author: luish
"""

import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos del archivo
data = np.loadtxt("stars.dat", float)
x = data[:, 0]
y = data[:, 1]

# Crear gráfico de dispersión
plt.scatter(x, y)
plt.xlabel("Temperature")
plt.ylabel("Magnitude")
plt.xlim(0, 13000)
plt.ylim(-5, 20)

# Mostrar la gráfica
plt.show()




import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo
data = np.loadtxt("stars.dat", float)
x = data[:, 0]
y = data[:, 1]

# Crear gráfico de dispersión usando seaborn
sns.scatterplot(x=x, y=y)
plt.xlabel("Temperature")
plt.ylabel("Magnitude")
plt.xlim(0, 13000)
plt.ylim(-5, 20)

# Mostrar la gráfica
plt.show()



