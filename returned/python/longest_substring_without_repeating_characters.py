class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maximum = 1
        l = 0
        r = 1
        cache = set(s[0])
        while r <= len(s) - 1:
            while (s[r] in cache) & (l < r):
                cache.remove(s[l])
                l += 1
            cache.add(s[r])
            maximum = max(maximum, r - l + 1)
            r += 1
        return maximum