from node import Node


def display_ll(head: Node) -> None:
    curr = head

    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("X")


def merge_ll(head1: Node, head2: Node) -> Node:
    return Node()


if __name__ == "__main__":
    new_node = Node(data=2)
    new_node.next = Node(data=8)
    new_node.next.next = Node(data=10)
    new_node.next.next.next = Node(data=15)
    new_node1 = Node(data=4)
    new_node1.next = Node(data=7)
    new_node1.next.next = Node(data=12)
    new_node1.next.next.next = Node(data=14)
    new_node1.next.next.next.next = Node(data=18)
    display_ll(merge_ll(new_node, new_node1))
