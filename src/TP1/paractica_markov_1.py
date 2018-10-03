import numpy as np
from numpy.linalg import matrix_power

p = [[0.6, 0.4], [0.1, 0.9]]

for i in range(0, 6):
    p = matrix_power(p, 2)

print(np.matrix(p))

