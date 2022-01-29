from node import Node


def display_ll(head: Node) -> None:
    curr = head

    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("X")


def insert_in_sorted_ll(head: Node, elem: int):
    new_node = Node(elem)
    curr = prev = head
    inserted = False

    if elem < head.data:
        temp = head
        head = new_node
        new_node.next = temp
        inserted = True

    while not inserted and curr:
        if new_node.data < curr.data:
            prev.next = new_node
            new_node.next = curr
            inserted = True
            break
        prev = curr
        curr = curr.next
    if not inserted:
        prev.next = new_node
    return head


if __name__ == "__main__":
    new_node = Node(data=4)
    new_node.next = Node(data=5)
    new_node.next.next = Node(data=8)
    new_node.next.next.next = Node(data=20)
    new_node.next.next.next.next = Node(data=45)
    new_node.next.next.next.next.next = Node(data=60)



    display_ll(head=insert_in_sorted_ll(head=new_node, elem=3))
