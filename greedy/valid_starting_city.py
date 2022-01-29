import heapq


def check_if_can_complete(distances, fuel, start):
    i = start
    tank = fuel[start]
    count = len(distances)

    while tank > 0 and count > 0:
        tank = tank - distances[i]
        if i == len(distances) - 1:
            i = 0
        else:
            i += 1
        tank += fuel[i]
        count -= 1

    return i == start


def validStartingCity(distances, fuel, mpg):
    fuel = [i * mpg for i in fuel]
    helper = []
    heapq.heapify(helper)

    for i in range(len(distances)):
        heapq.heappush(helper, -fuel[i] / distances[i])

    while helper:
        elem = -heapq.heappop(helper)

        for i in range(len(distances)):
            if fuel[i] / distances[i] == elem:
                if check_if_can_complete(distances, fuel, i):
                    return i

    return -1


print(validStartingCity([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10))
