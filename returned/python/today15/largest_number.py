# https://leetcode.com/problems/largest-number/
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numStrs = list(map(str, nums))
        numStrs = self._mergeSort(numStrs)
        
        if numStrs[0] == '0':
            return '0'
        
        return "".join(numStrs)

    def _mergeSort(self, numStrs: List[str]) -> List[str]:
        def merge(left: List[str], right: List[str]) -> List[str]:
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] + right[j] > right[j] + left[i]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            return result

        if len(numStrs) <= 1:
            return numStrs
        
        mid = len(numStrs) // 2
        left = self._mergeSort(numStrs[:mid])
        right = self._mergeSort(numStrs[mid:])
        return merge(left, right)
