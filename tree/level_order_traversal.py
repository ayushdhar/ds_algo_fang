from collections import deque


class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def level_order(root: TreeNode):
    q = deque()
    node = root
    q.append(node)

    level = 1


    while q:
        elem: TreeNode = q.popleft()

        print(elem.data, end="->")

        if elem.left:
            q.append(elem.left)
        if elem.right:
            q.append(elem.right)


root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(9)
root.right.left = TreeNode(7)
root.right.right = TreeNode(2)

level_order(root=root)
