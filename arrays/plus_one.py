from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1

        for i in range(len(digits) - 1, -1, -1):
            sum = digits[i] + c
            digits[i] = sum % 10
            c = sum // 10
        if c > 0:
            digits.insert(0, c)
        return digits


s = Solution()

print(s.plusOne([-1, 0, 0, 0]))
