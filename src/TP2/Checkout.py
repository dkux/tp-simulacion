import numpy
import simpy


class Checkout(object):
    def __init__(self, env, count):
        self.env = env
        self.count = count
        #ACA esta La clave para multiples recursos
        self.servers = [simpy.Resource(env) for x in range(count)]

    def serve_A(self, client):
        server = self.select_server_A()
        with server.request() as req:
            yield req
            yield self.env.timeout(client.get_petition_duration())
    
    def serve_B(self, client):
        server = self.select_server_B()
        with server.request() as req:
            yield req
            yield self.env.timeout(client.get_petition_duration())


    def select_server_A(self):
        queues = []

        for x in self.servers:
            if (x.count == 0) and (len(x.queue) == 0):
                return x
            else:
                queues.append(len(x.queue))
        return self.servers[numpy.array(queues).argmin()]


    def select_server_B(self):
        #Para el Round Robin
        for x in self.servers:
            pass
        