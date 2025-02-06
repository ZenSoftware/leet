# https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for p in path.split('/'):
            if not p or p == '.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        return '/' + '/'.join(stack)