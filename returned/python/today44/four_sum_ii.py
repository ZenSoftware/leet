# https://leetcode.com/problems/4sum-ii/description/
from typing import List
from collections import defaultdict


class Solution:
    """
    Time: O(n^2)
    Space: O(n)
    """

    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        memo = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                memo[n1 + n2] += 1

        res = 0
        for n3 in nums3:
            for n4 in nums4:
                res += memo[-(n3 + n4)]

        return res
