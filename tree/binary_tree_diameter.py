class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(root: BinaryTree):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


def binaryTreeDiameter(tree):
    # Write your code here.
    return -1


def binaryTreeDiameterRec(tree: BinaryTree, max_dia: int = -1):
    node = tree

    if node:
        return max(max_dia, binaryTreeDiameterRec(node.left, max_dia) +
                   binaryTreeDiameterRec(node.right, max_dia))
    else:
        return max_dia


root = BinaryTree(8)
root.left = BinaryTree(3)
root.right = BinaryTree(5)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(9)
root.right.left = BinaryTree(7)
root.right.right = BinaryTree(2)

print(height_rec(tree=root))
