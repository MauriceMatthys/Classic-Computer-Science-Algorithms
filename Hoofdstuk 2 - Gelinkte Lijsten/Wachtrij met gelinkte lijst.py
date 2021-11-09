class QueueList:
    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    def __init__(self):
        self.kop = None
        self.staart = None

    def empty(self):
        return (self.kop is None)

    def enqueue(self, dataElement):
        hulp = self.Knoop()
        hulp.data = dataElement
        hulp.volgende = None
        if self.kop is None:
            self.kop = hulp
            self.staart = hulp
        else:
            self.staart.volgende = hulp
            self.staart = hulp

    def front(self):
        if self.kop is None:
            return None
        return self.kop.data

    def dequeue(self):
        if self.kop is None:
            return None
        data = self.kop.data
        if self.kop == self.staart:
            self.kop = None
            self.staart = None
        else:
            self.kop = self.kop.volgende
        return data

    def invert(self):
        vorige = None
        huidige = self.kop
        while huidige != None:
            volgende = huidige.volgende
            huidige.volgende = vorige
            vorige = huidige
            huidige = volgende
        self.kop, self.staart = self.staart, self.kop
