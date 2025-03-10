# https://leetcode.com/problems/wiggle-subsequence/description/
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = None
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if up == True or up is None:
                    count += 1
                up = False
            elif nums[i-1] > nums[i]:
                if up == False or up is None:
                    count += 1
                up = True
        return count