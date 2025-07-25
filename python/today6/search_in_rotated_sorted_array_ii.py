# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True
            
            # left is sorted
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right is sorted
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1            
            else:
                l += 1
        return False