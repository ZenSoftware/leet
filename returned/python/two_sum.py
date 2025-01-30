# https://leetcode.com/problems/two-sum/description/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in cache:
                return [cache[dif], i]
            cache[nums[i]] = i

sol = Solution.twoSum(None, [2,7,11,15], 9)
print(sol)