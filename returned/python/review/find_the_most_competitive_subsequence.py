# https://leetcode.com/problems/find-the-most-competitive-subsequence/description/
from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        m = len(nums) - k
        for n in nums:
            while stack and stack[-1] > n and m > 0:
                m -= 1
                stack.pop()
            stack.append(n)
        
        return stack[:k]