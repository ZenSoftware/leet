from longest_substring_without_repeating_characters_attempt2 import Solution


def test1():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3


def test2():
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1


def test3():
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
