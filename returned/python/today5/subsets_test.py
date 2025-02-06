from subsets import Solution

def test1():
    result = Solution().subsets([1,2,3])
    assert result == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]