import GeneradorNumeros as GenNums
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt


semilla = 1
numExp = 1000

generador = GenNums.GeneradorNumeros(7, 1, 10)

valores = generador.generar_numeros(semilla, numExp)

generador.imprimir(valores)

#Tomo los valores de las posiciones pares
array_X = valores[::2]
#Tomo los valores de las posiciones impares
array_Y = valores[1:][::2]

plt.plot(array_X, array_Y, 'ro')
plt.axis([-1, 11, -1, 11])

plt.show()

