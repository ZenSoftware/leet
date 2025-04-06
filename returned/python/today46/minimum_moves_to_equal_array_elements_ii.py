# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
from typing import List


class Solution:
    """
    Time: O(n^2)
    Space: O(1)
    """

    def minMoves2(self, nums: List[int]) -> int:
        res = float("inf")
        for n1 in nums:
            count = 0
            for n2 in nums:
                count += abs(n1 - n2)
                if count >= res:
                    break
            res = min(res, count)
        return res
