# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        letter_to_word = dict()
        word_to_letter = dict()
        
        for i in range(len(words)):
            if pattern[i] not in letter_to_word:
                letter_to_word[pattern[i]] = words[i]
            elif letter_to_word[pattern[i]] != words[i]:
                return False

            if words[i] not in word_to_letter:
                word_to_letter[words[i]] = pattern[i]
            elif word_to_letter[words[i]] != pattern[i]:
                return False

        return True