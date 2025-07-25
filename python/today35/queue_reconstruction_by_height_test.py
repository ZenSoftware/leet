from queue_reconstruction_by_height import Solution

def test1():
    result = Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
    assert result == [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

def test2():
    result = Solution().reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]])
    assert result == [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]