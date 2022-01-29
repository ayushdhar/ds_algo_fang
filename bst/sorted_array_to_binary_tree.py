from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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


s = Solution()

print(s.sortedArrayToBST([-10, -3, 0, 5, 9]).left.right.val)
