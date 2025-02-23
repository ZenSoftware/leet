# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ascii_a = ord('a')
        count_s = [0] * 26
        count_t = [0] * 26
        for c in s:
            count_s[ord(c)-ascii_a] += 1
        for c in t:
            count_t[ord(c)-ascii_a] += 1
        return count_s == count_t
