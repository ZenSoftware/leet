# https://leetcode.com/problems/move-zeroes/description/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        end = len(nums) - 1
        while end > 0 and nums[end] == 0:
            end -= 1
        
        while end >= 0:
            if nums[end] == 0:
                p = end
                while p+1 < len(nums) and nums[p+1] != 0:
                    nums[p], nums[p+1] = nums[p+1], nums[p]
                    p += 1
            end -= 1
