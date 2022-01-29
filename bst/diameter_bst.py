class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(root: BinaryTree):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


def path(root: BinaryTree):
    if not root:
        return 0
    return height(root.left) + height(root.right) + 1


def helper(node: BinaryTree, max_path: int):
    if node:
        max_path = max(max_path, path(node), helper(node.left, max_path), helper(node.right, max_path))
        return max_path
    else:
        return max_path


def binaryTreeDiameter(tree):
    return helper(tree, float('-inf'))
