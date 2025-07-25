from the_skyline_problem import Solution

def test1():
    input = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    result = Solution().getSkyline(input)
    assert result == [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

def test2():
    input = [[0,2,3],[2,5,3]]
    result = Solution().getSkyline(input)
    assert result == [[0,3],[5,0]]