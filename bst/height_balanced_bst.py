class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(root: BinaryTree):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


def helper(root: BinaryTree):
    if root:
        return abs(height(root.left) - height(root.right)) <= 1 and helper(root.left) and helper(root.right)
    else:
        return True


def heightBalancedBinaryTree(tree):
    # Write your code here.
    return helper(tree)
