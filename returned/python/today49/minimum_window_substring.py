# https://leetcode.com/problems/minimum-window-substring/description/
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        counts = defaultdict(int)
        for char in t:
            counts[char] += 1

        remaining = len(t)
        result_length = float("inf")
        result_start = 0
        start = 0
        end = 0

        while end < len(s):
            if counts[s[end]] > 0:
                remaining -= 1
            counts[s[end]] -= 1

            end += 1

            while remaining == 0:
                if end - start < result_length:
                    result_length = end - start
                    result_start = start

                if counts[s[start]] >= 0:
                    remaining += 1
                counts[s[start]] += 1
                start += 1

        return (
            ""
            if result_length == float("inf")
            else s[result_start : result_start + result_length]
        )
