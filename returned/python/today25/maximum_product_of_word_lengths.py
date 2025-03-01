# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        char_sets = [set(words[i]) for i in range(len(words))]
        largest = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not char_sets[i] & char_sets[j]:
                    largest = max(largest, len(words[i]) * len(words[j]))
        return largest