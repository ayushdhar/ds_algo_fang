def minimumWaitingTime(queries: list):
    queries.sort()
    wait_time = 0

    for i in range(len(queries)):
        prev_exe_time = queries[i]
        queries[i] = wait_time
        wait_time += prev_exe_time

    return sum(queries)


print(minimumWaitingTime([3, 2, 1, 2, 6]))
