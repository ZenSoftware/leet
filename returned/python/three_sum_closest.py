# https://leetcode.com/problems/3sum-closest/description/
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i, a in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                current_sum = a + nums[l] + nums[r]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    return current_sum
        return closest_sum