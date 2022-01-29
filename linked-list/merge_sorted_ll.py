from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        elif l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2
        else:
            l3 = l1 if l1.val <= l2.val else l2
            curr1, curr2, curr3 = l1, l2, l3
            if l3 == l1:
                curr1 = curr1.next
            else:
                curr2 = curr2.next
            while curr1 and curr2:
                if curr1.val <= curr2.val:
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
