import numpy
import simpy


class Checkout(object):
    def __init__(self, env, count, load_balancer_type):
        self.env = env
        self.count = count
        self.servers = [simpy.Resource(env) for x in range(count)]
        self.max_queue_length = 0
        self.max_queue_time = 0
        self.load_balancer_type = load_balancer_type

    def serve(self, client):
        if self.load_balancer_type == 1:
            server = self.selectServerOptionA()
        else:
            server = self.selectServerOptionB(client)
        queue_time = self.env.now
        with server.request() as req:
            yield req
            yield self.env.timeout(client.get_petition_duration())
        queue_time = self.env.now - queue_time
        if queue_time > self.max_queue_time:
            self.max_queue_time = queue_time

    def selectServerOptionA(self):
        queues = []
        for x in self.servers:
            if (x.count == 0) and (len(x.queue) == 0):
                return x
            else:
                queues.append(len(x.queue))
        if self.max_queue_length < numpy.array(queues).argmax():
            self.max_queue_length = numpy.array(queues).argmax()

        return self.servers[numpy.array(queues).argmin()]

    def selectServerOptionB(self, client):
        server_number = client.numero % self.count
        queues = []
        if (self.servers[server_number].count == 0) and (len(self.servers[server_number].queue) == 0):
            return self.servers[server_number]
        else:
            queues.append(len(self.servers[server_number].queue))
        if self.max_queue_length < numpy.array(queues).argmax():
            self.max_queue_length = numpy.array(queues).argmax()

        return self.servers[numpy.array(queues).argmin()]
