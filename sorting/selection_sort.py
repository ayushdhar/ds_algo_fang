from typing import List


def selection_sort(nums: List[int]):
    length = len(nums)

    for i in range(length):
        j = i
        curr_min_idx = i

        while j < length:
            if nums[j] < nums[curr_min_idx]:
                curr_min_idx = j
            j += 1
        if i != curr_min_idx:
            nums[curr_min_idx], nums[i] = nums[i], nums[curr_min_idx]


nums = [-1, 6, 3, 2, 5, 4]

selection_sort(nums=nums)

print(nums)
