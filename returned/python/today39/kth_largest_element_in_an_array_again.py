# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
from random import randint


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        goal = len(nums) - k

        def quick_select(start: int, end: int) -> int:
            i = start - 1
            new_pivot_index = randint(start, end)
            nums[new_pivot_index], nums[end] = nums[end], nums[new_pivot_index]
            for j in range(start, end):
                if nums[j] < nums[end]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[end] = nums[end], nums[i]

            if i > goal:
                return quick_select(start, i - 1)
            elif i < goal:
                return quick_select(i + 1, end)
            else:
                return nums[i]

        return quick_select(0, len(nums) - 1)
