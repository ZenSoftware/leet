# https://leetcode.com/problems/ransom-note/description/
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCounts = Counter(ransomNote)
        magazineCounts = Counter(magazine)
        for r, c in ransomNoteCounts.items():
            if r not in magazineCounts or magazineCounts[r] < c:
                return False
        return True