import Pyro4

@Pyro4.expose
class StringConcatenator(object):

    def concatenate(self, str1, str2):
        return str1 + " " + str2

daemon = Pyro4.Daemon()

uri = daemon.register(StringConcatenator)

print("Server URI :", uri)

daemon.requestLoop()