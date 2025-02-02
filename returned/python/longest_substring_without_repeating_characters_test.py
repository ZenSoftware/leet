from longest_substring_without_repeating_characters import Solution

def test1():
    result = Solution().lengthOfLongestSubstring('abcabcbb')
    assert result == 3

def test2():
    result = Solution().lengthOfLongestSubstring('bbbbb')
    assert result == 1

def test3():
    result = Solution().lengthOfLongestSubstring('pwwkew')
    assert result == 3

def test4():
    result = Solution().lengthOfLongestSubstring('au')
    assert result == 2