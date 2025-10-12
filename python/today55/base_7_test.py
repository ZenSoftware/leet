from base_7 import Solution


def test1():
    assert Solution().convertToBase7(100) == "202"


def test2():
    assert Solution().convertToBase7(-7) == "-10"
