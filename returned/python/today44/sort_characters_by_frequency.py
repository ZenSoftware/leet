# https://leetcode.com/problems/sort-characters-by-frequency/description/
from collections import Counter


class Solution:
    """
    Time: O(nlogn)
    Space: O(n)
    """

    def frequencySort(self, s: str) -> str:
        s_sorted = sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
        res = []
        for char, count in s_sorted:
            res.append(char * count)
        return "".join(res)
