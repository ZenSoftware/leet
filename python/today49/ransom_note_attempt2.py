# https://leetcode.com/problems/ransom-note/description/
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts = Counter(magazine)
        for char, ransom_count in Counter(ransomNote).items():
            if magazine_counts.get(char, 0) - ransom_count < 0:
                return False
        return True
