# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
from bisect import bisect_left
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = []
        sorted_nums = []
        for n in reversed(nums):
            index = bisect_left(sorted_nums, n)
            counts.append(index)
            sorted_nums.insert(index, n)
        return counts[::-1]

    def binarySearch(self, sorted: List[int], insertion: int) -> int:
        l, r = 0, len(sorted)-1
        while l <= r:
            m = (l + r) // 2
            if insertion > sorted[m]:
                l = m + 1
            else:
                r = m - 1
        return l