from typing import List


def classPhotos(redShirtHeights: List[int], blueShirtHeights: List[int]) -> bool:
    redShirtHeights.sort()
    blueShirtHeights.sort()
    rt, bt = redShirtHeights[0] > blueShirtHeights[0], blueShirtHeights[0] > redShirtHeights[0]
    i, j = 1, 1
    if rt == bt:
        return False
    while i < len(redShirtHeights):

        if rt and redShirtHeights[i] <= blueShirtHeights[j]:
            return False
        if bt and redShirtHeights[i] >= blueShirtHeights[j]:
            return False
        i += 1
        j += 1

    return True
