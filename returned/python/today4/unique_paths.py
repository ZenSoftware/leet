# https://leetcode.com/problems/unique-paths/description/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        def dfs(x: int, y: int) -> None:
            if x == m - 1 and y == n -1:
                nonlocal count
                count += 1
                return
            if x > m - 1 or y > n - 1:
                return
            dfs(x, y+1)
            dfs(x+1, y)
        dfs(0,0)
        return count
