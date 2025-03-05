# https://leetcode.com/problems/counting-bits/description/
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        result = [0,1]
        i = 0
        while 2**(i+2) <= n:
            duplicate = result[2**i : 2**(i+1)]
            result.extend(duplicate)
            result.extend(map(lambda x: x+1, duplicate))
            i += 1
            
        duplicateLength = 2**(i+1) - 2**i
        remaining = n - 2**(i+1)
        if remaining <= duplicateLength:
            duplicate = result[2**i : 2**i + remaining+1]
            result.extend(duplicate)
        else:
            duplicate = result[2**i : 2**(i+1)]
            result.extend(duplicate)
            result.extend(map(lambda x: x+1, duplicate[:remaining-duplicateLength+1]))
            
        return result