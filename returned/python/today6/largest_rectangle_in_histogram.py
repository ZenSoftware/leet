# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = float('-inf')
        stack = []
        i = 0
        
        while i < len(heights):
            if not stack or heights[i] >= stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                while stack and stack[-1][1] > heights[i]:
                    (index, height) = stack.pop()
                    area = (i - index) * height
                    if area > largest:
                        largest = area
                stack.append((index, heights[i]))
            i += 1

        while stack:
            (index, height) = stack.pop()
            area = (i - index) * height
            if area > largest:
                largest = area

        return largest