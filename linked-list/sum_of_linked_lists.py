import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_ll(head: LinkedList):
    curr = head

    while curr:
        print(curr.value, end="->")
        curr = curr.next


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    curr_one = linkedListOne
    curr_two = linkedListTwo
    head_new = None
    curr_new = None
    carry = 0

    while curr_one or curr_two or carry != 0:
        value_one = curr_one.value if curr_one else 0
        value_two = curr_two.value if curr_two else 0
        sum = value_one + value_two + carry

        new_value = sum % 10
        carry = sum // 10
        new_node = LinkedList(new_value)

        if not head_new:
            head_new = new_node
            curr_new = head_new
        else:
            curr_new.next = new_node
            curr_new = curr_new.next
        curr_one = curr_one.next if curr_one else None
        curr_two = curr_two.next if curr_one else None

    return head_new


class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


ll1 = LinkedList(2).addMany([4, 7, 1])
ll2 = LinkedList(9).addMany([4, 5])

print_ll(sumOfLinkedLists(ll1, ll2))
