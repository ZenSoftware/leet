# https://leetcode.com/problems/rotate-function/
from typing import List

class Solution:
    '''
    Time: O(n)
    Space: O(1)
    '''
    def maxRotateFunction(self, nums: List[int]) -> int:
        length = len(nums)
        total = sum(nums)
        prev = 0
        for i, n in enumerate(nums):
            prev += i*n

        ans = prev
        for k in range(1, len(nums)):
            prev = prev + total - length * nums[length-k]
            ans = max(ans, prev)
        return ans