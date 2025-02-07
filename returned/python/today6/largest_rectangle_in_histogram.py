# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = float('-inf')
        stack = []

        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][1]:
                stack.append((i, h))
            else:
                while stack and stack[-1][1] > h:
                    j, height = stack.pop()
                    area = (i - j) * height
                    if area > largest:
                        largest = area
                stack.append((j, h))
 
        while stack:
            j, height = stack.pop()
            area = (len(heights) - j) * height
            if area > largest:
                largest = area

        return largest