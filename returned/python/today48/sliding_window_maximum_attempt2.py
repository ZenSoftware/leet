# https://leetcode.com/problems/sliding-window-maximum/description/
from typing import List
from collections import deque


class Solution:
    """
    Time: O(n)
    space: O(k)
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()
        l, r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if q[0] < l:
                q.popleft()

            if r >= k - 1:
                result.append(nums[q[0]])
                l += 1

            r += 1

        return result
