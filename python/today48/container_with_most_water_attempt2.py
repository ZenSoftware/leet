# https://leetcode.com/problems/container-with-most-water/description/
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            result = max(result, w * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
