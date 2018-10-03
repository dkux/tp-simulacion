import numpy as np
from numpy.linalg import matrix_power
from random import *
import matplotlib.pyplot as plt


F = [[0.95, 1], [0.4, 1]]

estado = 0
valores = [0] * 20
for i in range(0, 20):
    randomV = random()
    if randomV > F[estado][0] and estado == 0:
        estado = 1
    elif estado == 1 and randomV < F[estado][0]:
        estado = 0
    valores[i] = estado


print(np.matrix(valores))

plt.plot(valores, '--bo')
plt.show()



