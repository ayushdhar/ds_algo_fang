from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]

        helper = []

        for i in tokens:
            if i in operators:
                second, first = helper.pop(), helper.pop()
                if i == "+":
                    helper.append(first + second)
                elif i == "-":
                    helper.append(first - second)
                elif i == "*":
                    helper.append(first * second)
                else:
                    helper.append(int(first / second))
            else:
                helper.append(int(i))

        return helper[0]


s = Solution()

assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
