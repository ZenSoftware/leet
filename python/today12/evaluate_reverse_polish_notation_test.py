from evaluate_reverse_polish_notation import Solution

def test1():
    assert Solution().evalRPN(["2","1","+","3","*"]) == 9
    
def test2():
    assert Solution().evalRPN(["4","13","5","/","+"]) == 6

def test3():
    assert Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
