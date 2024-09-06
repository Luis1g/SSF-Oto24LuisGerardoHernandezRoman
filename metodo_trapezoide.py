# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:36:07 2024

@author: luish
"""
# Primera integral con 6 subintervalos 
from numpy import *
import numpy as np

def func(x):
    return (e**((-x**2)/2))/np.sqrt(2*pi)
def trapezoid(A, B, N):
    h=(B-A)/(N-1)
    sum = (func(A)+ func(B))/2
    for i in range(1, N-1):
        sum += func(A+i*h)
    return h* sum

# Se define los limites de integracion y el numero de subintervalos
A=-1
B=1
N=7 # Se necesita colocar N+1 subinetervalos para tener 6
print(trapezoid(A,B, N-1))

##############################################################################
# Primera integral con 15 subintervalos 
def func(x):
    return (e**((-x**2)/2))/np.sqrt(2*pi)
def trapezoid(A, B, N):
    h=(B-A)/(N-1)
    sum = (func(A)+ func(B))/2
    for i in range(1, N-1):
        sum += func(A+i*h)
    return h* sum

# Se define los limites de integracion y el numero de subintervalos
A=-1
B=1
N=16 # 15 subintervalos
print(trapezoid(A,B, N-1))

##############################################################################
# Segunda integral con 6 subintervalos 


def func(x):
    return (e**(x)*sin(x))/(1+e**2)
def trapezoid(A, B, N):
    h=(B-A)/(N-1)
    sum = (func(A)+ func(B))/2
    for i in range(1, N-1):
        sum += func(A+i*h)
    return h* sum

# Se define los limites de integracion y el numero de subintervalos
A=-1
B=1
N=7 # Se necesita colocar N+1 subinetervalos para tener 6
print(trapezoid(A,B, N-1))

##############################################################################
# Segunda integral con 15 subintervalos 


def func(x):
    return (e**(x)*sin(x))/(1+e**2)
def trapezoid(A, B, N):
    h=(B-A)/(N-1)
    sum = (func(A)+ func(B))/2
    for i in range(1, N-1):
        sum += func(A+i*h)
    return h* sum

# Se define los limites de integracion y el numero de subintervalos
A=-1
B=1
N=16 # Se necesita colocar N+1 subinetervalos para tener 6
print(trapezoid(A,B, N-1))

##############################################################################
# Segunda integral con 20 subintervalos 


def func(x):
    return (e**(x)*sin(x))/(1+e**2)
def trapezoid(A, B, N):
    h=(B-A)/(N-1)
    sum = (func(A)+ func(B))/2
    for i in range(1, N-1):
        sum += func(A+i*h)
    return h* sum

# Se define los limites de integracion y el numero de subintervalos
A=-1
B=1
N=21 # Se necesita colocar N+1 subinetervalos para tener 6
print(trapezoid(A,B, N-1))

