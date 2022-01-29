from collections import deque


class Stack:

    def __init__(self):
        self.data = []

    @property
    def top(self):
        if not self.is_empty:
            return self.data[-1]
        return -1

    @property
    def is_empty(self):
        return not self.data

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        if not self.is_empty:
            return self.data.pop()
        return -1


s = Stack()

s.push(6)
s.push(1)
s.push(2)
s.push(9)
s.push(3)

while s.pop() != -1:
    pass
print(s.top)
