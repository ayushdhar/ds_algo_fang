class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stack_a = []
        stack_b = []

        curr_a = headA
        curr_b = headB

        while curr_a:
            stack_a.append(curr_a)
            curr_a = curr_a.next
        while curr_b:
            stack_b.append(curr_b)
            curr_b = curr_b.next
        prev_pop, pop_a, pop_b = None, stack_a.pop(), stack_b.pop()
        while stack_a and stack_b:
            prev_pop = pop_a
            pop_a, pop_b = stack_a.pop(), stack_b.pop()
            if pop_a != pop_b:
                break
        return prev_pop
