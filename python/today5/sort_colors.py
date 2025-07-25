from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        
        while l < r:
            while nums[l] == 0 and l < r:
                l += 1

            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            else:
                r -= 1

        r = len(nums) - 1
        
        while l < r:
            while nums[r] == 2 and l < r:
                r -= 1

            if nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            else:
                l += 1