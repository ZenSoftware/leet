from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []
        def backtrack(i: int) -> None:
            if i >= len(s):
                result.append(part.copy())
                return
            
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return result
    
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1
        return True