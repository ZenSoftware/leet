from permutations import Solution

def test1():
    assert Solution().permute([1,2,3]) == [[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2],[3,2,1]]
                                            # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
def test2():
    assert Solution().permute([0,1]) == [[0,1],[1,0]]

def test3():
    assert Solution().permute([1]) == [[1]]

    