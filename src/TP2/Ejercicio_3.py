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

#Posicion inicial

W_next = np.array([-1,-1,-1])

X_curr = []
X_next = []

Y_curr = []
Y_next = []

Z_curr = []
Z_next = []

#W_curr = W_next

for x in [-1,0,1]:
    for y in [-1,0,1]:
        for z in [-1,0,1]:
            W_curr = np.array([x,y,z])
            X_curr.append(W_next.item(0))
            Y_curr.append(W_next.item(1))
            Z_curr.append(W_next.item(2))

            W_next = matriz_trancision.dot(W_curr)

            X_next.append(W_next.item(0))
            Y_next.append(W_next.item(1))
            Z_next.append(W_next.item(2))



exit(0)

