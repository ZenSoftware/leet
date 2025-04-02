# https://leetcode.com/problems/assign-cookies/description/
from typing import List


class Solution:
    """
    Time: O(nlogn)
    Space: O(1)
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i = 0
        for greed in g:
            while i < len(s) and s[i] < greed:
                i += 1
            if i >= len(s):
                return res
            res += 1
            i += 1
        return res
