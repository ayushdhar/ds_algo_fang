from node import Node


def circular_ll_display(head: Node):
    if not head:
        return
    curr = head
    has_displayed_all = False

    while not has_displayed_all:
        print(curr.data, end=" -> "),
        curr = curr.next
        if curr == head:
            has_displayed_all = True


def circular_ll_display_rec(curr: Node, head: Node):
    print(curr.data, end=" -> ")
    if curr.next != head:
        circular_ll_display_rec(curr.next, head)


def circular_ll_insert(head: Node, data: int, pos: int):
    prev = curr = head
    new_node = Node(data)
    curr_pos = 1

    while True:
        if curr_pos == pos:
            prev.next = new_node
            new_node.next = curr
        prev = curr
        curr = curr.next
        curr_pos += 1
        if curr == head:
            break
    return head


if __name__ == "__main__":
    new_node = Node(data=4)
    new_node.next = Node(data=7)
    new_node.next.next = Node(data=1)
    new_node.next.next.next = Node(data=2)
    new_node.next.next.next.next = Node(data=3)
    new_node.next.next.next.next.next = Node(data=23)
    new_node.next.next.next.next.next.next = new_node

    circular_ll_display(circular_ll_insert(head=new_node, data=36, pos=7))
