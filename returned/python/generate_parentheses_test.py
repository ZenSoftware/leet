from generate_parentheses import Solution

def test1():
    assert Solution.generateParenthesis(None, 3) == ["((()))","(()())","(())()","()(())","()()()"]

def test2():
    assert Solution.generateParenthesis(None, 1) == ["()"]