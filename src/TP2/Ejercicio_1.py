# coding=utf-8
from scipy.stats import bernoulli
import numpy


# Tiempo entre llamadas Exp media 4 seg
# Dos bases de datos
# Prob de ser atendida por la DB_1 0,6
# Prob de ser atendida por la DB_2 0,4
# Tiempo que demora en atender la DB_1 Exp media 0,7 seg
# Tiempo que demora en atender la DB_2 Exp media 1 seg
tiempo = 0
tiempo_atencion_db_1 = 0
tiempo_atencion_db_2 = 0
ocupacion_DB_1 = 0
ocupacion_DB_2 = 0
tiempo_espera_DB_1 = 0
tiempo_espera_DB_2 = 0
solicitudes_sin_espera_opcion_1 = 0
tiempo_espera_opcion_1 = 0
tiempo_total_opcion_1 = 0

data_bern = bernoulli.rvs(size=10000, p=0.6)
i = 0
while i < len(data_bern):
    tiempo_arribo = numpy.random.exponential(4.0)
    tiempo += tiempo_arribo
    if data_bern[i] == 1:
        # Lo atiende la DB 1
        tiempo_atencion_db_1 = numpy.random.exponential(0.7)
        if ocupacion_DB_1 < tiempo:
            # Se atiende sin espera
            solicitudes_sin_espera_opcion_1 += 1
            ocupacion_DB_1 = tiempo + tiempo_atencion_db_1
            tiempo_total_opcion_1 += tiempo_atencion_db_1
        else:
            # Debe esperar
            tiempo_espera_opcion_1 += (ocupacion_DB_1 - tiempo)
            tiempo_total_opcion_1 += (ocupacion_DB_1 - tiempo + tiempo_atencion_db_1)
            ocupacion_DB_1 += tiempo_atencion_db_1
    else:
        # Lo atiende la DB 2
        tiempo_atencion_db_2 = numpy.random.exponential(1.0)
        if ocupacion_DB_2 < tiempo:
            # Se atiende sin espera
            solicitudes_sin_espera_opcion_1 += 1
            ocupacion_DB_2 = tiempo + tiempo_atencion_db_2
            tiempo_total_opcion_1 += tiempo_atencion_db_2
        else:
            # Debe esperar
            tiempo_espera_opcion_1 += (ocupacion_DB_2 - tiempo)
            tiempo_total_opcion_1 += (ocupacion_DB_2 - tiempo + tiempo_atencion_db_2)
            ocupacion_DB_2 += tiempo_atencion_db_2
    i += 1

# Opcion 2
i = 0
tiempo = 0
ocupacion_DB_unica = 0
solicitudes_sin_espera_opcion_2 = 0
tiempo_espera_opcion_2 = 0
solicitudes_sin_espera_opcion_2 = 0
tiempo_espera_opcion_2 = 0
tiempo_total_opcion_2 = 0

while i < 10000:
    tiempo_arribo = numpy.random.exponential(4.0)
    tiempo += tiempo_arribo
    tiempo_atencion_db_unica = numpy.random.exponential(0.8)
    if ocupacion_DB_unica < tiempo:
        # Se atiende sin espera
        solicitudes_sin_espera_opcion_2 += 1
        ocupacion_DB_unica = tiempo + tiempo_atencion_db_unica
        tiempo_total_opcion_2 += tiempo_atencion_db_unica
    else:
        # Debe esperar
        tiempo_espera_opcion_2 += (ocupacion_DB_unica - tiempo)
        tiempo_total_opcion_2 += (ocupacion_DB_unica - tiempo + tiempo_atencion_db_unica)
        ocupacion_DB_unica += tiempo_atencion_db_unica
    i += 1

print "Tiempo medio de espera"
print("\tOpcion 1 %.3f" % (tiempo_espera_opcion_1 / (10000 - solicitudes_sin_espera_opcion_1)))
print("\tOpcion 2 %.3f" % (tiempo_espera_opcion_2 / (10000 - solicitudes_sin_espera_opcion_2)))

print "\nFracción de de solicitudes que no esperaron para ser atendidad"
print("\tOpcion 1 %.3f%%" % (solicitudes_sin_espera_opcion_1 / 100))
print("\tOpcion 2 %.3f%%" % (solicitudes_sin_espera_opcion_2 / 100))

print "\nSelección de la opciones"
print("\tEl tiempo total de la opcion 1 es de:  %f" % tiempo_total_opcion_1)
print("\tEl tiempo total de la opcion 2 es de:  %f" % tiempo_total_opcion_2)
relacion_tiempos = (1 - (tiempo_total_opcion_1 / tiempo_total_opcion_2)) * 100
if (relacion_tiempos >= 50):
    print ("\tComo el tiempo de la opción 1 es un %.0f%% menor elijo la opción 1" % relacion_tiempos)
else:
    print ("\tComo el tiempo de la opción 1 es sólo un %.0f%% menor elijo la opción 2" % relacion_tiempos)