from maximum_product_subarray_attempt2 import Solution


def test1():
    assert Solution().maxProduct([2, 3, -2, 4]) == 6


def test2():
    assert Solution().maxProduct([-2, 0, -1]) == 0
