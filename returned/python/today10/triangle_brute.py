from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        smallest = float('inf')
        def dfs(i, j, sum):
            if i == len(triangle) - 1:
                nonlocal smallest
                smallest = min(smallest, sum)
                return
            dfs(i+1, j, sum+triangle[i+1][j])
            dfs(i+1, j+1, sum+triangle[i+1][j+1])
        dfs(0,0,triangle[0][0])
        return smallest