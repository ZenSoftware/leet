from word_break_ii import Solution

def test1():
    result = Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
    assert result == ['cat sand dog','cats and dog']
                     
def test2():
    result = Solution().wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])
    assert result == ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']

def test3():
    result = Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"])
    assert result ==[]