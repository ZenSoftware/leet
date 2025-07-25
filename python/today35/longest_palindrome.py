# https://leetcode.com/problems/longest-palindrome/
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        total = 0
        for _, count in Counter(s).items():
            if count % 2 == 1:
                if total % 2 == 1:
                    total += count - 1
                else:
                    total += count
            else:
                total += count
        return total