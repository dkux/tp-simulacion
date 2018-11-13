#!/usr/bin/python
# coding=utf-8
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power
from numpy import linalg as LA


#Ptos de equilibrio =>  X=Y=0 ,  Z=Z para todo z

matriz_trancision = np.matrix([
    [0.5,1,0],
    [-0.5,1,0],
    [-1,-1,1]
])
#calculo de Autovalores y Autovectores
autovalores, autovectores = LA.eig(matriz_trancision)
W_next = np.matrix([0.0,0.0,0.0])

#Posicion inicial
n=100

for x in [-1,0,1]:
    for y in [-1,0,1]:
        for z in [-1,0,1]:
            #Fijo condicion inicial para esta sumulacion
            W_curr = np.matrix([x,y,z])
            X_curr = []
            X_next = []
            Y_curr = []
            Y_next = []
            Z_curr = []
            Z_next = []
            for i in range(n):
                if i==0:
                    X_curr.append(W_curr.item(0))
                    Y_curr.append(W_curr.item(1))
                    Z_curr.append(W_curr.item(2))

                W_next = W_curr.dot(matriz_trancision.transpose())

                    
                X_next.append(W_next.item(0))
                Y_next.append(W_next.item(1))
                Z_next.append(W_next.item(2))

                if i<n-1:
                    X_curr.append(W_next.item(0))
                    Y_curr.append(W_next.item(1))
                    Z_curr.append(W_next.item(2))
                W_curr=W_next
            # Plot
            plt.scatter(X_curr, X_next,c='red',label='X')
            plt.plot(X_curr,X_next,c='red')
            plt.scatter(Y_curr, Y_next,c='green',label='Y')
            plt.plot(Y_curr,Y_next,c='green')
            plt.scatter(Z_curr, Z_next,c='blue',label='Z')
            plt.plot(Z_curr,Z_next,c='blue')
            plt.title('Plano de fase Inicial: '+str(x)+"|"+str(y)+"|"+str(z))
            plt.xlabel('k')
            plt.ylabel('k+1')
            plt.show()


exit(0)

