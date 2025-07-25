# https://leetcode.com/problems/palindrome-pairs/
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.isPalindrome(words[i] + words[j]):
                    result.append([i,j])
                if self.isPalindrome(words[j] + words[i]):
                    result.append([j,i])
        return result

    def isPalindrome(self, word: str):
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True