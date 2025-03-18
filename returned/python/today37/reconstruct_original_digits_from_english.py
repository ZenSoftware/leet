# https://leetcode.com/problems/reconstruct-original-digits-from-english/
from collections import Counter

class Solution:
    NUMBERS = {
        '0': Counter('zero'),
        '1': Counter('one'),
        '2': Counter('two'),
        '3': Counter('three'),
        '4': Counter('four'),
        '5': Counter('five'),
        '6': Counter('six'),
        '7': Counter('seven'),
        '8': Counter('eight'),
        '9': Counter('nine'),
    }

    def originalDigits(self, s: str) -> str:
        counts = Counter(s)
        result = ''
        used = 0
        while used < len(s):
            for num, letters in self.NUMBERS.items():
                for c in letters:
                    if counts.get(c, 0) < letters[c]:
                        break
                else:
                    result += num
                    for c in letters:
                        counts[c] -= letters[c]
                        used += letters[c]
        return result