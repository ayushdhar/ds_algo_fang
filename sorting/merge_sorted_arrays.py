def merge(nums1: list, nums2: list):
    m = len(nums1)
    n = len(nums2)
    nums3 = []
    i, j, k = 0, 0, 0

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
            k += 1
        else:
            nums3.append(nums2[j])
            j += 1
            k += 1

    if j < n:
        for l in range(j, n):
            nums3.append(nums2[j])
    elif i < m:
        for p in range(i, m):
            nums3.append(nums1[i])

    return nums3


def merge_same_array(nums: list, start: int, mid: int, end: int):
    res = []
    i, j = start, mid + 1

    while i <= mid and j <= end:
        if nums[i] < nums[j]:
            res.append(nums[i])
            i += 1
        else:
            res.append(nums[j])
            j += 1

    for l in range(j, end+1):
        res.append(nums[l])

    for p in range(i, mid+1):
        res.append(nums[p])
    #
    # for i in range(len(res)):
    #     nums[i] = res[i]
    print(res)


nums = [2, 5, 8, 12, 3, 6, 7, 8]
merge_same_array(nums, 0, 3, 7)
