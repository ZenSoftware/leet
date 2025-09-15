from construct_the_rectangle import Solution


def test1():
    assert Solution().constructRectangle(4) == [2, 2]


def test2():
    assert Solution().constructRectangle(37) == [37, 1]


def test3():
    assert Solution().constructRectangle(122122) == [427, 286]
