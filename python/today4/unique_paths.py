# https://leetcode.com/problems/unique-paths/description/
from typing import Dict

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo: Dict[str,int] = {}
        
        def dfs(x: int, y: int) -> int:
            if x == m-1 and y == n-1:
                return 1
            if x > m-1 or y > n-1:
                return 0
            
            key = str(x) + '-' + str(y)
            if key in memo:
                return memo[key]

            count = dfs(x, y+1)
            count += dfs(x+1, y)

            memo[key] = count
            return count
        return dfs(0,0)