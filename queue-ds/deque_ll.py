class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Deque:
    def __init__(self):
        self.f = None
        self.r = None

    def insert_from_front(self, elem):
        new_node = Node(elem)

        if self.f:
            new_node.next = self.f
            self.f = new_node
        else:
            self.f = self.r = new_node

    def delete_from_front(self):
        if self.f:
            temp = self.f
            self.f = self.f.next
            del temp
        else:
            print("Queue empty, can't delete!!")

    def insert_from_rear(self, elem):
        new_node = Node(elem)
        if self.r:
            self.r.next = new_node
            self.r = new_node
        else:
            self.f = self.r = new_node

    def delete_from_rear(self):
        if self.f == self.r and self.r:
            self.f = self.r = None
        elif self.r:
            curr = self.f
            while curr.next != self.r:
                curr = curr.next
            self.r = curr
            self.r.next = None
        else:
            print("Queue empty, can't delete!!")

    def print(self):
        curr = self.f
        while curr:
            print(f"{curr.data}", end="--")
            curr = curr.next


q = Deque()
q.insert_from_front(5)
q.insert_from_front(1)
q.insert_from_front(2)
q.insert_from_front(3)
q.insert_from_front(4)
q.delete_from_front()
q.delete_from_front()
q.delete_from_front()
q.delete_from_front()
q.delete_from_rear()
q.print()
