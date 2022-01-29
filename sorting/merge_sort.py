def merge_arrays(nums: list, start: int, mid: int, end: int):
    res = []
    i, j = start, mid + 1

    while i <= mid and j <= end:
        if nums[i] < nums[j]:
            res.append(nums[i])
            i += 1
        else:
            res.append(nums[j])
            j += 1

    for l in range(j, end + 1):
        res.append(nums[l])

    for p in range(i, mid + 1):
        res.append(nums[p])
    for i in res:
        nums[start] = i
        start += 1


def merge_sort_rec(nums: list, l, r):
    if l < r:
        mid = (l + r) // 2

        merge_sort_rec(nums, l, mid)
        merge_sort_rec(nums, mid + 1, r)
        merge_arrays(nums, start=l, end=r, mid=mid)


nums = [8, 3, 7, 4, 9, 2, 6, 5, -1]

merge_sort_rec(nums, 0, len(nums) - 1)

print(nums)
