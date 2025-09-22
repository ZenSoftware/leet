# https://leetcode.com/problems/keyboard-row/description/
from typing import List


class Solution:
    row1 = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
    row2 = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
    row3 = {"z", "x", "c", "v", "b", "n", "m"}

    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            if self.wordBelongsToSingleRow(word):
                result.append(word)
        return result

    def wordBelongsToSingleRow(self, word: str) -> bool:
        char_set = set(word.lower())
        return (
            char_set.issubset(self.row1)
            or char_set.issubset(self.row2)
            or char_set.issubset(self.row3)
        )
