import simpy
import random


def atencion(env, atm):
    contador_clientes = 1
    media_arribo = 0
    while True:
        print("Cliente %d en el tiempo %d" % (contador_clientes, env.now))

        if env.now < 120:
            media_arribo = 240
        elif env.now >= 120 and env.now < 300:
            media_arribo = 120
        else:
            media_arribo = 360

        # Llegada de un cliente
        llegada_cliente = random.expovariate(media_arribo)
        yield env.timeout(llegada_cliente)
        # Levantar la berrera tarda tiempo_barrera
        tiempo_atm = calcular_tiempo_atm
        with atm.request() as req:
            yield req
            yield env.timeout(tiempo_atm)

        contador_clientes = contador_clientes + 1


def calcular_tiempo_atm():
    tiempo_estacionar = 8
    yield env.timeout(tiempo_estacionar)


enviroment = simpy.Environment()
atm = simpy.Resource(enviroment, capacity=1)
enviroment.process(atencion(enviroment, atm))

enviroment.run(until=600)
