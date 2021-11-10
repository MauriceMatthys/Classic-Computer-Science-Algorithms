class BinaryHeap:

    def __init__(self, max_size=100):
        self.max = max_size
        self.nb = 0
        self.arr = [0]

    def empty(self):
        return self.nb == 0

    def get_min_elem(self):
        return self.arr[1]

    def insert_elem(self, elem):
        if self.nb == self.max:
            print("binary heap is full")
            return
        self.nb = self.nb + 1
        index = self.nb
        self.arr.append(elem)
        while self.arr[index // 2] > self.arr[index] and index > 1:
            temp = self.arr[index]
            self.arr[index] = self.arr[index // 2]
            self.arr[index // 2] = temp
            index //= 2

    def remove_min_elem(self):
        if self.nb < 1:
            print("binary heap is full")
            return
        result = self.arr[1]
        self.nb = self.nb - 1
        if self.nb > 0:
            self.arr[1] = self.arr.pop()
        else:
            self.arr.pop()
        index = 1

        while index * 2 <= self.nb and self.arr[index] > self.arr[index * 2]:
            if index * 2 + 1 <= self.nb and self.arr[index * 2 + 1] < self.arr[index * 2]:
                temp = self.arr[index]
                self.arr[index] = self.arr[index * 2 + 1]
                self.arr[index * 2 + 1] = temp
                index = index * 2 + 1

            else:
                temp = self.arr[index]
                self.arr[index] = self.arr[index * 2]
                self.arr[index * 2] = temp
                index *= 2

        return result

    def __str__(self):
        dummy = self.arr.copy()
        dummy.pop(0)
        return str(dummy)
