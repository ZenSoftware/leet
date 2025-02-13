# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                a, b = stack.pop(), stack.pop() 
                stack.append(int(b/a))
            else:
                stack.append(int(t))
        return stack[0]