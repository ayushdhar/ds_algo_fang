# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: TreeNode, res: list):
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        helper = []

        inorder(root, helper)

        for i in range(1, len(helper)):
            if helper[i] <= helper[i - 1]:
                return False

        return True
