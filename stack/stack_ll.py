class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class StackLl:
    def __init__(self):
        self.head = None

    def push(self, elem):
        new_node = Node(elem)

        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def pop(self):
        if self.head and self.head.next:
            popped = self.head.data
            self.head = self.head.next
            return popped

        elif self.head:
            popped = self.head.data
            self.head = None
            return popped
        else:
            return -1

    @property
    def top(self):
        if self.head:
            return self.head.data
        else:
            return -1

    def is_empty(self):
        return self.head is None


s = StackLl()
s.push(6)
s.push(1)
s.push(2)
s.push(9)
s.push(3)


print(s.top)
