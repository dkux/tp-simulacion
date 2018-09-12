# coding=utf-8
import math
import matplotlib.pyplot as plt
import numpy as np
import GeneradorNumeros as GenNums

def inversa_exponencial(x):
    return -math.log(1-x)/lamb


lamb = 1 / 15.0

# Semilla: Parte entera del promedio de los padrones
semilla = (80560 + 85977) // 2  # type: int

generador = GenNums.GeneradorNumeros()
valores = generador.generar_numeros(semilla, 100000, True)
valores = map(inversa_exponencial, valores)
print "Media"
print "Valor teórico: ", 15, "Valor simulado: ", np.mean(valores)
print "Varinza"
print "Valor teórico: ", 15**2, "Valor simulado: ", np.var(valores)

print "Moda"
counts = np.bincount(valores)
print "Valor teórico: ", 0, "Valor simulado: ", np.argmax(counts)
plt.hist(valores, 20)
plt.show()
