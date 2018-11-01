import simpy
import random


def atencion(env, barrera):
    index = 1
    tiempo_barrera = 4
    while True:
        print("Auto %d en el tiempo %d" % (index, env.now))

        # Los autos llegan con dist Poisson de lambda 2
        llegada_auto = random.expovariate(1 / 2.0)
        yield env.timeout(llegada_auto)
        # Levantar la berrera tarda tiempo_barrera
        with barrera.request() as req:
            yield req
            yield env.timeout(tiempo_barrera)

        estacionar(env)
        index = index + 1


def estacionar(env):
    tiempo_estacionar = 8
    yield env.timeout(tiempo_estacionar)


enviroment = simpy.Environment()
barrera = simpy.Resource(enviroment, capacity=1)
enviroment.process(atencion(enviroment, barrera))

enviroment.run(until=600)
