from longest_substring_without_repeating_characters import Solution

def test1():
    result = Solution.lengthOfLongestSubstring(None, 'abcabcbb')
    assert result == 3

def test2():
    result = Solution.lengthOfLongestSubstring(None, 'bbbbb')
    assert result == 1

def test3():
    result = Solution.lengthOfLongestSubstring(None, 'pwwkew')
    assert result == 3

def test4():
    result = Solution.lengthOfLongestSubstring(None, 'au')
    assert result == 2