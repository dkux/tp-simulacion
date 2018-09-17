import math
import matplotlib.pyplot as plt
import numpy as np
import GeneradorNumeros as GenNums

from scipy.stats import norm
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

def ajuste_extremos(x):
    x = [i * (1-2*delta) for i in x]
    #return (1-2*delta)*x+delta
    x = [i + delta for i in x]
    return x


n=101 #cant de ptos de F(x) preferentemente impar para considerar el 0 
delta=0.01 #valores maximos y minimos de la F(x)
w=(1-2*delta)/(n-1) #ancho de bin
semilla = (80560 + 85977) // 2  # type: int


x = np.linspace(norm.ppf(delta),norm.ppf(1-delta), n)
print x
generador = GenNums.GeneradorNumeros()
valores = generador.generar_numeros(semilla, 1000, True)

#valores = map((1-2*delta)*valores+delta, valores)
res = ajuste_extremos(valores)
#u=0.581 #ejemplo fijo
#k=int(math.floor(u/w))-1 #indice de bin

k = [int(math.floor(i / w))-1 for i in res]
#inversa = ((u - (delta+k*w))/w) * (x[k+1]-x[k])+x[k]
#print inversa

inversas = []

for index, value in enumerate(res):
    inv = ((value - (delta+k[index]*w))/w) * (x[k[index]+1]-x[k[index]])+x[k[index]]
    #inv = np.interp(value,[delta+k[index]*w, delta+(k[index]+1)*w],[x[k[index]],x[k[index]+1]])
    inversas.append(inv)
print inversas

