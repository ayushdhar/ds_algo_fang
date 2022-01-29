class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def bst_search(root: TreeNode, val: int):
    node = root
    if node:
        if node.data == val:
            return True
        elif val < node.data:
            return bst_search(node.left, val)
        else:
            return bst_search(node.right, val)
    else:
        return False


def bst_search_itr(root: TreeNode, val: int):
    node = root
    while node:
        if val == node.data:
            return True
        elif val < node.data:
            node = node.left
        else:
            node = node.right
    return False


node = TreeNode(30)
node.left = TreeNode(20)
node.right = TreeNode(40)
node.left.left = TreeNode(10)
node.left.right = TreeNode(25)
node.right.left = TreeNode(35)
node.right.right = TreeNode(50)

print(bst_search_itr(node, 30))
