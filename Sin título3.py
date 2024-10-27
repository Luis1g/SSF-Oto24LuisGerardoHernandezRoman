# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:47:49 2024

@author: luish
"""
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import math
from pandas.plotting import scatter_matrix  # Importar de pandas.plotting en lugar de pandas.tools

# Importamos los datos de eBADS_Accel
data = pd.read_excel("S1_Dataset.xlsx")
df = pd.DataFrame(data)
# In[0]
# Modificación de los datos para su uso
BADS_Ac = df["BADS-SF_Activation"]
BADS_Av = df["BADS-SF_Avoidance"]
QOL_MTS = df["WHOQOL_26_Mean_total_score"]
CES_D = df["CES_D"]
QOL_PhiH = df["WHOQOL_26_Phisical_health"]
QOL_PsyH = df["WHOQOL_26_Psychological_health"]
QOL_SR = df["WHOQOL_26_Social_relationships"]
QOL_E = df["WHOQOL_26_Environment"]
QOL_O = df["WHOQOL_26_Overall_QOL"]

# In[1]
# Crear la matriz de dispersión

scatter_matrix(df[["BADS-SF_Activation", "WHOQOL_26_Mean_total_score", "CES_D"]], 
               alpha=0.7, 
               figsize=(10, 10), 
               diagonal='hist')

plt.suptitle("Matriz de Dispersión")  # Título para la figura
plt.show()
# In[1.1]

# Crear la matriz de dispersión
scatter_matrix(df[["BADS-SF_Avoidance", "WHOQOL_26_Mean_total_score", "CES_D"]], 
               alpha=0.7, 
               figsize=(10, 10), 
               diagonal='hist')

plt.suptitle("Matriz de Dispersión")  # Título para la figura
plt.show()
# In[2]

# Relizamos una regresion simple de los datos
# Cantidad de puntos
n = len(QOL_MTS)

# Cálculo de las sumatorias necesarios para la regresion
sum_x = sum(QOL_MTS)
sum_y = sum(CES_D)
sum_xy = sum(xi * yi for xi, yi in zip(QOL_MTS, CES_D))
sum_x_squared = sum(xi ** 2 for xi in QOL_MTS)

# Cálculo de la pendiente (m) QOL_MTS la intercepcion (b)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b = (sum_y - m * sum_x) / n

# Valores predichos por la regresión
y_pred = [m * xi + b for xi in QOL_MTS]

# Cálculo de los residuos QOL_MTS desviación estándar
residuos = [yi - y_pred_i for yi, y_pred_i in zip(CES_D, y_pred)]
std_residuos = math.sqrt(sum(r ** 2 for r in residuos) / (n - 2))

# Imprimir la ecuación de la recta
print(f"Ecuación de la recta: CES_D = {m:.2f}QOL_MTS + {b:.2f}")

plt.figure()

#Grafica de puntos con barras de error
plt.errorbar(QOL_MTS, CES_D, yerr=std_residuos, fmt='o', color='b', ecolor='gray', alpha=0.7, label='Datos')

# Valores para de la regresion lineal
regression_line = [m * xi + b for xi in QOL_MTS]

# Grafica de la regresion lineal
plt.plot(QOL_MTS, regression_line, color='r', label=f'CES_D = {m:.2f}QOL_MTS + {b:.2f}')

# Datos de la gráfica
plt.xlabel("WHOQOL_26_Mean_total_score")
plt.ylabel("CES_D")
plt.title("Regresión Lineal entre la calidad de vida y la depresión")
plt.legend()
plt.grid(True)
plt.show()
# In[3]

from statsmodels.formula.api import ols
model = ols("BADS_Ac ~ QOL_MTS", data).fit()

print(model.summary())

# In[4]
import seaborn as sns
df = pd.DataFrame(data)
sns.pairplot(df, vars=["BADS-SF_Activation", "WHOQOL_26_Mean_total_score", "CES_D"], kind='reg')
plt.suptitle("BADS-SF_Activation", y=1)  # Título opcional, se ajusta hacia arriba
plt.show()

import seaborn as sns
df = pd.DataFrame(data)
sns.pairplot(df, vars=["BADS-SF_Avoidance", "WHOQOL_26_Mean_total_score", "CES_D"], kind='reg')
plt.suptitle("BADS-SF_Avoidance", y=1)  # Título opcional, se ajusta hacia arriba
plt.show()