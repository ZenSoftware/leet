# https://leetcode.com/problems/generate-parentheses/description/
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: List[str], open: int, closed: int):
            if len(current) == n*2:
                result.append(''.join(current))
                return
            
            if open < n:
                current.append('(')
                backtrack(current, open+1, closed)
                current.pop()

            if closed < open:
                current.append(')')
                backtrack(current, open, closed+1)
                current.pop()
        
        backtrack([], 0, 0)

        return result