from node import Node


def display_ll(head: Node) -> None:
    curr = head

    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("X")


def insert_at_head(head: Node, elem):
    new_node = Node(elem)

    if not head:
        head = new_node
    else:
        new_node.next = head
        head = new_node
    return head


def reverse_ll(head: Node):
    rev_head = None

    curr = head

    while curr:
        rev_head = insert_at_head(head=rev_head, elem=curr.data)
        curr = curr.next
    return rev_head


def reverse_ll_opt(head: Node):
    if not head.next:
        return head
    l, r, curr = None, None, head.next

    while r:
        r.next = l
        l = r
        r = curr
        if curr:
            curr = curr.next
    return l


def reverse_ll_rec(prev, curr: Node):
    if curr:
        rev_head = reverse_ll_rec(curr, curr.next)
        curr.next = prev
        return rev_head
    else:
        return prev


if __name__ == "__main__":
    new_node = Node(data=4)
    new_node.next = Node(data=6)
    new_node.next.next = Node(data=1)
    new_node.next.next.next = Node(data=2)
    new_node.next.next.next.next = Node(data=3)
    new_node.next.next.next.next.next = Node(data=23)
    new_node.next.next.next.next.next.next = Node(data=7)

    display_ll(reverse_ll_rec(prev=None, curr=new_node))
