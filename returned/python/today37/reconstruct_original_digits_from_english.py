# https://leetcode.com/problems/reconstruct-original-digits-from-english/
from collections import Counter

class Solution:
    NUMBERS = {'0': Counter({'z': 1, 'e': 1, 'r': 1, 'o': 1}), '1': Counter({'o': 1, 'n': 1, 'e': 1}), '2': Counter({'t': 1, 'w': 1, 'o': 1}), '3': Counter({'e': 2, 't': 1, 'h': 1, 'r': 1}), '4': Counter({'f': 1, 'o': 1, 'u': 1, 'r': 1}), '5': Counter({'f': 1, 'i': 1, 'v': 1, 'e': 1}), '6': Counter({'s': 1, 'i': 1, 'x': 1}), '7': Counter({'e': 2, 's': 1, 'v': 1, 'n': 1}), '8': Counter({'e': 1, 'i': 1, 'g': 1, 'h': 1, 't': 1}), '9': Counter({'n': 2, 'i': 1, 'e': 1})}
    
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