import simpy
from random import randint


def atencion(env):
    index = 1
    while index <= 50:
        print("Atendiendo al cliente %d en el tiempo %d" % (index , env.now))
        tiempo_atencion = randint(2, 7)
        yield env.timeout(tiempo_atencion)
        index = index + 1

enviroment = simpy.Environment()

enviroment.process(atencion(enviroment))
enviroment.run()
