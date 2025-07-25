# https://leetcode.com/problems/concatenated-words/description/
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        visited: set[int] = set()
        words_set: set[str] = set(words)

        def dfs(word: str, start: int):
            n = len(word)
            if start == n:
                # Got past the end - the word is made of multiple words.
                return True
            if start in visited:
                # We already searched from this index.
                return False

            visited.add(start)
            # Go up until the last character in the word if we are starting
            # from the first index. Otherwise we'll mark single words as results.
            for i in range(start + 1, (n + 1 if start != 0 else n)):
                if word[start:i] in words_set and dfs(word, i):
                    return True

            return False

        result: list[str] = []
        for word in words:
            visited.clear()
            if dfs(word, 0):
                result.append(word)

        return result
