from different_ways_to_add_parentheses import Solution

def test1():
    result = Solution().diffWaysToCompute('2-1-1')
    result.sort()
    assert result == [0,2]

def test2():
    result = Solution().diffWaysToCompute('2*3-4*5')
    result.sort()
    assert result == [-34,-14,-10,-10,10]