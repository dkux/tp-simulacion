# coding=utf-8
import math
import matplotlib.pyplot as plt
import numpy as np

arribos = [1, 3, 7, 8, 15]
atencion = [3.5, 4, 2, 1, 1.5, 4]
personas_en_el_sitema = []

tiempo = np.arange(0.0, 22.0, 0.5)

personas = 0
for value in tiempo:
    if value in arribos:
        personas = personas + 1
        personas_en_el_sitema.append(personas)
    else:
        personas_en_el_sitema.append(personas)

plt.plot(tiempo, personas_en_el_sitema)
plt.show()
