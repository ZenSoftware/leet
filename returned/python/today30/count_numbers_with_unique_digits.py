# https://leetcode.com/problems/count-numbers-with-unique-digits/description/

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        count = 0
        for i in range(10**n):
            as_string = str(i)
            if len(set(as_string)) == len(as_string):
                count += 1
        return count
    