# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l, r = 0, 0
        seen = set()
        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            else:
                seen.add(s[r])
            result = max(result, r - l + 1)
            r += 1
        return result
