from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalHelper(self, node: Optional[TreeNode], res: list):
        if node:
            self.inorderTraversalHelper(node.left, res)
            res.append(node.val)
            self.inorderTraversalHelper(node.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorderTraversalHelper(root, res)
        return res
