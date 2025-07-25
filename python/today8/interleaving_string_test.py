from interleaving_string import Solution

def test1():
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == True

def test2():
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") == False

def test3():
    assert Solution().isInterleave("", "", "") == True

def test4():
    assert Solution().isInterleave("a", "b", "a") == False
