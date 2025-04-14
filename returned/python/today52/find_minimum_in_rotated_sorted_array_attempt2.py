# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                # in right of rotation
                right = mid
            else:
                # in left of rotation
                if nums[left] < nums[right]:
                    return nums[left]
                else:
                    left = mid + 1

        return nums[left]
