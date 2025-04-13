# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
from typing import List


class Solution:
    """
    nums=[0,1,2,3,4,5,6]    k=4
                ^--k--^
              goal   end
    goal = end - k + 1
         = (len(n) - 1) - k + 1
         = len(n) - k
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quick_select(start: int, end: int) -> int:
            i = start - 1
            for j in range(start, end):
                if nums[j] < nums[end]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[end] = nums[end], nums[i]

            dup_start = i
            for j in range(dup_start + 1, end + 1):
                if nums[j] == nums[dup_start]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            dup_end = i

            if dup_start <= target <= dup_end:
                return nums[target]

            if i < target:
                return quick_select(i + 1, end)
            else:
                return quick_select(start, i - 1)

        return quick_select(0, len(nums) - 1)
