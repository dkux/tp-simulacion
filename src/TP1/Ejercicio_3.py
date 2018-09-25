import math
import matplotlib.pyplot as plt
import numpy as np
import GeneradorNumeros as GenNums

from scipy.stats import norm
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

def ajuste_extremos(x):
    x = [i * (1-2*delta) + delta for i in x]
    #return (1-2*delta)*x+delta
    #x = [i + delta for i in x]
    return x

semilla = (80560 + 85977) // 2  # type: int
num = 18500 #cantidad de puntos a simular
n=981 #cant de intervalos de F(x) preferentemente impar para considerar el 0 
delta=0.01 #valores maximos y minimos de la F(x)
w=(1-2*delta)/(n-1) #ancho de bin para la acumulada de la normal F(x)

m = 101  #cant de intervalos de f(x) => intervalos del histograma
gamma = 3.0 #valores maximos y minimos de la normal f(x)
q=(2*gamma)/(m-1) #ancho de bin para la acumulada de la normal F(x)


x = np.linspace(norm.ppf(delta),norm.ppf(1-delta), n) #invierte la normal
max_x = max(x)
min_x = min(x)
#print x
generador = GenNums.GeneradorNumeros()
valores = generador.generar_numeros(semilla, num, True)

#valores = map((1-2*delta)*valores+delta, valores)
res = ajuste_extremos(valores)
#u=0.581 #ejemplo fijo
#k=int(math.floor(u/w))-1 #indice de bin

#inversa = ((u - (delta+k*w))/w) * (x[k+1]-x[k])+x[k]
#print inversa
max_res = max(res)
min_res = min(res)

inversas = []

for value in res:
    k=int(math.floor((value-delta) / w)) # Este es mi indice de bin
    #interpola los valores de la F^-1(x)
    inv = ((value - (delta+k*w))/w) * (x[k+1]-x[k])+x[k] 
    
    #inv = np.interp(value,[delta+k*w, delta+(k+1)*w],[x[k],x[k+1]])
    inversas.append(inv)
#print inversas

max_inv = max(inversas)
min_inv = min(inversas)
h = [0] * m
for value in inversas:
    k = int(math.floor((value+gamma)/q))
    h[k] = h[k]+1
print sum(h)
#p, bins, patches = plt.hist(inversas, m , density=True, facecolor='g', alpha=0.75)
plt.show(h)