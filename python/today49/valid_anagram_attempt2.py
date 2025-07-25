# https://leetcode.com/problems/valid-anagram/
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = Counter(s)
        t_counts = Counter(t)

        if len(s_counts) != len(t_counts):
            return False

        for s_char, s_count in s_counts.items():
            if t_counts.get(s_char, 0) != s_count:
                return False

        return True
