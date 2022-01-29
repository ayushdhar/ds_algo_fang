from typing import List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def display_ll(head: Node) -> None:
    curr = head

    while curr:
        print(curr.value, end=" -> ")
        curr = curr.next
    print("X")


def ll_sorted_insert(head: Node, value: int) -> Node:
    new_node = Node(value)
    if not head:
        return new_node
    curr = head
    prev = None

    while curr:
        if curr.value > value:
            if prev:
                prev.next = new_node
                new_node.next = curr
            else:
                head = new_node
                new_node.next = curr
            return head
        prev = curr
        curr = curr.next
    prev.next = new_node
    return head


def ll_search(head: Node, value: int) -> Optional[Node]:
    curr = head

    while curr:
        if curr.value == value:
            return curr
        curr = curr.next
    return None


def ll_delete(head: Node, value: int) -> Optional[Node]:
    curr = head
    prev = None
    while curr:
        if curr.value == value:
            if prev:
                prev.next = curr.next
                del curr

            else:
                head = head.next
                del curr
            return head
        prev = curr
        curr = curr.next
    return head


class ChainedHash:
    @staticmethod
    def __hash_function(value):
        return value % 10

    def __init__(self, size):
        self.ds: List[Optional[Node]] = [None for _ in range(size)]

    def insert(self, value: int):
        self.ds[self.__hash_function(value)] = ll_sorted_insert(head=self.ds[self.__hash_function(value)], value=value)

    def search(self, value):
        return ll_search(head=self.ds[self.__hash_function(value)], value=value) is not None

    def delete(self, value):
        self.ds[self.__hash_function(value)] = ll_delete(head=self.ds[self.__hash_function(value)], value=value)


h = ChainedHash(10)

h.insert(16)
h.insert(12)
h.insert(25)
h.insert(39)
h.insert(6)
h.insert(122)
h.insert(5)
h.insert(68)
h.insert(75)
h.delete(75)
print(display_ll(h.ds[5]))
