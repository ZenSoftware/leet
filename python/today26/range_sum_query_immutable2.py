# https://leetcode.com/problems/range-sum-query-immutable/description/
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        accum = 0
        for n in nums:
            accum += n
            self.prefix.append(accum)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]