from matchsticks_to_square import Solution


def test1():
    assert Solution().makesquare([1, 1, 2, 2, 2]) == True


def test2():
    assert Solution().makesquare([3, 3, 3, 3, 4]) == False


def test3():
    assert Solution().makesquare([2, 2, 2, 6]) == False
