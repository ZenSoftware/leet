from add_binary import Solution

def test1():
    assert Solution().addBinary("11", "1") == "100"

def test2():
    assert Solution().addBinary("1010", "1011") == "10101"