from rectangle_area import Solution

def test1():
    assert Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2) == 45
    assert Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2) == 16