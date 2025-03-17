# https://leetcode.com/problems/partition-equal-subset-sum/description/
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(i: int, nums1: List[int], nums2: List[int]) -> bool:
            if i >= len(nums):
                return sum(nums1) == sum(nums2)
            result = False
            
            nums1.append(nums[i])
            result |= dfs(i+1, nums1, nums2)
            nums1.pop()
            if result:
                return True

            nums2.append(nums[i])
            result |= dfs(i+1, nums1, nums2)
            nums2.pop()

            return result
        return dfs(0, [], [])