# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def minMoves(self, nums: List[int]) -> int:
        nums_min = min(nums)
        res = 0
        for n in nums:
            res += n - nums_min
        return res
