from find_the_difference import Solution

def test1():
    assert Solution().findTheDifference('abcd', 'abcde') == 'e'

def test2():
    assert Solution().findTheDifference('', 'y') == 'y'