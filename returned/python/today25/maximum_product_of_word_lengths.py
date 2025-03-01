# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordSets = {i: set(word) for i, word in enumerate(words)}
        largest = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.allUnique(wordSets[i], wordSets[j]):
                    largest = max(largest, len(words[i]) * len(words[j]))
        return largest

    def allUnique(self, a: set, b: set) -> bool:
        for a_char in a:
            if a_char in b:
                return False
        return True