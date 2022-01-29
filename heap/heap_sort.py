from typing import List

lchild = lambda i: 2 * i + 1
rchild = lambda i: 2 * i + 2


def delete(heap: List[int], size: int):
    heap[0], heap[size] = heap[size], heap[0]
    i = 0
    l = lchild(i)
    r = rchild(i)

    while l < size and r < size and (heap[i] < heap[l] or heap[i] < heap[r]):
        if heap[l] > heap[r]:
            heap[i], heap[l] = heap[l], heap[i]
            i = l
        else:
            heap[i], heap[r] = heap[r], heap[i]
            i = r
        l = lchild(i)
        r = rchild(i)


heap = [30, 20, 15, 5, 10, 12, 6]

for i in range(1, len(heap)):
    delete(heap, len(heap) - i)
print(heap)
