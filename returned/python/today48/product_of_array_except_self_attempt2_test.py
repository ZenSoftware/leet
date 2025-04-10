from product_of_array_except_self_attempt2 import Solution


def test1():
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test2():
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
