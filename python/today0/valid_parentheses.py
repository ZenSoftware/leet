# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {'}':'{', ')':'(', ']':'['}
        for c in s:
            if c in mappings.values():
                stack.append(c)
            elif not stack:
                return False
            elif stack.pop() != mappings[c]:
                return False
        return not stack
