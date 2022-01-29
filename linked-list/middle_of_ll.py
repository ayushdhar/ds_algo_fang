from node import Node


def middle_of_ll(head: Node):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.data


if __name__ == "__main__":
    new_node = Node(data=4)
    new_node.next = Node(data=6)
    new_node.next.next = Node(data=1)
    new_node.next.next.next = Node(data=2)
    new_node.next.next.next.next = Node(data=3)
    new_node.next.next.next.next.next = Node(data=23)
    new_node.next.next.next.next.next.next = Node(data=7)
    new_node.next.next.next.next.next.next.next = Node(data=9)

    print(middle_of_ll(head=new_node))
