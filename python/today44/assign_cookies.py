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
        g_idx, s_idx, res = 0, 0, 0
        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] <= s[s_idx]:
                res += 1
                g_idx += 1
            s_idx += 1
        return res
