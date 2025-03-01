# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = [0] * len(words)
        for i, word in enumerate(words):
            for c in word:
                masks[i] |= 1 << (ord(c) - ord('a'))

        largest = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not masks[i] & masks[j]:
                    largest = max(largest, len(words[i]) * len(words[j]))
        return largest
        