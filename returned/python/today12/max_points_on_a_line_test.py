from max_points_on_a_line import Solution

def test1():
    assert Solution().maxPoints([[1,1],[2,2],[3,3]]) == 3

def test2():
    assert Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4