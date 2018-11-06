# coding=utf-8
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power
from numpy import linalg as LA

lambda_L = 1/40.0
lambda_R = 1/30.0

exp_lambda_L= np.random.exponential(1/lambda_L)
exp_lambda_R= np.random.exponential(1/lambda_L)

matriz_transistion = ([])

for i in range(0, 29):
    #generar matriz
    pass

#multiplico la matriz 6 veces
power_matriz_transistion = matrix_power(matriz_transistion,6)

#calculo de Autovalores y Autovectores
autovectores , autovalores = LA.eig(matriz_transistion)



