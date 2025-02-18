# https://leetcode.com/problems/subsets-ii/description/
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset[::])
                return
            
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return result
