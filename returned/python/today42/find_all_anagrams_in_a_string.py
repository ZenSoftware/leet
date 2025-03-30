# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_counts = defaultdict(int)
        s_counts = defaultdict(int)
        for i in range(len(p)):
            p_counts[p[i]] += 1
            s_counts[s[i]] += 1

        def is_anagram():
            for p_char, p_count in p_counts.items():
                if s_counts[p_char] != p_count:
                    return False
            return True

        res = []
        for i in range(len(s) - len(p) + 1):
            if is_anagram():
                res.append(i)

            s_counts[s[i]] -= 1
            if i + len(p) in range(len(s)):
                next_char = s[i + len(p)]
                s_counts[next_char] += 1
        return res
