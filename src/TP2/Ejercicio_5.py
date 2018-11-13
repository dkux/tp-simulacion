#!/usr/bin/python
# coding=utf-8
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import simpy

from Checkout import Checkout
from Client import Client


client_count = 200
arrival_rate = random.expovariate(1/45)
server_count = 5


def generate_clients(environment, count, interval, checkout):
    for i in range(count):
        client = Client(env)
        environment.process(client.petition(checkout))
        t = random.expovariate(1.0 / interval)
        yield environment.timeout(t)


env = simpy.Environment()
checkout = Checkout(env, server_count)
env.process(generate_clients(env, client_count, arrival_rate, checkout))
env.run()