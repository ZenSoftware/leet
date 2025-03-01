from maximum_product_of_word_lengths import Solution

def test1():
    assert Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]) == 16

def test2():
    assert Solution().maxProduct(["a","ab","abc","d","cd","bcd","abcd"]) == 4

def test3():
    assert Solution().maxProduct(["a","aa","aaa","aaaa"]) == 0