# https://leetcode.com/problems/4sum-ii/description/
from typing import List
from collections import defaultdict


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        memo = defaultdict(int)
        for i in nums1:
            for j in nums2:
                memo[i + j] += 1

        res = 0
        for i in nums3:
            for j in nums4:
                res += memo[-i - j]

        return res
