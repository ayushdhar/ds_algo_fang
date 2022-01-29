from typing import List


def get_partition_key(nums: List[int], l: int, r: int):
    pivot = l

    while l < r:
        while l < len(nums) and nums[l] <= nums[pivot]:
            l += 1
        while nums[r] > nums[pivot]:
            r -= 1
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
    nums[pivot], nums[r] = nums[r], nums[pivot]
    return r


def __quick_sort_rec_helper(nums: List[int], start: int, end: int):
    if start < end:
        partition_index = get_partition_key(nums=nums, l=start, r=end)
        __quick_sort_rec_helper(nums=nums, start=start, end=partition_index - 1)
        __quick_sort_rec_helper(nums=nums, start=partition_index + 1, end=end)
    else:
        return


def quick_sort(nums: List[int]):
    __quick_sort_rec_helper(nums=nums, start=0, end=len(nums) - 1)


nums = [8, 5, 7, 3, 2]
quick_sort(nums=nums)
print(nums)
