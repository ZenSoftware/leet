# https://leetcode.com/problems/next-greater-element-i/description/
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = {}

        for r in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[r]:
                stack.pop()
            if not stack:
                ans[nums2[r]] = -1
            else:
                ans[nums2[r]] = stack[-1]
            stack.append(nums2[r])

        result = []
        for n in nums1:
            result.append(ans[n])
        return result
