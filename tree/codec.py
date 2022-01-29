from typing import Optional, List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder(root: TreeNode, s: str):
    node = root

    if node:
        inorder(node.left, s)
        s += f",{node.val}"
        inorder(node.right, s)


class Codec:
    def __init__(self):
        self.coded_data = ""

    def helper(self, nums, start, end) -> Optional[TreeNode]:
        if start <= end:
            mid = (start + end) // 2
            new_node = TreeNode(nums[mid])
            new_node.left = self.helper(nums, start, mid - 1)
            new_node.right = self.helper(nums, mid + 1, end)
            return new_node
        else:
            return None

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if length == 0:
            return None
        return self.helper(nums, 0, length - 1)

    def serialize(self, root: TreeNode):
        inorder(root, self.coded_data)
        return self.coded_data

    def deserialize(self, data: str):
        return self.sortedArrayToBST([int(i) for i in data.split(",")])
