# https://leetcode.com/problems/permutations-ii/description/
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        count = { n:0 for n in nums }
        for n in nums:
            count[n] += 1
        
        def dfs():
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()
        dfs()
        return result