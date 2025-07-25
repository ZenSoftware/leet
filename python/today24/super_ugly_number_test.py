from super_ugly_number import Solution

def test1():
    assert Solution().nthSuperUglyNumber(12, [2,7,13,19]) == 32
    
def test2():
    assert Solution().nthSuperUglyNumber(1, [2,3,5]) == 1