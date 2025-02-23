# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
from typing import List

class Solution:
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def backtrack(exp: List[str | int]) -> List[int]:
            result = []
            for i in range(len(exp)):
                if exp[i] in self.operators:
                    nums1 = backtrack(exp[:i])
                    nums2 = backtrack(exp[i+1:])
                    op = self.operators[exp[i]]
                    for n1 in nums1:
                        for n2 in nums2:
                            result.append(op(n1, n2))
            if result == []:
                return exp
            return result
        exp = self.parse(expression)
        return backtrack(exp)
        
    def parse(self, expression: str) -> List[str | int]:
        result = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                j = i
                while j < len(expression) and expression[j].isdigit():
                    j += 1
                num = int(expression[i:j])
                result.append(num)
                i = j
            elif expression[i] in self.operators:
                result.append(expression[i])
                i += 1
            else:
                i += 1
        return result