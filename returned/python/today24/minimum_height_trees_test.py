from minimum_height_trees import Solution

def test1():
    assert Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]]) == [1]

def test2():
    assert Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]) == [3,4]
    assert Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]]) == [1]

def test3():
    assert Solution().findMinHeightTrees(3, [[0,1],[0,2]]) == [0]