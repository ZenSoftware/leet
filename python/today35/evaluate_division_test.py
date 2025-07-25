from evaluate_division import Solution

def test1():
    result = Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    assert result == [6.00000,0.50000,-1.00000,1.00000,-1.00000]