class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def inorder(root: TreeNode):
    node = root

    if node:
        inorder(node.left)
        print(node.data, end=",")
        inorder(node.right)


def height(root: TreeNode):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


def in_pre(node: TreeNode, parent_node: TreeNode):
    left_node = node.left
    while left_node.right:
        parent_node = left_node
        left_node = left_node.right
    return left_node, parent_node


def in_succ(node: TreeNode, parent_node: TreeNode):
    right_node = node.right
    while right_node.left:
        parent_node = right_node
        right_node = right_node.left
    return right_node, parent_node


def delete(node: TreeNode, val: int, parent_node: TreeNode = None):
    if val < node.data:
        parent_node = node
        delete(node=node.left, val=val, parent_node=parent_node)
    elif val > node.data:
        parent_node = node
        delete(node=node.right, val=val, parent_node=parent_node)
    else:
        if not node.left and not node.right:
            if parent_node.right == node:
                parent_node.right = None
            else:
                parent_node.left = None
        else:

            if height(node.left) > height(node.right):
                replacement, parent_node = in_pre(node, parent_node=parent_node)
                delete(node=replacement, parent_node=parent_node, val=replacement.data)
                node.data = replacement.data
            else:
                replacement, parent_node = in_succ(node, parent_node=parent_node)
                delete(node=replacement, parent_node=parent_node, val=replacement.data)
                node.data = replacement.data
    return node


node = TreeNode(10)
node.right = TreeNode(90)
node.right.left = TreeNode(20)
node.right.left.right = TreeNode(80)
node.right.left.right.left = TreeNode(30)
node.right.left.right.left.right = TreeNode(70)
inorder(node)
print("\n")
# delete(node=node, val=30, parent_node=None)
inorder(delete(node=node, val=10, parent_node=None))
