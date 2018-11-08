#!/usr/bin/python
# coding=utf-8
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power
from numpy import linalg as LA

lambda_L = 1/40.0
lambda_R = 1/30.0

rand_exp_lambda_L = np.random.exponential(1/lambda_L)
rand_exp_lambda_R = np.random.exponential(1/lambda_L)

def exp_lambda_L_T(t):
    return(lambda_L*math.exp(-1*lambda_L*t))

def exp_lambda_R_T(t):
    return(lambda_R*math.exp(-1*lambda_R*t))

matriz_transision = []


invariante = exp_lambda_L_T(0)*exp_lambda_R_T(0)+exp_lambda_L_T(1)*exp_lambda_R_T(1)

aumento = exp_lambda_L_T(1)*exp_lambda_R_T(0)

disminuye = exp_lambda_L_T(0)*exp_lambda_R_T(1)

#generar matriz
for i in range(0,30):
    my_list=[]
    for j in range(0,29):
        if i==j:
            my_list.append(invariante)
        if i==j+1:
            my_list.append(aumento)
        if i==j-1:
            my_list.append(disminuye)
        else:
            my_list.append(0)
    matriz_transision.append(my_list)


#print(type(matriz_transision))
#print(len(matriz_transision))
#print(len(matriz_transision[0]))

mt = np.array(matriz_transision)
print(type(mt))
print(len(mt))
print(len(mt[0]))

#multiplico la matriz 6 veces
power_matriz_transistion = matrix_power(mt,6)

#calculo de Autovalores y Autovectores
autovectores , autovalores = LA.eig(matriz_transision)

