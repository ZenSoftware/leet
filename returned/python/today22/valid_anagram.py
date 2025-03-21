# https://leetcode.com/problems/valid-anagram/description/
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = defaultdict(int)
        for c in s:
            count_s[c] += 1
        
        count_t = defaultdict(int)
        for c in t:
            count_t[c] += 1
        
        for c in count_s:
            if count_s[c] != count_t[c]:
                return False
            
        return True