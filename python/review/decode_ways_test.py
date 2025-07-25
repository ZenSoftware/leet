from decode_ways import Solution

def test1():
    assert Solution().numDecodings("12") == 2

def test2():
    assert Solution().numDecodings("226") == 3

def test3():
    assert Solution().numDecodings("06") == 0

def test4():
    assert Solution().numDecodings("00") == 0

def test5():
    assert Solution().numDecodings("100") == 0