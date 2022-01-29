from typing import List


def helper(heap: List[int]):
    elem_idx = len(heap) - 1
    if elem_idx % 2 == 0:
        parent_idx = (elem_idx - 2) // 2
    else:
        parent_idx = (elem_idx - 1) // 2

    while heap[elem_idx] > heap[parent_idx] and parent_idx >= 0:
        heap[elem_idx], heap[parent_idx] = heap[parent_idx], heap[elem_idx]
        elem_idx = parent_idx
        if elem_idx % 2 == 0:
            parent_idx = (elem_idx - 2) // 2
        else:
            parent_idx = (elem_idx - 1) // 2


def insert(heap: List[int], elem: int) -> List[int]:
    heap.append(elem)
    helper(heap)
    return heap


heap = sorted([30, 20, 15, 5, 10, 12, 6])
new = []
for i in heap:
    insert(new, i)

print(new)
