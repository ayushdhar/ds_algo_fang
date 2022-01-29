from typing import List


def shift_right(nums: List[int], start_index: int, end_index: int):
    for i in range(end_index, start_index, -1):
        nums[i] = nums[i - 1]


def insertion_sort(nums: List[int]):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j+1] = temp


nums = [8, 5, 7, 3, 2]

insertion_sort(nums)

print(nums)
