import numpy as np
import matplotlib.pyplot as plt
import GeneradorNumeros as GenNums
from scipy import stats

gap_1 = [0.6 , 0.2]
gap_2 = [1.0 , 0.5]

semilla = (80560 + 85977) // 2  # type: int

n=10000
generador = GenNums.GeneradorNumeros()
valores = generador.generar_numeros(semilla, n, True)

res1 = []
res2 = []

count_1 = 0
count_2 = 0

for idx, val in enumerate(valores):
    if val <=gap_1[0] and val>= gap_1[1]:
        count_1 = count_1+1
        res1.append((count_1,idx))
    if val <=gap_2[0] and val>= gap_2[1]:
        count_2 = count_2+1
        res2.append((count_2,idx))

print "Valores simulados vs teorico"
#print valores
print "--------------"
print str(count_1)+" cayeron en intervalo 1 => P(intervalo simulado 1) = "+ str(count_1/float(n)) + " vs. " + "P(intervalo teorico 1) = " + str(gap_1[0]-gap_1[1])
#print res1
print "--------------"
print str(count_2)+" cayeron en intervalo 2 => P(intervalo simulado 2) = "+ str(count_2/float(n)) + " vs. " + "P(intervalo teorico 2) = " + str(gap_2[0]-gap_2[1])
#print res2

