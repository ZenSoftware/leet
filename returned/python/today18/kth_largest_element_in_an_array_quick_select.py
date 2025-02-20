# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:        
        k = len(nums) - k

        def quickSelect(l: int, r: int) -> int:
            p, cur = l, l
            while cur < r:
                if nums[cur] < nums[r]:
                    nums[cur], nums[p] = nums[p], nums[cur]
                    p += 1
                cur += 1
            nums[r], nums[p] = nums[p], nums[r]
            
            if p < k:   return quickSelect(p+1, r)
            elif p > k: return quickSelect(l, p-1)
            else:       return nums[p]
        
        return quickSelect(0, len(nums)-1)
