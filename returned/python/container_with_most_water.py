# https://leetcode.com/problems/container-with-most-water/description/
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maximum = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > maximum:
                maximum = area
            if height[l] <= height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
        return maximum
