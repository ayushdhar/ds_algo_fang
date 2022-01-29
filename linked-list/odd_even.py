# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_tail(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head

    while curr.next:
        curr = curr.next
    return curr


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        tail = get_tail(head)
        curr = head
        count = 1
        prev = None
        while curr:
            if curr == init_tail:
                if count % 2 == 0:
                    prev.next = curr.next
                    curr.next = None
                    curr_tail.next = curr
                    curr_tail = curr
                break
            if count % 2 == 0:
                prev.next = curr.next
                curr.next = None
                curr_tail.next = curr
                curr_tail = curr
            prev = curr
            curr = curr.next
            count += 1
        return head
