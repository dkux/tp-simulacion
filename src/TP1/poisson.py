from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt


mu = 1 * 5
exitos = 6

probabilidad = poisson.pmf(exitos, mu)

print probabilidad

tiempo = []
ocurrencias = []

tiempoAnterior = 0
for i in range(0, 100):
    tiempoAnterior += np.random.exponential(0.5)
    tiempo.append(tiempoAnterior)
    ocurrencias.append(i + 1)


plt.step(tiempo, ocurrencias)
plt.show()

