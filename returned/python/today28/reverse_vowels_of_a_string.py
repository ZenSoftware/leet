# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s)-1
        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while l < r:
            if s[l] in VOWELS and s[r] in VOWELS:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] not in VOWELS:
                l += 1
            elif s[r] not in VOWELS:
                r -= 1
        return ''.join(s)