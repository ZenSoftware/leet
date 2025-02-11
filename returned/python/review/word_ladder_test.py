from word_ladder import Solution

def test1():
    assert Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5

def test2():
    assert Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0

def test3():
    assert Solution().ladderLength("a", "c", ["a","b","c"]) == 2