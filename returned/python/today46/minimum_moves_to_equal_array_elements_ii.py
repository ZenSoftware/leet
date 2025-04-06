# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
from typing import List


class Solution:
    """
    Time: O(n^2)
    Space: O(1)
    """

    def minMoves2(self, nums: List[int]) -> int:
        res = float("inf")
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                count += abs(nums[i] - nums[j])
            res = min(res, count)
        return res
