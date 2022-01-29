from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def ll_prepend(head: Node, val):
    new_node = Node(val)

    if not head:
        return new_node
    new_node.next = head
    head = new_node
    return head



def ll_to_list(head: Node):
    curr = head
    res = []
    while curr:
        res.append(curr.val)
        curr = curr.next

    return res


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        node = root
        q.append(node)
        res = []
        level_value = 1
        while q:
            level = None if level_value % 2 == 0 else []
            size = len(q)

            for _ in range(size):
                elem: TreeNode = q.popleft()
                if level_value % 2 == 0:
                    level = ll_prepend(level, elem.val)
                else:
                    level.append(elem.val)

                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
            if level_value % 2 == 0:
                level = ll_to_list(level)
            res.append(level)
            level_value += 1
        return res
