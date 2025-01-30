from longest_palindromic_substring import Solution

def test1():
    result = Solution.longestPalindrome(None, 'babad')
    assert result == 'bab'

def test2():
    result = Solution.longestPalindrome(None, 'cbbd')
    assert result == 'bb'