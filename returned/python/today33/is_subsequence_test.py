from is_subsequence import Solution

def test1():
    assert Solution().isSubsequence('abc', 'ahbgdc') == True

def test2():
    assert Solution().isSubsequence('axc', 'ahbgdc') == False