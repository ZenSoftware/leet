from shortest_palindrome_rabin_karp import Solution

def test1():
    assert Solution().shortestPalindrome('aacecaaa') == 'aaacecaaa'

def test2():
    assert Solution().shortestPalindrome('abcd') == 'dcbabcd'

def test3():
    # assert Solution().shortestPalindrome('aba') == 'aba'
    assert Solution().shortestPalindrome('aac') == 'caac'

def test4():
    assert Solution().shortestPalindrome('a') == 'a'