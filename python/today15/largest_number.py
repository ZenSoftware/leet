# https://leetcode.com/problems/largest-number/
from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return -1 if x+y > y+x else 1
        
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        
        if nums[0] == '0':
            return '0'

        return "".join(nums)
