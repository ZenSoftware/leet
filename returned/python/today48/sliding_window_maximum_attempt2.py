# https://leetcode.com/problems/sliding-window-maximum/description/
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur_max_index = 0
        for i in range(1, k):
            if nums[i] > nums[cur_max_index]:
                cur_max_index = i

        result = []
        for i in range(len(nums) - k + 1):
            if nums[i + k - 1] >= nums[cur_max_index]:
                cur_max_index = i + k - 1
            elif cur_max_index < i:
                cur_max_index = i
                for j in range(1, k):
                    if nums[i + j] > nums[cur_max_index]:
                        cur_max_index = i + j
            result.append(nums[cur_max_index])
        return result
