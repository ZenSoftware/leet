# https://leetcode.com/problems/the-skyline-problem/description/
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        size = buildings[len(buildings)-1][1]
        skyline = [0] * (size + 2)
        
        for left, right, height in buildings:
            for i in range(left,right+1):
                if height > skyline[i]:
                    skyline[i] = height
        
        result = []

        if skyline[0] > 0:
            result.append([0, skyline[0]])

        for i in range(0, len(skyline)-1):
            if skyline[i] < skyline[i+1]:
                result.append([i+1, skyline[i+1]])
            if skyline[i] > skyline[i+1]:
                result.append([i, skyline[i+1]])
                            
        return result