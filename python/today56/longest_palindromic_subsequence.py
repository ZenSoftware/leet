# https://leetcode.com/problems/longest-palindromic-subsequence/


class Solution(object):
    def longestPalindromeSubseq(self, s):
        return self.longestCommonSubsequence(s, s[::-1])

    def longestCommonSubsequence(self, text1, text2):
        rows = len(text1) + 1
        cols = len(text2) + 1
        grid = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                if text1[r] == text2[c]:
                    grid[r][c] = grid[r + 1][c + 1] + 1
                else:
                    grid[r][c] = max(grid[r + 1][c], grid[r][c + 1])

        return grid[0][0]
