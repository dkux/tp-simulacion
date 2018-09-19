# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import GeneradorNumeros as GenNums


# Semilla: Parte entera del promedio de los padrones
semilla = (80560 + 85977) // 2  # type: int
totalValues = 6000
generador = GenNums.GeneradorNumeros()
valores = generador.generar_numeros(semilla, totalValues)

#Tomo los valores de las posiciones pares
array_X = valores[::2]
#Tomo los valores de las posiciones impares
array_Y = valores[1:][::2]

plt.plot(array_X, array_Y, 'ro')
plt.show()

array_X = []
array_Y = []
array_Z = []
index = 0
for value in valores:
    if index == 0:
        array_X.append(value)
        index += 1
    elif index == 1:
        array_Y.append(value)
        index += 1
    else:
        array_Z.append(value)
        index = 0

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(array_X, array_Y, array_Z)
plt.show()
