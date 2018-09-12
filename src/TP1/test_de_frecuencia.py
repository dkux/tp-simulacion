import GeneradorNumeros as GenNums
import numpy as np
from scipy.stats import chisquare

semilla = 1
numExp = 1000
generador = GenNums.GeneradorNumeros(7, 1, 10)

valores = generador.generar_numeros(semilla, numExp)

y = np.bincount(valores)
frequencias = [0] * 10
freq_esperadas = [0.1 * numExp] * 10

for idx, val in enumerate(y):
    frequencias[idx] = val

result_test = chisquare(frequencias, freq_esperadas)
if result_test.statistic == 0:
    print "No se puede rechazar H0"
else:
    print "No se puede aceptar H0"
# Power_divergenceResult(statistic=0.0, pvalue=1.0)
# Como statistic es 0.00 no se puede rechazar h0
