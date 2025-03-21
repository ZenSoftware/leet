# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        goal = len(nums) - k

        def quick_select(start, end):
            # 1st patition such that all elements that are less than
            # the pivot are shuffled to the front
            i = start - 1
            pivot = nums[end]
            for j in range(start, end):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            dup_start = i + 1
            nums[dup_start], nums[end] = nums[end], nums[dup_start]

            # 2nd partition will contains all duplicates of pivot
            # 3rd partition will contain all elements greater than the pivot
            i = dup_start
            for j in range(dup_start + 1, end + 1):
                if nums[j] == pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            dup_end = i

            # Recurse on the 1st and 3rd partitions
            # Skip the 2nd partition due to it containing only duplicates
            if goal < dup_start:
                return quick_select(start, dup_start - 1)
            elif dup_end < goal:
                return quick_select(dup_end + 1, end)
            else:
                return nums[dup_start]

        return quick_select(0, len(nums) - 1)
