from combination_sum_ii import Solution

def test1():
    result = Solution().combinationSum2([10,1,2,7,6,1,5], 8)
    assert result == [[1,1,6],[1,2,5],[1,7],[2,6]]

def test2():
    result = Solution().combinationSum2([2,5,2,1,2], 5)
    assert result == [[1,2,2],[5]]
