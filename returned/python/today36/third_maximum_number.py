# https://leetcode.com/problems/third-maximum-number/description/
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = list(set(nums))
        if len(distinct) < 3:
            return max(distinct)
        
        distinct.sort(reverse=True)
        return distinct[2]