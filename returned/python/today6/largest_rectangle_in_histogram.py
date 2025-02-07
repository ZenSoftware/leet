# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = float('-inf')
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                largest = max(largest, (i - index) * height)
                start = index
            stack.append((start, h))
 
        while stack:
            index, height = stack.pop()
            largest = max(largest, (len(heights) - index) * height)

        return largest