from longest_palindromic_substring import Solution

def test1():
    result = Solution().longestPalindrome('babad')
    assert result == 'bab'

def test2():
    result = Solution().longestPalindrome('cbbd')
    assert result == 'bb'