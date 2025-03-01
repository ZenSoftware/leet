# https://leetcode.com/problems/find-the-most-competitive-subsequence/description/
from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        digits = []
        left = 0
        while len(digits) < k:
            right = len(nums) - (k - len(digits))
            smallest = float('inf')
            smallest_index = None
            for i in range(left, right+1):
                if nums[i] < smallest:
                    smallest = min(smallest, nums[i])
                    smallest_index = i
            digits.append(smallest)
            left = smallest_index + 1
        return digits