# https://leetcode.com/problems/repeated-substring-pattern/description/


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            chunk = s[:i]
            for j in range(i, len(s), i):
                if chunk != s[j : j + i]:
                    break
            else:
                return True
        return False
