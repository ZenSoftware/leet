# https://leetcode.com/problems/next-greater-element-i/description/
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n in nums1:
            i = nums2.index(n) + 1
            nextGreater = -1
            while i < len(nums2):
                if nums2[i] > n:
                    nextGreater = nums2[i]
                    break
                i += 1
            result.append(nextGreater)
        return result
