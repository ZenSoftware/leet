from word_break_ii import Solution

def test1():
    result = Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
    assert result == ["cats and dog","cat sand dog"]

def test2():
    result = Solution().wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])
    assert result ==["pine apple pen apple","pineapple pen apple","pine applepen apple"]

def test3():
    result = Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"])
    assert result ==[]