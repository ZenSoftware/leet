# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        i = 0
        while i < len(nums) - 2:
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    entry = [nums[i], nums[j], nums[k]]
                    entry.sort()
                    result.add(tuple(entry))
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        return [list(x) for x in result]
        