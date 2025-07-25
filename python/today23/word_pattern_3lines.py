# https://leetcode.com/problems/word-pattern/solutions/2977027/python-3-2-lines-w-explanation-t-s-95-99/
from itertools import zip_longest

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        return (
            len(set(s)) ==
            len(set(pattern)) ==
            len(set(zip_longest(s, pattern)))
        )