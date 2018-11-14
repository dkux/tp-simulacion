# coding=utf-8
import random
import simpy

from Checkout import Checkout
from Client import Client


client_count = 200
arrival_rate = 45.0
server_count = 5
contador_clientes = 1


def generate_clients(environment, interval, checkout):
    global contador_clientes
    contador_clientes = 1
    while True:
        client = Client(env, contador_clientes)
        environment.process(client.petition(checkout))
        t = random.expovariate(1.0 / interval)
        yield environment.timeout(t)
        contador_clientes = contador_clientes + 1


env = simpy.Environment()
checkout = Checkout(env, server_count, 1)
env.process(generate_clients(env, arrival_rate, checkout))
env.run(until=10000)

print "Load Balancer Opcion a:"
print "\tEn 10 segundos se procesaron %d clientes" % contador_clientes
print "\tEl tamaño máximo de la cola fue de %d " % checkout.max_queue_length
print "\tEl tiempo máximo en la cola fue de %.2f ms" % checkout.max_queue_time

env = simpy.Environment()
checkout = Checkout(env, server_count, 2)
env.process(generate_clients(env, arrival_rate, checkout))
env.run(until=10000)

print "\n"
print "Load Balancer Opcion b:"
print "\tEn 10 segundos se procesaron %d clientes" % contador_clientes
print "\tEl tamaño máximo de la cola fue de %d " % checkout.max_queue_length
print "\tEl tiempo máximo en la cola fue de %.2f ms" % checkout.max_queue_time