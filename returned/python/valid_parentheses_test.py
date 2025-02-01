from valid_parentheses import Solution

def test1():
    assert Solution.isValid(None, "()") == True

def test2():
    assert Solution.isValid(None, "()[]{}") == True

def test3():
    assert Solution.isValid(None, "(]") == False

def test4():
    assert Solution.isValid(None, "([])") == True
    
def test5():
    assert Solution.isValid(None, "]") == False
