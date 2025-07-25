from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        sub1 = self.rob_sub(nums[1:])
        sub2 = self.rob_sub(nums[:len(nums)-1])
        return max(sub1, sub2)
    
    def rob_sub(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2