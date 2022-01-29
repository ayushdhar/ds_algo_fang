class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_leaf_nodes(root: BinaryTree, leaves: list):
    node = root
    if node and not node.left and not node.right:
        leaves.append(node.value)
    elif node:
        get_leaf_nodes(node.left, leaves)
        get_leaf_nodes(node.right, leaves)


def compareLeafTraversal(tree1, tree2):
    leaves1 = []
    get_leaf_nodes(tree1, leaves1)
    leaves2 = []
    get_leaf_nodes(tree2, leaves2)
    return sorted(leaves1) == sorted(leaves2)

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.left.right.left = BinaryTree(7)
root.left.right.right = BinaryTree(8)
root.right.right = BinaryTree(6)

leaves = []
get_leaf_nodes(root, leaves)
print(1000_000_000)