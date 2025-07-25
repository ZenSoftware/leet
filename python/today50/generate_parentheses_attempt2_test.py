from generate_parentheses_attempt2 import Solution


def test1():
    assert Solution().generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]


def test2():
    assert Solution().generateParenthesis(1) == ["()"]
