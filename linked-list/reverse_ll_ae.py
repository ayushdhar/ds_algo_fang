# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head: LinkedList):
    if not head or not head.next:
        return head

    anchor = head
    curr = head.next

    while curr:
        anchor.next = curr.next
        curr.next = head
        head = curr
        curr = anchor.next

    return head

