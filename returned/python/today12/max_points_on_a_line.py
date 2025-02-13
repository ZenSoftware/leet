# https://leetcode.com/problems/max-points-on-a-line/description/
from typing import List
from math import isclose

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        largest = 1
        for i1 in range(len(points)-1):
            p1 = points[i1]
            for i2 in range(i1, len(points)):
                p2 = points[i2]
                
                if p1[0] == p2[0]:
                    # x coordinates equal
                    count = 0
                    for p in points:
                        if p[0] == p1[0]:
                            count += 1
                    largest = max(largest, count)
                else:
                    # x coordinates do not equal
                    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
                    b = p1[1] - m * p1[0]
                    count = 0
                    for p in points:
                        if isclose(p[1], m * p[0] + b):
                            count += 1
                    largest = max(largest, count)
        return largest
