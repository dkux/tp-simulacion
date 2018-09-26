from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
import random

valores = [0] * 1000
for i in range(0, 1000):
    tiempo = random.uniform(0, 1)
    tasa = 7 * tiempo
    valores[i] = np.random.poisson(tasa)
media = np.mean(valores)
varianza = np.var(valores)
desvio = np.std(valores)


print "Media", media, "Varianza: ", varianza, "Desvio", desvio



