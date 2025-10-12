# https://leetcode.com/problems/base-7/description/


class Solution:
    def convertToBase7(self, num: int) -> str:
        n = abs(num)
        result = ""

        while n >= 7:
            result = str(n % 7) + result
            n = n // 7

        result = str(n) + result

        if num < 0:
            result = "-" + result

        return result
