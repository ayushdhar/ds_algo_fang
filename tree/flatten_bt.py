# This is the class of the input root. Do not edit it.
from typing import List


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def right_most(root: BinaryTree):
    node = root
    if node:
        node = right_most(node.right)
        return node


def left_most(root: BinaryTree):
    node = root
    if node:
        node = left_most(node.left)
        return node


def inorder(root: BinaryTree, res: List[BinaryTree]):
    node = root

    if node:
        node.left = right_most(node.left)
        node.right = left_most(node.right)
        return node
    else:
        return None


def flattenBinaryTree(root):
    inorder_list = []

    inorder(root, inorder_list)

    for i in range(len(inorder_list)):
        left = inorder_list[i - 1] if i > 0 else None
        right = inorder_list[i + 1] if i < len(inorder_list) - 1 else None
        inorder_list[i].left = left
        inorder_list[i].right = right
    return inorder_list[0]
