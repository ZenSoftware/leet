# https://leetcode.com/problems/fizz-buzz/description/
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            divisible_3 = i % 3 == 0
            divisible_5 = i % 5 == 0
            if divisible_3 and divisible_5:
                res.append('FizzBuzz')
            elif divisible_3:
                res.append('Fizz')
            elif divisible_5:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res