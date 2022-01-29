def find_min_coins(v, coins_available):
    coins_available.sort()
    i = len(coins_available) - 1
    res = []
    while i >= 0:
        if coins_available[i] > v:
            i -= 1
            continue
        v -= coins_available[i]
        res.append(coins_available[i])
        if v < 0:
            del coins_available[-1]
            v += coins_available[i]
            break
        if v == 0:
            break
    if v > 0:
        return None
    return res


def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    res = find_min_coins(v=n, coins_available=denoms)
    if res:
        return len(res)
    return -1


v = 7
coins = [2, 4]
print(find_min_coins(v, coins))
