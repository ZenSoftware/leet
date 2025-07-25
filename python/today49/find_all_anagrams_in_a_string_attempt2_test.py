from find_all_anagrams_in_a_string_attempt2 import Solution


def test1():
    assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]


def test2():
    assert Solution().findAnagrams("abab", "ab") == [0, 1, 2]
