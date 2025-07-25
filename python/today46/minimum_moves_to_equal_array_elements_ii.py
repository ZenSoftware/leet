# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
from typing import List


class Solution:
    """
    Time: O(nlogn)
    Space: O(1)
    """

    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[(len(nums) - 1) // 2]
        res = 0
        for n in nums:
            res += abs(median - n)
        return res
