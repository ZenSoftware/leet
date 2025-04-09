# https://leetcode.com/problems/sliding-window-median/description/
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i = 0
        result = []
        mid_index = k // 2
        if k % 2 == 1:
            while i + k <= len(nums):
                median = self.quick_select_odd(nums[i : i + k], mid_index)
                result.append(median)
                i += 1
        else:
            while i + k <= len(nums):
                mid_left, mid_right = self.quick_select_even(nums[i : i + k], mid_index)
                median = (mid_left + mid_right) / 2
                result.append(median)
                i += 1
        return result

    def quick_select_even(
        self, nums: List[int], mid_right_index: int
    ) -> tuple[int, int]:
        def helper(left: int, right: int, target: int):
            if left == right:
                return nums[left]

            i = left - 1
            for j in range(left, right):
                if nums[j] < nums[right]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            i += 1
            nums[i], nums[right] = nums[right], nums[i]

            if i < target:
                return helper(i + 1, right, target)
            elif target < i:
                return helper(left, i - 1, target)
            else:
                return nums[i]

        mid_right = helper(0, len(nums) - 1, mid_right_index)
        mid_left = helper(0, mid_right_index - 1, mid_right_index - 1)
        return (mid_right, mid_left)

    def quick_select_odd(self, nums: List[int], target_index: int) -> int:
        def helper(left: int, right: int):
            if left == right:
                return nums[left]

            i = left - 1
            for j in range(left, right):
                if nums[j] < nums[right]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            i += 1
            nums[i], nums[right] = nums[right], nums[i]

            if i < target_index:
                return helper(i + 1, right)
            elif target_index < i:
                return helper(left, i - 1)
            else:
                return nums[i]

        return helper(0, len(nums) - 1)
