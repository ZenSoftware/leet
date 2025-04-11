# https://leetcode.com/problems/ransom-note/description/
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts = Counter(magazine)
        for char, count in Counter(ransomNote).items():
            if magazine_counts.get(char, 0) - count < 0:
                return False
        return True
