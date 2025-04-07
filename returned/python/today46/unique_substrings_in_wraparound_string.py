# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/
from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        d = defaultdict(int)
        i = 0
        while i < len(s):
            d[s[i]] = max(d[s[i]], 1)
            j = i + 1
            while j < len(s) and (
                ord(s[j]) - ord(s[j - 1]) == 1 or ord(s[j]) - ord(s[j - 1]) == -25
            ):
                d[s[j]] = max(d[s[j]], j - i + 1)
                j += 1
            i = j
        return sum(d.values())
