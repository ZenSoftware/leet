# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
from typing import List


class Solution:
    """
    Time: O(nlogn)
    Space: O(1)
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res = 0
        prev = [None, float("-inf")]
        for cur in points:
            if prev[1] < cur[0]:
                res += 1
                prev = cur
        return res
