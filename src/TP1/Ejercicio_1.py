# coding=utf-8
import matplotlib.pyplot as plt
import GeneradorNumeros as GenNums


# Semilla: Parte entera del promedio de los padrones
semilla = (80560 + 85977) // 2  # type: int

generador = GenNums.GeneradorNumeros()
valores = generador.generar_numeros(semilla, 6)
print "Valores generados"
generador.imprimir(valores)

valores = generador.generar_numeros(semilla, 100000, True)
plt.hist(valores, 20)
plt.show()
