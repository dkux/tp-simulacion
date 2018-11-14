# coding=utf-8
import simpy
import random

max_wait_time = 0


def atencion(env, atm):
    max_queue_length = 0
    while True:
        # El timpo comienza en 0 y se mide en segundos

        if env.now < 120*60:
            # Estoy en el rango de 10:00 a 12:00 se transforma en tiempo entre 0 y 120*60 segundos
            media_arribo = 240.0
        elif 120*60 < env.now <= 300*60:
            # Estoy en el rango de 12:00 a 15:00 se transforma en tiempo entre 120*60 y 300*60 segundos
            media_arribo = 120.0
        elif 300*60 < env.now < 540*60:
            # Estoy en el rango de 15:00 a 19:00 se transforma en tiempo entre 3000*60 y 540*60 segundos
            media_arribo = 360.0
        else:
            break
        llegada_cliente = random.expovariate(1/media_arribo)
        yield env.timeout(llegada_cliente)

        env.process(usar_atm(env, atm))
        if len(atm.queue) > max_queue_length:
            max_queue_length = len(atm.queue)

    print("El tamaño maximo de la cola fue de %d personas" % max_queue_length)
    print("El tiempo maximo en la cola fue de %7.4f minutos" % (max_wait_time/60.0))


def usar_atm(env, atm):
    global max_wait_time
    tipo = random.random
    queue_time = env.now
    if tipo < 0.1:
        tiempo_proceso = random.randint(1*60, 7*60)
    elif 0.1 >= tipo < 0.8:
        tiempo_proceso = random.randint(1*60, 3*60)
    else:
        tiempo_proceso = random.randint(1*60, 5*60)
    with atm.request() as req:
        yield req
        yield env.timeout(tiempo_proceso)
    queue_time = env.now - queue_time
    if queue_time > max_wait_time:
        max_wait_time = queue_time


environment = simpy.Environment()
atm = simpy.Resource(environment, capacity=1)
environment.process(atencion(environment, atm))
environment.run()


