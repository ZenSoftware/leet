from bulls_and_cows import Solution

def test1():
    assert Solution().getHint('1807', '7810') == '1A3B'

def test2():
    assert Solution().getHint('1123', '0111') == '1A1B'

def test3():
    assert Solution().getHint('1122', '2211') == '0A4B'