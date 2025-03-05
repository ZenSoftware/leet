from reverse_string import Solution

def test1():
    input = ["h","e","l","l","o"]
    Solution().reverseString(input)
    assert input == ["o","l","l","e","h"]

def test2():
    input = ["H","a","n","n","a","h"]
    Solution().reverseString(input)
    assert input == ["h","a","n","n","a","H"]