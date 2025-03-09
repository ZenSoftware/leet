# https://leetcode.com/problems/water-and-jug-problem/description/

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        
        if y < x:
            x, y = y, x
        
        for i in range(x, 0, -1):
            if x % i == 0 and y % i == 0:
                gdc = i
                break
        
        return target % gdc == 0