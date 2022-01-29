# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_ll_rec(prev, curr: ListNode):
    if curr:
        rev_head = reverse_ll_rec(curr, curr.next)
        curr.next = prev
        return rev_head
    else:
        return prev


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        is_odd = fast is not None

        mid = slow

        if is_odd:
            curr = mid.next
        else:
            curr = mid
        prev = None

        mid = reverse_ll_rec(prev, curr)

        curr1 = head
        curr2 = mid
        while curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        return True
