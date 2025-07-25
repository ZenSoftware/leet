# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total_len = len(A) + len(B)
        half = total_len // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            A_left = A[m1] if m1 >= 0 else float('-infinity')
            A_right = A[m1+1] if m1+1 < len(A) else float('infinity')
            B_left = B[m2] if m2 >= 0  else float('-infinity')
            B_right = B[m2+1] if m2+1 < len(B) else float('infinity')

            if A_left <= B_right and B_left <= A_right:
                if total_len % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    return min(A_right, B_right)
            elif A_left > B_right:
                r = m1 - 1
            else:
                l = m1 + 1