# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordSets = {}
        largest = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if i not in wordSets:
                    wordSets[i] = set(words[i])
                if j not in wordSets:
                    wordSets[j] = set(words[j])
                if self.allUnique(wordSets[i], wordSets[j]):
                    product = len(words[i]) * len(words[j])
                    largest = max(largest, product)
        return largest

    def allUnique(self, a: set, b: set) -> bool:
        for a_char in a:
            if a_char in b:
                return False
        return True