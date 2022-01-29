from typing import List
import time


def bubble_sort(nums: List[int]):
    length = len(nums)

    for i in range(length - 1):
        for j in range(length - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


nums = [8, 5, 7, 3, 2]

start_time = time.time()
bubble_sort(nums)
print("--- %s seconds ---" % (time.time() - start_time))

