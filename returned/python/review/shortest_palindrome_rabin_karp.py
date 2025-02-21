# https://leetcode.com/problems/shortest-palindrome/
# NeetCode solution: https://www.youtube.com/watch?v=niOT-FK1RH8

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        suffix = 0
        base = 26
        last_index = 0
        power = 1

        for i, c in enumerate(s):
            char = ord(c) - ord('a') + 1

            prefix = prefix * base
            prefix = prefix + char

            suffix = suffix + char * power
            power = power * base
            if prefix == suffix:
                last_index = i
        
        suffix = s[last_index + 1:]
        return suffix[::-1] + s