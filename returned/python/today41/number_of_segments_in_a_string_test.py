from number_of_segments_in_a_string import Solution


def test1():
    assert Solution().countSegments("Hello, my name is John") == 5


def test2():
    assert Solution().countSegments("Hello") == 1
