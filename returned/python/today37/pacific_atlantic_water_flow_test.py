from pacific_atlantic_water_flow import Solution

def test1():
    input = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    result = Solution().pacificAtlantic(input)
    result.sort()
    assert result == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]