# https://leetcode.com/problems/find-the-difference/
from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counts = Counter(s)
        t_counts = Counter(t)
        for c in t_counts:
            if c not in s_counts or s_counts[c] != t_counts[c]:
                return c