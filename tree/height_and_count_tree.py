class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def height(root: TreeNode):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


def path(root: TreeNode):
    if not root:
        return 0
    return height(root.left) + height(root.right) + 1


def count(node: TreeNode):
    if node:
        return 1 + count(node.left) + count(node.right)
    else:
        return 0


def count_leaf_nodes(node: TreeNode):
    if node:
        if not node.left and not node.right:
            return 1
        else:
            return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)
    else:
        return 0


root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(12)
root.left.left.right = TreeNode(14)
root.left.left.right.left = TreeNode(4)
root.left.left.right.left.left = TreeNode(9)
root.left.left.right.left.right = TreeNode(7)
root.right = TreeNode(5)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(2)

print(count_leaf_nodes(node=root))
