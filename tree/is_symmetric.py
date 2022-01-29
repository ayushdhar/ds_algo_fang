from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: TreeNode, res: list):
    node = root

    if node:
        inorder(node.left, res)
        res.append(node.val)
        inorder(node.right, res)

inorder_array = []
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(2)
root.right.left = TreeNode(2)

inorder(root=root, res =inorder_array)
print(inorder_array)

class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        inorder_array = []
        inorder(root, inorder_array)
        inorder_array_length = len(inorder_array)
        if inorder_array_length <= 1:
            return True
        root_elem = root.val
        m = -1
        l, r = 0, 0
        for i in range(inorder_array_length):
            if inorder_array[i] == root_elem:
                m = i
                break
        if m != 0 and m != inorder_array_length - 1:
            l = m - 1
            r = m + 1

        while l >= 0 and r <= inorder_array_length - 1:
            if inorder_array[l] != inorder_array[r]:
                return False
            l -= 1
            r += 1
        return True
