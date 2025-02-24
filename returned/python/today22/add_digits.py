# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            next_num = 0
            while num > 0:
                next_num += num % 10
                num //= 10
            num = next_num
        return num