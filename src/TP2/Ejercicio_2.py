#!/usr/bin/python
# coding=utf-8
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power
from numpy import linalg as LA

lambda_L = 1/40.0
lambda_R = 1/30.0

matriz_trancision = []

p = (1-lambda_L)*(1-lambda_R)+lambda_L*lambda_R
#p = 0.5
q = (1-lambda_L)*lambda_R
#q = 0.3

n = 30
iteraciones = 100000
#generar matriz
for i in range(n):
    my_list=[]
    for j in range(n):
        if i==j:
            my_list.append(p)
        elif j==i+1:
            my_list.append(1-p-q)
        elif j==i-1:
            my_list.append(q)
        else:
            my_list.append(0)
    matriz_trancision.append(my_list)

matriz_trancision[0][1] = 1-p
matriz_trancision[n-1][n-2] = 1-p

mt = np.array(matriz_trancision).transpose()

#multiplico la matriz iteraciones veces
power_matriz_trancision = matrix_power(mt,iteraciones)

#calculo de Autovalores y Autovectores
autovalores, autovectores = LA.eig(matriz_trancision)

#Defino el estado inicial 
P0 = np.zeros(n)
P0[0]=1

#Calculo el estado final
Pn =power_matriz_trancision.dot(P0)
#print np.sum(Pn)
veces=np.zeros(n)
veces[0]=1
estado=0
window=0.01 #ventana 10 ms

L=np.zeros(iteraciones)
R=np.zeros(iteraciones)
for i in range(iteraciones):
    #Tiempo de llegada del próximo
    tL=np.random.binomial(1,lambda_L)
    if tL>0 and estado<n-1:
        #Llegan pedidos y no me paso del maximo
        estado=estado+1
        if i>0:
            L[i]=L[i-1]+1
    else:
        #No llegan pedidos
        L[i]=L[i-1]
        
    #Tiempo de salida del próximo
    tR=np.random.binomial(1,lambda_R) 
    if tR>0 and estado >0:
        #Se resuelven pedidos y no me paso del minimo
        estado=estado-1
        if i>0:
            R[i]=R[i-1]+1
    else:
        #No se resurlven pedidos
        R[i]=R[i-1]
    veces[estado]=veces[estado]+1

plt.plot(L)
plt.show()
# x = []
# plt.hist(veces,20)
plt.plot(veces)
plt.show()

plt.plot(Pn)
plt.plot(veces/iteraciones)
plt.show()

print "Porcentaje de tiempo que el servidor se encuentra sin procesar solicitudes = "+str(veces[0]/iteraciones)

exit(0)

