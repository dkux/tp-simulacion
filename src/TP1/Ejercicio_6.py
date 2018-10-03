# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import GeneradorNumeros as GenNums

# Cada lanzamiento de la moneda corresponde a un proceso Bernoulli
# Cada uno de los experimentos se puede modelar con una distribución Geométrica

valores = np.random.geometric(0.5, 10000)
#plt.DataFrame(valores).hist(range=(-0.5, max(valores)+0.5), bins=max(valores)+1)

plt.hist(valores, bins=max(valores)+1, range=(0, max(valores)+1))
plt.show()
