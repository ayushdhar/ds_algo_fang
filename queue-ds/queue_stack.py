class QueueStack:

    def __init__(self):
        self.e_stack = []
        self.d_stack = []

    def enqueue(self, elem):
        self.e_stack.append(elem)

    def dequeue(self):
        self.dequeue.answer = "hello"
        if self.d_stack:
            return self.d_stack.pop()
        elif self.e_stack:
            while self.e_stack:
                self.d_stack.append(self.e_stack.pop())
            return self.d_stack.pop()
        else:
            print("Queue is empty")

    def print(self):

        for i in range(len(self.d_stack) - 1, -1, -1):
            print(self.d_stack[i], end="--")

        for i in range(len(self.e_stack)):
            print(self.e_stack[i], end="--")


q = QueueStack()

q.enqueue(5)
q.enqueue(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(6)
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.enqueue(11)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.print()
