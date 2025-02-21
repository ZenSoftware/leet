# https://leetcode.com/problems/shortest-palindrome/description/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        for i in range(len(s)):
            suffix = s[len(s)-i:]
            prefix = suffix[::-1]
            pal = prefix + s
            if self.is_palindrome(pal):
                return pal

    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True