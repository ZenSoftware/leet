# https://leetcode.com/problems/increasing-triplet-subsequence/description/
# explenation: https://www.youtube.com/watch?v=41gyzVIx-ds

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = float('inf')
        j = float('inf')
        for n in nums:
            if n <= i:
                i = n
            elif n <= j:
                j = n
            else:
                return True
        return False
