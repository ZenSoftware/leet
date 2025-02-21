# https://leetcode.com/problems/shortest-palindrome/description/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        s_reversed = s[::-1]
        longest = 0
        for i in range(1, len(s)+1):
            prefix = s[:i]
            suffix = s_reversed[len(s)-i:]
            if prefix == suffix:
                longest = i
        
        suffix = s[longest:]
        prefix = suffix[::-1]
        return prefix + s