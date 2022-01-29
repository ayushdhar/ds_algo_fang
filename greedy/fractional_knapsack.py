from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        max_units = 0

        for entry in boxTypes:
            num_of_boxes = min(entry[0], truckSize)
            max_units += entry[1] * num_of_boxes
            truckSize -= num_of_boxes
            if truckSize == 0:
                return max_units
        return max_units


s = Solution()

print(s.maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10))
