class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next = None


def display_ll(head: Node) -> None:
    curr = head

    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("X")


def display_ll_rec(head: Node) -> None:
    if head:
        print(head.data, end=" -> ")
        display_ll_rec(head.next)
    else:
        print("X")


def count_ll_nodes(head: Node) -> int:
    if head:
        return count_ll_nodes(head.next) + 1
    else:
        return 0


def sum_ll_rec(head: Node) -> int:
    if head:
        return head.data + sum_ll_rec(head.next)
    return 0


def sum_ll_it(head: Node) -> int:
    curr = head
    sum = 0

    while curr:
        sum += curr.data
        curr = curr.next
    return sum


def max_ll_rec(head: Node, max_elem: int) -> int:
    if head:
        max_elem = max(max_elem, head.data)
        return max_ll_rec(head.next, max_elem)
    return max_elem


def search_ll_rec(head: Node, elem: int) -> bool:
    if head:
        if head.data == elem:
            return True
        else:
            return search_ll_rec(head.next, elem)
    return False


def search_ll_opt(head: Node, elem: int) -> int:
    curr = head
    prev = head

    while curr:
        if curr.data == elem:
            if curr != head:
                prev.next = curr.next
                curr.next = head
                temp = head
                head = curr
                head.next = temp
            return curr.data
        prev = curr
        curr = curr.next
    return -1


def insert_at_head(head: Node, elem: int):
    new_node = Node(elem)
    temp = head

    new_node.next = temp
    temp = new_node


def insert_at_tail(head: Node, elem: int):
    new_node = Node(elem)
    curr = head

    while curr.next:
        curr = curr.next
    curr.next = new_node


if __name__ == "__main__":
    new_node = Node(data=4)
    new_node.next = Node(data=6)
    new_node.next.next = Node(data=1)
    new_node.next.next.next = Node(data=2)
    new_node.next.next.next.next = Node(data=3)
    new_node.next.next.next.next.next = Node(data=23)
    new_node.next.next.next.next.next.next = Node(data=7)

    head = new_node
    insert_at_head(head=head, elem=45)
    display_ll(head=head)
    insert_at_tail(head=head, elem=45)
