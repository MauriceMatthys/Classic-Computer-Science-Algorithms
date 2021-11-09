class HashSet:

    DELETED = 9999
    def __init__(self, max_size=10):
        self.max = max_size
        self.arr = [None] * max_size
        self.nb = 0

    def add(self, item):
        if self.nb == self.max:
            raise ValueError()
        index = hash(item) % self.max
        while self.arr[index] is not None and self.arr[index] != HashSet.DELETED:
            print(index)
            index = (index+1) % self.max
        self.arr[index] = item
        self.nb += 1
        return index

    def index_of(self, item):
        index = hash(item) % self.max
        startIndex = index
        while self.arr[index] != item:
            if self.arr[index] is None:
                return -1
            print(index)
            index = (index+1) % self.max
            if startIndex == index:
                return -1
        return index

    def delete(self, item):
        index = self.index_of(item)
        if index == -1:
            return False
        else:
            self.arr[index] = HashSet.DELETED
            self.nb -= 1
            return True


