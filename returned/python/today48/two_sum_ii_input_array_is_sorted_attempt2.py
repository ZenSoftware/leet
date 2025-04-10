# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            for j in range(len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
