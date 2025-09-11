# https://leetcode.com/problems/max-consecutive-ones/description/
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        largest = 0
        for n in nums:
            if n == 1:
                count += 1
                largest = max(largest, count)
            else:
                count = 0
        return largest
