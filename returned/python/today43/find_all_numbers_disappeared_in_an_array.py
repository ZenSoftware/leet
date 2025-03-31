# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in seen:
                res.append(i)
        return res
