from longest_increasing_path_in_a_matrix import Solution

def test1():
    input = [[9,9,4],[6,6,8],[2,1,1]]
    assert Solution().longestIncreasingPath(input) == 4

def test2():
    input = [[3,4,5],[3,2,6],[2,2,1]]
    assert Solution().longestIncreasingPath(input) == 4

def test3():
    input = [[1]]
    assert Solution().longestIncreasingPath(input) == 1