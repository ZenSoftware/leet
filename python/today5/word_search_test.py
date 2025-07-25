from word_search import Solution

def test1():
    result = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    assert result == True

def test2():
    result = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    assert result == True

def test3():
    result = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    assert result == False