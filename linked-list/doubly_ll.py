class DoubleNode:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


def insert_at_head_ll(head: DoubleNode, value: int) -> DoubleNode:
    new_node = DoubleNode(data=value)

    new_node.next = head
    head.prev = new_node
    head = new_node

    return head


def insert_at_pos(head: DoubleNode, val: int, pos: int):
    curr = head
    new_node = DoubleNode(val)
    curr_pos = 0
    if not head:
        return new_node
    elif pos == 0:
        new_node.next = head
        head.prev = new_node
        head = new_node
        return head
    else:

        while curr_pos < pos - 1:
            curr = curr.next
            curr_pos += 1

        curr.prev.next = new_node
        new_node.prev = curr.prev
        new_node.next = curr
        curr.prev = new_node

        return head


def delete_ll(head: DoubleNode, pos: int):
    curr = head
    curr_pos = 0

    if pos == 0:
        head = head.next
        head.prev = None
        return head

    while curr_pos != pos:
        curr = curr.next
        curr_pos += 1

    curr.prev.next = curr.next
    if curr.next:
        curr.next.prev = curr.prev
    del curr
    return head


def rev_db_ll(head: DoubleNode) -> DoubleNode:
    curr = head

    if head.next:
        while curr:
            curr.next, curr.prev = curr.prev, curr.next
            prev = curr
            curr = curr.prev

        return prev
    else:
        return head


def display_dll(head: DoubleNode):
    curr = head

    while curr:
        print(curr.data)
        curr = curr.next


data = [1, 3, 67, 2, 15]
head = DoubleNode(4)

for i in data:
    head = insert_at_head_ll(head=head, value=i)

display_dll(head=rev_db_ll(head=head))
