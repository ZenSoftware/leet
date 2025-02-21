from word_search_ii import Solution

def test1():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"]]
    words = ["oath","pea","eat","rain"]
    assert Solution().findWords(board, words) == ['oath', 'eat']

def test2():
    board = [["a","b"],["c","d"]]
    words = ["abcb"]
    assert Solution().findWords(board, words) == []

def test3():
    board = [["a","b","c"],["a","e","d"],["a","f","g"]]
    words = ["eaabcdgfa"]
    assert Solution().findWords(board, words) == ["eaabcdgfa"]

def test4():
    board = [["a","b"],["a","a"]]
    words = ["bab"]
    assert Solution().findWords(board, words) == []

def test5():
    board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
    words = ["oa","oaa"]
    assert Solution().findWords(board, words) == ['oa', 'oaa']
