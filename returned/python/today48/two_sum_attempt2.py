# https://leetcode.com/problems/two-sum/description/
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in cache:
                return [cache[diff], i]
            else:
                cache[nums[i]] = i
