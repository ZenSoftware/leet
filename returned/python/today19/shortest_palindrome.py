# https://leetcode.com/problems/shortest-palindrome/description/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s_reversed = s[::-1]
        longest = 0
        for i in range(len(s)):
            prefix = s[:len(s)-i]
            suffix = s_reversed[i:]
            if prefix == suffix:
                longest = len(s)-i
                break
        
        suffix = s[longest:]
        prefix = suffix[::-1]
        return prefix + s