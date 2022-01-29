def tasks_with_original_idx(tasks: list) -> dict:
    helper = {}

    for i in range(len(tasks)):
        if tasks[i] in helper:
            helper[tasks[i]].append(i)
        else:
            helper[tasks[i]] = [i]
    return helper


def taskAssignment(k, tasks: list):
    res = []
    tasks_idx = tasks_with_original_idx(tasks)
    tasks = sorted(tasks)

    i = k - 1
    j = k

    while i >= 0:
        res.append([tasks_idx[tasks[i]].pop(), tasks_idx[tasks[j]].pop()])
        i -= 1
        j += 1

    return res


k = 3
tasks = [1, 3, 5, 3, 1, 4]

print(taskAssignment(k, tasks))
