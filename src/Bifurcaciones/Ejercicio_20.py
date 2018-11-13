# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0.1, 5., 0.1)
q = np.arange(-5., 0.1, 0.1)

valores = [(1-r) / r for r in t]
valoresq = [(1-r) / r for r in q]
valores_0_1 = [0 for r in t]
valores_0_2 = [0 for r in q]

#plt.plot(t, valores)
plt.plot(q, valoresq)
plt.show()
