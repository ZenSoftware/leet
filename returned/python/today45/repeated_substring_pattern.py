# https://leetcode.com/problems/repeated-substring-pattern/description/


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2):
            chunk = s[: i + 1]
            for j in range(i + 1, len(s), i + 1):
                if chunk != s[j : j + i + 1]:
                    break
            else:
                return True
        return False
