from minimum_window_substring import Solution


def test1():
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"


def test2():
    assert Solution().minWindow("a", "a") == "a"


def test3():
    assert Solution().minWindow("a", "aa") == ""


def test4():
    assert Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd") == "abbbbbcdd"
