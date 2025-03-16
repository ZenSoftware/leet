# https://leetcode.com/problems/longest-palindrome/
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        for _, count in Counter(s).items():
            if count % 2 == 1:
                if length % 2 == 1:
                    length += count - 1
                else:
                    length += count
            else:
                length += count
        return length