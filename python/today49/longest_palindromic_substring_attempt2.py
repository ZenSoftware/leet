# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    """
    Time: O(n^2)
    Space: O(1)
    """

    def longestPalindrome(self, s: str) -> str:
        res = [0, 0]

        def expand(start, end):
            nonlocal res
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    if end - start > res[1] - res[0]:
                        res = [start, end]
                else:
                    break
                start -= 1
                end += 1

        for center in range(len(s)):
            expand(center, center)
            expand(center, center + 1)

        start, end = res
        return s[start : end + 1]
