# https://leetcode.com/problems/generate-parentheses/description/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(open: int, close: int, path: List[str]):
            if open == n and close == n:
                result.append("".join(path))
                return

            if open < n:
                path.append("(")
                dfs(open + 1, close, path)
                path.pop()

            if close < n and close < open:
                path.append(")")
                dfs(open, close + 1, path)
                path.pop()

        dfs(0, 0, [])
        return result
