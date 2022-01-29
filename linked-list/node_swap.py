# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    if not head or not head.next:
        return head

    curr_a, curr_b, prev = head, head.next, None

    while curr_a and curr_b:
        next_a = curr_a.next.next
        next_b = curr_b.next.next if curr_b.next else None

        curr_b.next = curr_a
        curr_a.next = next_a
        if not prev:
            head = curr_b
        else:
            prev.next = curr_b
        prev = curr_a
        curr_a, curr_b = next_a, next_b
    return head
