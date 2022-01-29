def is_overlapping(t1: list, t2: list):
    return t2[0] < t1[1]


def find_platform(arrival: list, departure: list):
    data = sorted([list(i) for i in zip(arrival, departure)], key=lambda x: x[0])
    platforms = {}
    count = 1

    for d in data:
        added = False
        for k, v in platforms.items():
            if not is_overlapping(v, d):
                platforms[k] = d
                added = True
                break
        if not added:
            platforms[count] = d
            count += 1
    return len(platforms.keys())


arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

print(find_platform(arrival, departure))


def find_platform(arrival: list, departure: list):
    arrival.sort()
    departure.sort()
    platforms = result = 1
    i = 1
    j = 0
    n = len(arrival)
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platforms += 1
            i += 1
        elif arrival[i] > departure[j]:
            platforms -= 1
            j += 1
        result = max(result, platforms)
    return result


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print("Minimum Number of Platforms Required = ",
      findPlatform(arr, dep, n))
