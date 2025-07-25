# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        char_dict = {char: 1 for char in s}
        count = 1
        for i in range(1, len(s)):
            diff = ord(s[i]) - ord(s[i - 1])
            if diff == 1 or diff == -25:
                count += 1
            else:
                count = 1
            char_dict[s[i]] = max(char_dict[s[i]], count)
        return sum(char_dict.values())
