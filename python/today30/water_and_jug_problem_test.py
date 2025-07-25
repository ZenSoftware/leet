from water_and_jug_problem import Solution

def test1():
    assert Solution().canMeasureWater(3,5,4) == True

def test2():
    assert Solution().canMeasureWater(2,6,5) == False

def test3():
    assert Solution().canMeasureWater(1,2,3) == True