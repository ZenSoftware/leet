# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for char_s in s:
            while j < len(t) and t[j] != char_s:
                j += 1
            if j >= len(t) or t[j] != char_s:
                return False
            j += 1
        return True