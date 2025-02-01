# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        progress = []
        for b in s:
            if b == '{' or b == '(' or b == '[':
                progress.append(b)
            elif len(progress) == 0:
                return False
            elif b == '}' and progress.pop() != '{':
                return False
            elif b == ')' and progress.pop() != '(':
                return False
            elif b == ']' and progress.pop() != '[':
                return False
        return len(progress) == 0
