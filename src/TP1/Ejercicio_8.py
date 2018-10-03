# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import GeneradorNumeros as GenNums
from scipy import stats

p=0.5 #probabilidad de exito
n=1000 #cantidad de intentos
m=12 #cantidad de bins
ns = 0.01 #nivel de significacion

#Primero genereramos el resultado esperado con m bins
resultado_esperado = [1.0] * m

for idx, val in enumerate(resultado_esperado):
    if idx == 0:
        resultado_esperado[idx] = p
    else:
        resultado_esperado[idx] = resultado_esperado[idx-1]*p

#calculo del resultado empirico
resultado_empirico = np.random.geometric(p, n)
#generar el histograma del resultado empirico
h = [0.0] * m
k=0
for val in resultado_empirico:
    if val < m:
        h[val-1] = h[val-1]+1
    else:
        k=k+1
print "Valores fuera del histograma = "+str(k)
#Normalizar el histograma a porcentaje de valores
for i in range(m):
    h[i] = h[i]/n

chisq, pvalue = stats.chisquare(h, resultado_esperado)

if 1-pvalue<ns:
    print "Aceptado a nivel "+str(ns)
    print "Valores chisquare , 1-pval = " + str(chisq) + "," + str(1-pvalue)
else:
    print "Rechazado a nivel "+str(ns)
    print "Valores chisquare , 1-pval = " + str(chisq) + "," + str(1-pvalue)

exit(0)




