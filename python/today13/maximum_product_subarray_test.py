from maximum_product_subarray import Solution

def test1():
    assert Solution().maxProduct([2,3,-2,4]) == 6

def test2():
    assert Solution().maxProduct([-2,0,-1]) == 0

def test3():
    assert Solution().maxProduct([0,0,0,-1]) == 0