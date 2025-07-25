# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] > nums[mid]:
                # in right part of rotation
                if target < nums[mid]:
                    right = mid - 1
                else:
                    if target > nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                # in left part of rotation
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[left] > target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1
