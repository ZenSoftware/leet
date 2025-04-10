# https://leetcode.com/problems/sliding-window-maximum/description/
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            cur_max = nums[i]
            for j in range(1, k):
                cur_max = max(cur_max, nums[i + j])
            result.append(cur_max)
        return result
