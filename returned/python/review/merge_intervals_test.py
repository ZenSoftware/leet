from merge_intervals import Solution

def test1():
    result = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
    assert result == [[1,6],[8,10],[15,18]]

def test2():
    result = Solution().merge([[1,4],[4,5]])
    assert result == [[1,5]]

def test3():
    result = Solution().merge([[1,4],[0,0]])
    assert result == [[0,0],[1,4]]

def test4():
    result = Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]])
    assert result == [[1,10]]