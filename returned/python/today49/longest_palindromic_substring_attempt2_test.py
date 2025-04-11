from longest_palindromic_substring_attempt2 import Solution


def test1():
    assert Solution().longestPalindrome("babad") == "bab"


def test2():
    assert Solution().longestPalindrome("cbbd") == "bb"
