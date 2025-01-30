class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maximum = 1
        i = 0
        while i <= len(s) - 1 - maximum:
            cache = {s[i]: None}
            j = i+1
            while j <= len(s) - 1:
                if s[j] in cache:
                    break
                maximum = max(maximum, j-i+1)
                cache[s[j]] = None
                j += 1
            i += 1
        return maximum