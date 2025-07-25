# https://leetcode.com/problems/create-maximum-number/description/
from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        result = None
        largest = float('-inf')
        
        def backtrack(i: int, j: int, digits: List[int]):
            nonlocal result, largest

            if len(digits) == k:
                as_num = self.to_int(digits)
                if as_num > largest:
                    largest = as_num
                    result = digits.copy()
                return
            
            if i < len(nums1):
                digits.append(nums1[i])
                backtrack(i+1, j, digits)
                digits.pop()

            if j < len(nums2):
                digits.append(nums2[j])
                backtrack(i, j+1, digits)
                digits.pop()

            if i+1 < len(nums1):
                backtrack(i+1, j, digits)
            if j+1 < len(nums2):
                backtrack(i, j+1, digits)
            if i+1 < len(nums1) and j+1 < len(nums2):
                backtrack(i+1, j+1, digits)

        backtrack(0, 0, [])
        return result
    
    def to_int(self, digits: List[int]) -> int:
        result = 0
        for d in digits:
            result += d
            result *= 10
        return result