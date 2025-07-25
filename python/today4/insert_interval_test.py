from insert_interval import Solution

def test1():
    result = Solution().insert([[1,3],[6,9]], [2,5])
    assert result == [[1,5],[6,9]]

def test2():
    result = Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
    assert result == [[1,2],[3,10],[12,16]]

def test3():
    result = Solution().insert([[1,2],[3,4],[7,8]], [5,6])
    assert result == [[1,2],[3,4],[5,6],[7,8]]
