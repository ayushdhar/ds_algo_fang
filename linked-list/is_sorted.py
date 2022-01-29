from node import Node


def is_sorted(head: Node) -> bool:
    if not head.next:
        return True

    prev = head
    curr = head.next

    while curr:
        if prev.data > curr.data:
            return False
        prev = curr
        curr = curr.next
    return True


if __name__ == "__main__":
    new_node = Node(data=1)
    new_node.next = Node(data=3)
    new_node.next.next = Node(data=2)
    new_node.next.next.next = Node(data=4)
    new_node.next.next.next.next = Node(data=5)
    new_node.next.next.next.next.next = Node(data=6)
    new_node.next.next.next.next.next.next = Node(data=7)

    print(is_sorted(head=new_node))
