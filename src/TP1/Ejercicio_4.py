import math
import matplotlib.pyplot as plt
import numpy as np
import GeneradorNumeros as GenNums

from scipy.stats import norm
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

media_normal = 35.0
desvio_e_normal = 5.0
lamb = 1 / 35.0
#Hay que Normalizar la Dist. Normal
#z = x-media_normal/desvio_e_normal

def inversa_exponencial(x):
    return -math.log(1-x)/lamb

def funcion_normal_estandard(x):
    return (1/math.sqrt(2*math.pi*desvio_e_normal**2))*math.e**(-x**2/2)

def funcion_normal(x):
    return (1/math.sqrt(2*math.pi))*math.e**((-1*(x-media_normal)**2)/(2*desvio_e_normal**2))

def funcion_exponencial(x,lamb):
    return (lamb*math.e**(-lamb*x))

def funcion_exponencial_vs_normal_standard(x):
    return ((math.sqrt(2/math.pi))*math.e**(x-(x**2/2)))

maximo = funcion_normal(media_normal)

semilla = (80560 + 85977) // 2  # type: int
generador = GenNums.GeneradorNumeros()
valores = generador.generar_numeros(semilla, 1000, True)

valores = map(inversa_exponencial, valores)

nro_muestras = 1000

for index, value in enumerate(valores):
    pass
    #lamb=1
    probabilidad_aceptar = funcion_normal_estandard(value)/(maximo*funcion_exponencial(value,lamb))
    if probabilidad_aceptar <  0.5:
        pass
    else:
        pass