from doubly_ll import DoubleNode


def rev_db_ll(head: DoubleNode) -> DoubleNode:
    curr = head

    if head.next:
        while curr.prev:
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev
        head = curr

    return head
