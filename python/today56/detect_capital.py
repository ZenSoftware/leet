# https://leetcode.com/problems/detect-capital/description/


class Solution(object):
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or self.isPascal(word)

    def isPascal(self, word):
        if not word:
            return False

        return word[0].isupper() & word[1:].islower()
