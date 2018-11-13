import simpy
import numpy
import random

#En este caso no espero a estacionar el auto para que ingrese el siguiente
def atencion(env, cajeros):
    index = 1
    queues = []
    max_tam_queue = []
    while index <= 1000:

        print("Cliente %d en el tiempo %d- tamaño de la cola" % (index, env.now, queues))
        # Los Personas llegan dist uniforme discreta
        llegada_persona = random.randint(4, 6)
        yield env.timeout(llegada_persona)

        enviroment.process(atencionCliente(env, queues, cajeros))

        index = index + 1


def atencionCliente(env, queues, cajeros):
    # Selecciono un cajero
    cajero_seleccionado = None
    for x in cajeros:
        if (x.count == 0) and (len(x.queue) == 0):
            cajero_seleccionado = x
        else:
            queues.append(len(x.queue))

    if not cajero_seleccionado:
        cajero_seleccionado = cajeros[numpy.array(queues).argmin()]


    with cajero_seleccionado.request() as req:
        yield req
        yield env.timeout(random.randint(6, 14))


cantidad_cajeros = 2
enviroment = simpy.Environment()
cajeros = [simpy.Resource(enviroment) for x in range(cantidad_cajeros)]
enviroment.process(atencion(enviroment, cajeros))
enviroment.run()
