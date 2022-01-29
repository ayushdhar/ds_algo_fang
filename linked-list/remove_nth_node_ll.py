# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        prev = None

        while n > 0:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = slow.next
            del slow
        elif slow.next:
            return slow.next
        else:
            return None
        return head
