# https://leetcode.com/problems/maximal-rectangle/description/
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        histograms = [[0] * len(matrix[0])]
        for row in matrix:
            next_row = [0] * len(matrix[0])
            for j, val in enumerate(row):
                if val == '1':
                    next_row[j] = histograms[-1][j] + 1
            histograms.append(next_row)
        
        largest = 0
        i = 1
        while i < len(histograms):
            largest = max(largest, self.largestRectangleArea(histograms[i]))
            i += 1

        return largest
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
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
