import numpy.linalg as linalg

A = [[1, -1, 0], [-1, -3, 1], [0, 1, 1]]

auto_valores, auto_vectores = linalg.eig(A)

print auto_vectores

print auto_valores 