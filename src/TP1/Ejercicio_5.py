# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import GeneradorNumeros as GenNums

# Semilla: Parte entera del promedio de los padrones
semilla = (80560 + 85977) // 2  # type: int

generador = GenNums.GeneradorNumeros()
valores = generador.generar_numeros(semilla, 100000, True)
discreta = [0] * 4
for value in valores:
    if value < 0.5:
        discreta[0] = discreta[0] + 1
    elif 0.5 <= value < 0.7:
        discreta[1] = discreta[1] + 1
    elif 0.7 <= value < 0.8:
        discreta[2] = discreta[2] + 1
    else:
        discreta[3] = discreta[3] + 1
discreta = np.divide(discreta, 100000.0)
plt.bar([1, 2, 3, 4], discreta, 0.01, align='center')
plt.show()
