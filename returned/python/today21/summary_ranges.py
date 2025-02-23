# https://leetcode.com/problems/summary-ranges/
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        lower = nums[0]
        upper = nums[0]
        result = []

        for i in range(1,len(nums)):
            if nums[i-1] + 1 != nums[i]:
                if lower == upper:
                    result.append(str(lower))
                else:
                    result.append(str(lower) + '->' + str(upper))
                lower = nums[i]
                upper = nums[i]
            upper = nums[i]
        
        if lower == upper:
            result.append(str(lower))
        else:
            result.append(str(lower) + '->' + str(upper))

        return result