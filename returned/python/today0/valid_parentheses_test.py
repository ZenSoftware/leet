from valid_parentheses import Solution

def test1():
    assert Solution().isValid("()") == True

def test2():
    assert Solution().isValid("()[]{}") == True

def test3():
    assert Solution().isValid("(]") == False

def test4():
    assert Solution().isValid("([])") == True
    
def test5():
    assert Solution().isValid("]") == False
