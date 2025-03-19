from construct_quad_tree import Solution

def test1():
    input = [[0,1],[1,0]]
    assert Solution().construct(input) == [[0,1],[1,0],[1,1],[1,1],[1,0]]

def test2():
    input = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    assert Solution().construct(input) == [[0,1],[1,1],[0,1],[1,1],[1,0],None,None,None,None,[1,0],[1,0],[1,1],[1,1]]