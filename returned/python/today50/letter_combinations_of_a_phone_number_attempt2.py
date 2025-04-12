# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from typing import List


class Solution:
    PHONE_LETTERS = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []

        def dfs(i: int, path: List[str]):
            if i == len(digits):
                result.append("".join(path))
                return

            for char in self.PHONE_LETTERS[digits[i]]:
                path.append(char)
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return result
