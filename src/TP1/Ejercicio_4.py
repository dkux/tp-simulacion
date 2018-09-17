import math
import matplotlib.pyplot as plt
import numpy as np
import GeneradorNumeros as GenNums

from scipy.stats import norm
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

def funcion_normal_estandard(x):
    return (1/math.sqrt(2*math.pi))*math.e**(-x**2/2)

def funcion_exponencial(x,lamb):
    return (lamb*math.e**(-lamb*x))

def funcion_exponencial_vs_normal_standard(x):
    return ((math.sqrt(2/math.pi))*math.e**(x-(x**2/2)))

c = math.sqrt(2*math.e/math.pi) #si x es 1 el exponente de funcion_exponencial_vs_normal_standard es maximo

semilla = (80560 + 85977) // 2  # type: int
generador = GenNums.GeneradorNumeros()
valores = generador.generar_numeros(semilla, 1000, True)



for index, value in enumerate(valores):
    pass
    lamb=1
    probabilidad = funcion_normal_estandard(value)/(c*funcion_exponencial(value,lamb))
    #if value < 