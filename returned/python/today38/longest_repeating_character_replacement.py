# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        counts = {}
        max_freq = 0
        res = 0
        l = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_freq = max(max_freq, counts[s[r]])
            if r-l+1 - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res