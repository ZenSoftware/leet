# https://leetcode.com/problems/3sum-closest/description/
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i, a in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if abs(threeSum - target) < abs(closest - target):
                    closest = threeSum
                if threeSum < target:
                    l += 1
                elif threeSum > target:
                    r -= 1
                else:
                    l += 1
        return closest