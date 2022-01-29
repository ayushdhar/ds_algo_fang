class Queue:
    @property
    def length(self):
        return len(self.ds)

    def __init__(self):
        self.ds = []

    def shift_at_start(self):
        for i in range(self.length-1):
            self.ds[i] = self.ds[i + 1]
        del self.ds[self.length - 1]

    def enqueue(self, elem):
        self.ds.append(elem)

    def dequeue(self):
        if self.length > 1:
            self.shift_at_start()
        elif self.length == 1:
            del self.ds[0]

    def print(self):
        for i in range(self.length):
            print(self.ds[i]),


q = Queue()

q.enqueue(5)
q.enqueue(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(6)

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(7)
q.enqueue(8)
q.dequeue()
q.dequeue()
q.print()
