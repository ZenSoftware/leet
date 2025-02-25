# https://leetcode.com/problems/perfect-squares/description/
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        memo = set()
        level = 0
        queue = deque([0])
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                children = []
                i = 1
                while i**2 <= n-current:
                    children.append(i**2 + current)
                    i += 1
                
                for child in children:
                    if child not in memo:
                        memo.add(child)
                        queue.append(child)
                    
                    if child == n:
                        return level + 1
            level += 1
