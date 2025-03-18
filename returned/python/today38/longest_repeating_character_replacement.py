# https://leetcode.com/problems/longest-repeating-character-replacement/description/
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Time: O(26*n)
        Space: O(1)
        '''
        counts = defaultdict(int)
        counts[s[0]] = 1
        l, r = 0, 0
        result = 0
        
        while True:
            max_freq = 0
            for freq in counts.values():
                max_freq = max(max_freq, freq)
            
            size = r-l+1
            if size - max_freq <= k:
                result = max(result, size)
                r += 1
                if r >= len(s):
                    break
                counts[s[r]] += 1
            else:
                counts[s[l]] -= 1
                l += 1

        return result