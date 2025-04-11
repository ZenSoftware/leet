# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    """
    Time: O(n^2)
    Space: O(n)
    """

    def longestPalindrome(self, s: str) -> str:
        def get_pal(center: int):
            start, end = center, center
            pal = ""
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    pal = s[start : end + 1]
                else:
                    break
                start -= 1
                end += 1

            start, end = center, center + 1
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    if end - start + 1 > len(pal):
                        pal = s[start : end + 1]
                else:
                    break
                start -= 1
                end += 1

            return pal

        longest = ""
        for start in range(len(s)):
            pal = get_pal(start)
            if len(pal) > len(longest):
                longest = pal
        return longest
