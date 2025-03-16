# https://leetcode.com/problems/queue-reconstruction-by-height/description/
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = None
        
        def backtrack(remaining: List[List[int]], current: List[List[int]]) -> List[List[int]]:
            nonlocal result
            if len(current) == len(people):
                result = current.copy()
                return True
            
            for i, r in enumerate(remaining):
                if self.countAhead(current, r) == r[1]:
                    current.append(r)
                    if backtrack(remaining[:i] + remaining[i+1:], current):
                        return True
                    current.pop()
            
            return False
            
        backtrack(people, [])
        return result
    
    def countAhead(self, current: List[List[int]], person: List[int]) -> int:
        count = 0
        for c in current:
            if person[0] <= c[0]:
                count += 1
        return count