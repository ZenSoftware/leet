from assign_cookies import Solution


def test1():
    assert Solution().findContentChildren([1, 2, 3], [1, 1]) == 1


def test2():
    assert Solution().findContentChildren([1, 2], [1, 2, 3]) == 2
