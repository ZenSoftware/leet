# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        i = 0
        nums_len = len(nums)
        while i < nums_len - 2:
            j = i+1
            while j < nums_len - 1:
                k = j+1
                while k < nums_len:
                    if nums[i] + nums[j] + nums[k] == 0:
                        array_results =[nums[i], nums[j], nums[k]]
                        array_results.sort()
                        # result.append((nums[i], nums[j], nums[k]))
                        result.add(tuple(array_results))
                    k += 1
                j += 1
            i += 1
        result = [list(x) for x in result]
        return result