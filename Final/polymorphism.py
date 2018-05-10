class a:
    def __init__(self):
        pass
    def printMessage(self, msg):
        print(msg)


class b(a):
    def __init__(self):
        a.__init__(self)

    a.printMessage(a, "Hello world")

b()
