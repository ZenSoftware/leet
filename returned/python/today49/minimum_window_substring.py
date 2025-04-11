# https://leetcode.com/problems/minimum-window-substring/description/
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_counts = Counter(t)

        def is_valid(s_counts: Counter):
            for char, count in t_counts.items():
                if s_counts[char] < count:
                    return False
            return True

        def get_min_window(start: int):
            s_counts = defaultdict(int)
            for end in range(len(t) - 1):
                s_counts[s[start + end]] += 1

            for end in range(start + len(t) - 1, len(s)):
                s_counts[s[end]] += 1
                if is_valid(s_counts):
                    return s[start : end + 1]

            return ""

        result = ""
        for start in range(len(s) - len(t) + 1):
            if s[start] not in t_counts:
                continue

            window = get_min_window(start)
            if window != "" and (result == "" or len(window) < len(result)):
                result = window
        return result
