from can_i_win import Solution


def test1():
    assert Solution().canIWin(10, 11) == False


def test2():
    assert Solution().canIWin(10, 0) == True


def test3():
    assert Solution().canIWin(10, 1) == True
