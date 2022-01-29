from node import Node


def remove_dups_ll(head: Node):
    if not head or not head.next:
        return head

    prev = head
    curr = head.next

    while curr:

        if prev.data == curr.data:
            prev.next = curr.next
            del curr
            curr = prev.next
        else:
            prev = curr
            curr = curr.next
    return head


def display_ll(head: Node) -> None:
    curr = head

    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("X")


if __name__ == "__main__":
    new_node = Node(data=3)
    new_node.next = Node(data=5)
    new_node.next.next = Node(data=5)
    new_node.next.next.next = Node(data=8)
    new_node.next.next.next.next = Node(data=8)
    new_node.next.next.next.next.next = Node(data=8)
    new_node.next.next.next.next.next.next = Node(data=8)

    display_ll(head=remove_dups_ll(new_node))
