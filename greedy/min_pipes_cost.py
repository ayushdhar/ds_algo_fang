import heapq


def min_cost(pipes: list):
    weight = 0
    heapq.heapify(pipes)

    for i in range(len(pipes) - 1):
        first = heapq.heappop(pipes)
        second = heapq.heappop(pipes)
        weight += first + second
        heapq.heappush(pipes, first + second)
    return weight
