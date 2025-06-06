# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(searching_left: bool):    
            left = 0
            right = len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    index = mid
                    if searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1    
            return index
        left = binary_search(True)
        right = binary_search(False)
        return [left, right]
