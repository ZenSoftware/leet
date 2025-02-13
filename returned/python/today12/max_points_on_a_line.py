# https://leetcode.com/problems/max-points-on-a-line/description/
from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        largest = 1
        for i1 in range(len(points)-1):
            count = defaultdict(lambda: 1)
            p1 = points[i1]
            for i2 in range(i1+1, len(points)):
                p2 = points[i2]
                
                if p1[0] == p2[0]:
                    slope = float('inf')
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

                count[slope] += 1
                largest = max(largest, count[slope])

        return largest
