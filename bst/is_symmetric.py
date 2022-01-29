from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def is_symmetric_helper(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if node1 and node2:
            if node1.val != node2.val:
                return False
            return self.is_symmetric_helper(node1.left, node2.right) and self.is_symmetric_helper(node1.right,
                                                                                                  node2.left)
        elif (node1 is None) or (node2 is None):
            return False
        else:
            return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        else:
            return self.is_symmetric_helper(root.left, root.right)


print(int(1/2))