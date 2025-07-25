from fizz_buzz import Solution

def test1():
    assert Solution().fizzBuzz(3) == ["1","2","Fizz"]

def test2():
    assert Solution().fizzBuzz(5) == ["1","2","Fizz","4","Buzz"]

def test3():
    assert Solution().fizzBuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]