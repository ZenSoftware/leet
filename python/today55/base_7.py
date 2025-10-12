# https://leetcode.com/problems/base-7/description/


class Solution:
    def convertToBase7(self, num: int) -> str:
        remainder = abs(num)
        result = ""

        while remainder >= 7:
            result = str(remainder % 7) + result
            remainder = remainder // 7

        result = str(remainder) + result

        if num < 0:
            result = "-" + result

        return result
