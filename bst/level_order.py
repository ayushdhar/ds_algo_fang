from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        node = root
        q.append(node)
        res = []
        while q:
            level = []
            size = len(q)

            for _ in range(size):
                elem: TreeNode = q.popleft()
                level.append(elem.val)

                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
            res.append(level)
        return res
