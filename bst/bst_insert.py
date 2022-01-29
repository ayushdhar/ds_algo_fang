class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def inorder(root: TreeNode):
    node = root

    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)


def bst_insert(root: TreeNode, val: int) -> None:
    prev = node = root

    while node:
        if val == node.data:
            return
        elif val < node.data:
            prev = node
            node = node.left
        else:
            prev = node
            node = node.right
    new_node = TreeNode(val)
    if new_node.data < prev.data:
        prev.left = new_node
    else:
        prev.right = new_node


def bst_insert_rec(root: TreeNode, val: int):
    bst_insert_rec_helper(root, val)


def bst_insert_rec_helper(root: TreeNode, val: int, prev: TreeNode = None):
    node = root
    if node:
        if node.data == val:
            return
        elif val < node.data:
            bst_insert_rec_helper(node.left, val, node)
        else:
            bst_insert_rec_helper(node.right, val, node)
    else:
        new_node = TreeNode(val)
        if prev:
            if new_node.data < prev.data:
                prev.left = new_node
            else:
                prev.right = new_node


node = TreeNode(30)
node.left = TreeNode(20)
node.right = TreeNode(40)
node.left.left = TreeNode(10)
node.left.right = TreeNode(25)
node.right.left = TreeNode(35)
node.right.right = TreeNode(50)

bst_insert_rec(node, 11)

inorder(node)
inorder(node)
