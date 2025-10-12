# https://leetcode.com/problems/base-7/description/


class Solution:
    def convertToBase7(self, num: int) -> str:
        n = abs(num)
        result = []

        while n >= 7:
            result.append(str(n % 7))
            n = n // 7

        result.append(str(n))

        if num < 0:
            result.append("-")

        result.reverse()
        return "".join(result)
