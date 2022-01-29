# Definition for a Node.

from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect_(self, root: 'Node') -> 'Node':

        node = root

        while node:
            node.left.next = node.right
        ...

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            prev = None

            for i in range(size):
                elem = queue.popleft()
                if prev:
                    prev.next = elem
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
                prev = elem
        return root
