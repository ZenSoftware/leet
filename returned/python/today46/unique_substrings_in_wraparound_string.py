# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        seen = set()
        count = 0
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if substr not in seen and self.is_substring(substr):
                    count += 1
                    seen.add(substr)
        return count

    def is_substring(self, s: str) -> bool:
        prev = ord(s[0])
        for i in range(1, len(s)):
            cur = ord(s[i])
            if cur % 26 != (prev + 1) % 26:
                return False
            prev = cur
        return True
