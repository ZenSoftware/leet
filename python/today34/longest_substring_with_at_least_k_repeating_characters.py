# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/

from typing import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        counts = Counter(s)
        for i, c in enumerate(s):
            if counts[c] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)    
        return len(s)