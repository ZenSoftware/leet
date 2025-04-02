# https://leetcode.com/problems/4sum-ii/description/
from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        n = len(nums1)
        count = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                            count += 1
        return count
