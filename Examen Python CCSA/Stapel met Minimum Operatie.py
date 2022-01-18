class Stack:

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def empty(self):
        return len(self._data) == 0


class StackMin:

    def __init__(self):
        self._data = []
        self._min = []

    def peek(self):
        return self._data[-1]

    def get_minimum(self):
        return self._min[-1]

    def pop(self):
        popped = self._data.pop()
        if popped == self.get_minimum():
            self._min.pop()
        return popped

    def push(self, item):
        self._data.append(item)
        if len(self._min) == 0:
            self._min.append(item)

        elif item <= self.get_minimum():
            self._min.append(item)

    def empty(self):
        return len(self._data) == 0
