from longest_common_subsequence import Solution


def test1():
    text1 = "abcde"
    text2 = "ace"
    assert Solution().longestCommonSubsequence(text1, text2) == 3
