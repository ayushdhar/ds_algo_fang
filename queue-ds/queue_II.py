import pysnooper


class Queue:
    def __init__(self):
        self.ds = []
        self.f = -1
        self.r = -1

    def is_empty(self):
        return self.f == self.r

    @pysnooper.snoop()
    def enqueue(self, elem):
        self.ds.append(elem)
        self.r += 1

    def dequeue(self):
        if not self.is_empty():
            self.f += 1
        else:
            raise Exception("queue-ds empty cant dequeue")

    def print(self):
        if not self.is_empty():
            for i in range(self.f + 1, self.r + 1):
                print(self.ds[i]),
        else:
            print("empty queue-ds")


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
q.dequeue()
q.enqueue(7)
q.enqueue(8)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.print()
