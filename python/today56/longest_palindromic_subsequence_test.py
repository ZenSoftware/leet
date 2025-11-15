from longest_palindromic_subsequence import Solution


def test1():
    assert Solution().longestPalindromeSubseq("bbbab") == 4


def test2():
    assert Solution().longestPalindromeSubseq("cbbd") == 2
