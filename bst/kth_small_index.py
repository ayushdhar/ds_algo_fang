# Definition for a binary tree node.
from typing import Optional


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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        self.inorderTraversalHelper(root, inorder)
        return inorder[-k]
