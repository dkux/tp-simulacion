import math
import matplotlib.pyplot as plt
import numpy as np
import GeneradorNumeros as GenNums

from scipy.stats import norm
import matplotlib.pyplot as plt
from random import *



fig, ax = plt.subplots(1, 1)
delta = 0.01
mu = 35.0
sigma = 5.0
#lamb = 1 / 35.0
lamb = 1
#Hay que Normalizar la Dist. Normal
#z = x-mu/sigma
#x = z*sigma+mu

def inversa_exponencial(x):
    return -math.log(1-x)/lamb

def funcion_normal_estandard(x):
    return (1/math.sqrt(2*math.pi*sigma**2))*math.e**(-x**2/2)

def funcion_normal(x):
    return (1/math.sqrt(2*math.pi))*math.e**((-1*(x-mu)**2)/(2*sigma**2))

def funcion_exponencial(x,lamb):
    return (lamb*math.e**(-lamb*x))

def funcion_exponencial_vs_normal_standard(x):
    return ((math.sqrt(2/math.pi))*math.e**(x-(x**2/2)))

def desnormalizar(z,mu,sigma):
    return [mu+i*sigma for i in z]

semilla = (80560 + 85977) // 2  # type: int
semilla2 = semilla+10000  # type: int
generador = GenNums.GeneradorNumeros()

c = math.sqrt(2*math.e/math.pi) #cota normal estandar / exponencial
num = 100 #cantidad de valores a simular


z = []

i=0
while i<num:
    t = random()
    s = random()
    p = funcion_normal_estandard(t)/(c*funcion_exponencial(t,lamb))
    if s<p:
        u = random()
        if u < 0.5:
            z.append(t)
            i = i+1
        else:
            z.append(-t)
            i = i+1

#probabilidad_aceptar = funcion_normal_estandard(t)/(c*funcion_exponencial(t,lamb))
x = desnormalizar(z,mu,sigma)
print x