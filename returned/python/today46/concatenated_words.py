# https://leetcode.com/problems/concatenated-words/description/
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)

        def isConcatenatedWord(word: str) -> bool:
            i = 0
            while i < len(word):
                j = i + 1
                while j <= len(word):
                    substr = word[i:j]
                    if substr in words:
                        words.remove(substr)
                        if isConcatenatedWord(word[i:]):
                            words.add(substr)
                            return True
                        words.add(substr)
                        break
                    j += 1
                else:
                    return False
                i = j
            return True

        result = []
        for word in words.copy():
            words.remove(word)
            if isConcatenatedWord(word):
                result.append(word)
            words.add(word)
        return result
