from shortest_palindrome import Solution

def test1():
    assert Solution().shortestPalindrome('aacecaaa') == 'aaacecaaa'

def test2():
    assert Solution().shortestPalindrome('abcd') == 'dcbabcd'