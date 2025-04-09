# https://leetcode.com/problems/sliding-window-median/description/
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i = 0
        result = []
        mid_index = k // 2
        if k % 2 == 1:
            while i + k <= len(nums):
                nums_sorted = nums[i : i + k]
                nums_sorted.sort()
                result.append(nums_sorted[mid_index])
                i += 1
        else:
            while i + k <= len(nums):
                nums_sorted = nums[i : i + k]
                nums_sorted.sort()
                median = (nums_sorted[mid_index - 1] + nums_sorted[mid_index]) / 2
                result.append(median)
                i += 1
        return result
