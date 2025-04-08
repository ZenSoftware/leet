# https://leetcode.com/problems/ones-and-zeroes/description/
from typing import List
from collections import Counter


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs.sort(key=len)
        res = 0
        for s in strs:
            counts = Counter(s)
            if counts["0"] <= m and counts["1"] <= n:
                res += 1
                m -= counts["0"]
                n -= counts["1"]
        return res
