class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def display_ll(head: LinkedList) -> None:
    curr = head

    while curr:
        print(curr.value, end=" -> ")
        curr = curr.next
    print("X")


def reverse_ll(head: LinkedList) -> LinkedList:
    if not head or not head.next:
        return head

    prev, curr = None, head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def get_middle_LinkedList_ll(head: LinkedList):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    if fast:
        return slow.next
    return slow


def zipLinkedList(linkedList):
    middle_node = get_middle_LinkedList_ll(head=linkedList)
    rev_middle_head = reverse_ll(middle_node)
    curr, curr_rev = linkedList, rev_middle_head

    while curr_rev:
        next = curr.next
        next_rev = curr_rev.next
        curr.next = curr_rev
        curr_rev.next = next
        curr = next
        curr_rev = next_rev
    next.next = None

    return linkedList


if __name__ == "__main__":
    new_LinkedList = LinkedList(value=4)
    new_LinkedList.next = LinkedList(value=6)
    new_LinkedList.next.next = LinkedList(value=1)
    new_LinkedList.next.next.next = LinkedList(value=2)
    new_LinkedList.next.next.next.next = LinkedList(value=3)
    new_LinkedList.next.next.next.next.next = LinkedList(value=23)
    # new_LinkedList.next.next.next.next.next.next = LinkedList(value=7)
    # display_ll(get_middle_LinkedList_ll(head=new_LinkedList))

    display_ll(zipLinkedList(new_LinkedList))
