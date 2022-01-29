class LinkedList:
    def __init__(self, valueue):
        self.valueue = valueue
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    l1, l2 = headOne, headTwo
    if not l1 and not l2:
        return None
    elif l1 and not l2:
        return l1
    elif not l1 and l2:
        return l2
    else:
        l3 = l1 if l1.value <= l2.value else l2
        curr1, curr2, curr3 = l1, l2, l3
        if l3 == l1:
            curr1 = curr1.next
        else:
            curr2 = curr2.next
        while curr1 and curr2:
            if curr1.value <= curr2.value:
                curr3.next = curr1
                curr1 = curr1.next
                curr3 = curr3.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
                curr3 = curr3.next
        if curr1:
            curr3.next = curr1
        elif curr2:
            curr3.next = curr2
        return l3

