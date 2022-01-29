from node import Node


def display_ll(head: Node) -> None:
    curr = head

    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("X")


def delete_from_ll(head: Node, elem: int) -> Node:
    if head.data == elem:
        temp = head.next
        del head
        return temp

    curr = prev = head

    while curr:
        if curr.data == elem:
            prev.next = curr.next
            del curr
            break
        prev = curr
        curr = curr.next
    return head


if __name__ == "__main__":
    new_node = Node(data=4)
    new_node.next = Node(data=6)
    new_node.next.next = Node(data=1)
    new_node.next.next.next = Node(data=2)
    new_node.next.next.next.next = Node(data=3)
    new_node.next.next.next.next.next = Node(data=23)
    new_node.next.next.next.next.next.next = Node(data=7)

    display_ll(delete_from_ll(new_node, 4))
    # display_ll(delete_from_ll(new_node, 7))
    display_ll(delete_from_ll(new_node, 1))
