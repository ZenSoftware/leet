# https://leetcode.com/problems/number-of-segments-in-a-string/description/


class Solution:
    def countSegments(self, s: str) -> int:
        s_split = s.split(" ")
        count = 0
        for word in s_split:
            if word:
                count += 1
        return count
