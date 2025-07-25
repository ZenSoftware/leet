from number_of_boomerangs import Solution


def test1():
    assert Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]) == 2


def test2():
    assert Solution().numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]) == 2


def test3():
    assert Solution().numberOfBoomerangs([[1, 1]]) == 0
