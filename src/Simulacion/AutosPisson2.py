import simpy
import random

#En este caso no espero a estacionar el auto para que ingrese el siguiente
def llegada(env):
    index = 1
    while True:
        print("Auto %d en el tiempo %d" % (index, env.now))
        #Los autos llegan con dist Poisson de lambda 2
        llegada_auto = random.expovariate(1 / 2.0)
        yield env.timeout(llegada_auto)
        index = index + 1


def estacionamiento(env):
    index = 1
    while True:
        print("Auto %d estacionado en el tiempo %d" % (index, env.now))
        tiempo_estacionar = 3
        yield env.timeout(tiempo_estacionar)
        index = index + 1

enviroment = simpy.Environment()
enviroment.process(llegada(enviroment))
enviroment.process(estacionamiento(enviroment))
enviroment.run(until=600)
