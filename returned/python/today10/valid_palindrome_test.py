from valid_palindrome import Solution

def test1():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True

def test2():
    assert Solution().isPalindrome("race a car") == False

def test3():
    assert Solution().isPalindrome(" ") == True

def test4():
    assert Solution().isPalindrome("0P") == False