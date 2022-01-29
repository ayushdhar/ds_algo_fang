from collections import deque
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, elem):
        new_node = Node(elem)
        if not self.first and not self.last:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def deque(self):
        if self.first:
            temp = self.first
            self.first = self.first.next
            del temp

        else:
            print("queue-ds empty cant deque")

    def print(self):
        curr = self.first
        while curr:
            print(f"{curr.data}", end="--")
            curr = curr.next


q = LinkedQueue()

q.enqueue(5)
q.enqueue(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(6)
q.deque()
q.deque()
q.deque()
q.deque()
q.deque()
q.deque()
q.deque()
q.print()

