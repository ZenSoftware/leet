# https://leetcode.com/problems/next-greater-element-ii/
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            j = i + 1
            while j != i:
                if j == len(nums):
                    j = 0
                    continue
                if nums[j] > nums[i]:
                    result.append(nums[j])
                    break
                j += 1
            if j == i:
                result.append(-1)
        return result
