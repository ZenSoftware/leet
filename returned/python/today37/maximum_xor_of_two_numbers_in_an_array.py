# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
from typing import List

class Solution:
    '''
    Time: O(n^2)
    Space: O(1)
    '''
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ans = float('-inf')
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                ans = max(ans, nums[i] ^ nums[j])
        return ans