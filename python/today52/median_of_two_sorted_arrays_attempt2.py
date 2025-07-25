# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
from typing import List


class Solution:
    """
    Time: O(log n+m)
    Space: O(1)
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1) - 1
        while True:
            i = (left + right) // 2
            x_left = nums1[i] if i >= 0 else float("-inf")
            x_right = nums1[i + 1] if i + 1 < len(nums1) else float("inf")

            j = half - i - 2
            y_left = nums2[j] if j >= 0 else float("-inf")
            y_right = nums2[j + 1] if j + 1 < len(nums2) else float("inf")

            if x_left <= y_right and y_left <= x_right:
                if total % 2 == 1:
                    return min(x_right, y_right)
                else:
                    return (max(x_left, y_left) + min(x_right, y_right)) / 2
            elif x_left > y_right:
                right = i - 1
            else:
                left = i + 1
