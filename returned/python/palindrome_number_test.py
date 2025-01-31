from palindrome_number import Solution

def test1():
    assert Solution.isPalindrome(None, 121) == True

def test2():
    assert Solution.isPalindrome(None, -121) == False

def test3():
    assert Solution.isPalindrome(None, 10) == False