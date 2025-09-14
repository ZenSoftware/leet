# https://leetcode.com/problems/non-decreasing-subsequences/description/
from typing import List


class Solution:
    def solution(self, nums: List[int], index: int, output: List[int], ans: set):
        if index >= len(nums):
            if len(output) >= 2:
                ans.add(tuple(output))
            return

        if not output or nums[index] >= output[-1]:
            output.append(nums[index])
            self.solution(nums, index + 1, output, ans)
            output.pop()

        self.solution(nums, index + 1, output, ans)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        self.solution(nums, 0, [], ans)
        result = [list(x) for x in ans]
        return result
