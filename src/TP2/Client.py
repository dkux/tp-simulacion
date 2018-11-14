import numpy
from random import randint

class Client(object):

    petition_duration = {
        'A': randint(60, 180),
        'B': randint(120, 360),
        'C': randint(200, 800)
    }

    def __init__(self, env, numero):
        self.env = env
        self.type = numpy.random.choice(['A', 'B', 'C'], p=[0.7, 0.2, 0.1])
        self.numero = numero

    def petition(self, checkout):
        yield self.env.process(checkout.serve(self))

    def get_petition_duration(self):
        return self.petition_duration[self.type]    