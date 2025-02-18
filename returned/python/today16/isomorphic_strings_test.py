from isomorphic_strings import Solution

def test1():
    assert Solution().isIsomorphic("egg", "add") == True

def test2():
    assert Solution().isIsomorphic("foo", "bar") == False

def test3():
    assert Solution().isIsomorphic("paper", "title") == True

def test4():
    assert Solution().isIsomorphic("badc", "baba") == False