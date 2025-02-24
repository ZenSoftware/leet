# https://leetcode.com/problems/missing-number/
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rollcall = [False] * (len(nums)+1)
        
        for n in nums:
            rollcall[n] = True

        for i in range(len(nums)+1):
            if rollcall[i] == False:
                return i