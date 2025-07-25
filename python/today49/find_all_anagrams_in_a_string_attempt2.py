# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
from collections import defaultdict, Counter
from typing import List


class Solution:
    """
    Time: O(n) where n is the length of s
    Space: O(P) where P is length of p
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        window_counts = defaultdict(int)
        p_counts = Counter(p)

        def is_anagram() -> bool:
            for char, count in p_counts.items():
                if window_counts[char] != count:
                    return False
            return True

        for i in range(len(p) - 1):
            window_counts[s[i]] += 1

        result = []
        for i in range(len(s) - len(p) + 1):
            window_counts[s[i + len(p) - 1]] += 1
            if is_anagram():
                result.append(i)
            window_counts[s[i]] -= 1
        return result
