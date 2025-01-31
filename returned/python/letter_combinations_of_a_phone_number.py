# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digit_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(i, combs):
            if len(combs) == len(digits):
                result.append(combs)
                return
            
            for c in digit_letters[digits[i]]:
                backtrack(i+1, combs + c)

        if digits:
            backtrack(0,'')
            
        return result