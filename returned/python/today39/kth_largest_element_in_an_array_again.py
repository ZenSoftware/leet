# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
from random import randint


class Solution:
    """
     Time: O(n)
     Space: O(1)

     k: 4, len(nums): 7
     indicies: 0 1 2 3 4 5 6
                     ^--k--^
                   goal   end
     goal = end - k + 1
     goal = (len(nums) - 1) - k + 1
     goal = len(nums) - k

                  p
     [4 3 2 1 5 3 3]
    i j

     [2 1 | 4 3 5 3 3]     if num[j] < pivot: swap(++i, j)
        i           j

     Pivots final resting place of pivot will be at i+1.
     Store the index of the beginnging of 2nd partition.
     [2 1 | 3 3 5 3 4]
            ^
         dup_start

     Shuffle all duplicates of pivot into the 2nd partition.
     [2 1 | 3 3 5 3 4]
            i j

     [2 1 | 3 3 3 | 5 4]    if num[j] == pivot: swap(++i, j)
                i   j
                ^
             dup_end

     [2 1 | 3 3 3 | 5 4]
      1st    2nd    3rd

     Recurse on the partition containing the goal.
     Return if the goal is within the 2nd partition.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        goal = len(nums) - k

        def quick_select(start, end):
            # Process the 1st patition such that the front of
            # the array contains all elements less than the pivot.
            i = start - 1
            pivot_index = randint(start, end)
            nums[pivot_index], nums[end] = nums[end], nums[pivot_index]
            pivot = nums[end]
            for j in range(start, end):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            dup_start = i + 1
            nums[dup_start], nums[end] = nums[end], nums[dup_start]

            # Process 2nd partition such that it contains all the duplicates
            # of pivot.  Thus, the 3rd partition will contain all elements
            # strictly greater than the pivot.
            i = dup_start
            for j in range(dup_start + 1, end + 1):
                if nums[j] == pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            dup_end = i

            # Recurse on the 1st and 3rd partitions.
            # Skip the 2nd partition due to it containing only duplicates.
            if goal < dup_start:
                return quick_select(start, dup_start - 1)
            elif dup_end < goal:
                return quick_select(dup_end + 1, end)
            else:
                return nums[dup_start]

        return quick_select(0, len(nums) - 1)
