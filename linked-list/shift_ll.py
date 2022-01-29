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


def get_tail(head: LinkedList):
    curr = head

    while curr.next:
        curr = curr.next

    return curr


def shiftLinkedList(head: LinkedList, k):
    if not head or not head.next or k == 0:
        return head
    tail = get_tail(head)
    is_pos = k > 0
    k = abs(k)

    while k > 0:

        if is_pos:
            curr = head
            prev = None

            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            curr.next = head
            head = curr

        else:
            temp = head
            head = head.next
            tail.next = temp
            temp.next = None
            tail=temp
        k -= 1
    return head


head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)

display_ll(shiftLinkedList(head, -2))