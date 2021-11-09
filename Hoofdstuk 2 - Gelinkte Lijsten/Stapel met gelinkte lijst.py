class StackList:
    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    def __init__(self):
        self.t = None

    def empty(self):
        return self.t is None

    def push(self, data):
        hulp = self.Knoop()
        hulp.data = data
        hulp.volgende = self.t
        self.t = hulp

    def peek(self):
        return self.t.data

    def pop(self):
        x = self.t.data
        self.t = self.t.volgende
        return x




