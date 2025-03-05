# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    VOWELS = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s)-1
        while l < r:
            if s[l] in self.VOWELS and s[r] in self.VOWELS:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] not in self.VOWELS:
                l += 1
            elif s[r] not in self.VOWELS:
                r -= 1
        return ''.join(s)