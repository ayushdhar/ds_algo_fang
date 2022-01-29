from typing import List


def radix_sort(nums: List[int]):
    max_number = max(nums)
    count = 0

    while max_number > 0:
        max_number = int(max_number / 10)
        count += 1
    i = 0
    while i < count:
        helper = [[] for _ in range(10)]

        for j in nums:
            radix_idx = int((j / (10 ** i))) % 10
            helper[radix_idx].append(j)

        m = 0
        for k in helper:
            if k:
                for l in k:
                    nums[m] = l
                    m += 1
        i += 1


nums = [237, 196, 259, 348, 152, 163, 235, 48, 36]
radix_sort(nums=nums)

print(nums)
