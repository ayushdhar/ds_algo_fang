from node import Node


def linked_list_loop(head: Node) -> bool:
    if not head:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow.data == fast.data:
            return True
    return False
