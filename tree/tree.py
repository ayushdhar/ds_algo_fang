class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def preorder(root: TreeNode):
    node = root

    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


def inorder(root: TreeNode):
    node = root

    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)


def postorder(root: TreeNode):
    node = root

    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


def preorder_it(root: TreeNode):
    node = root

    while True:
        print(node.data)
        if node.left:
            node = node.left
        else:
            node = node.right


root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(9)
root.right.left = TreeNode(7)
root.right.right = TreeNode(2)

preorder(root)
print("\n")
postorder(root)
print("\n")
inorder(root)
