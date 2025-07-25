from repeated_substring_pattern import Solution


def test1():
    assert Solution().repeatedSubstringPattern("abab") == True


def test2():
    assert Solution().repeatedSubstringPattern("aba") == False


def test3():
    assert Solution().repeatedSubstringPattern("abcabcabcabc") == True


def test4():
    assert Solution().repeatedSubstringPattern("babbabbabbabbab") == True


def test5():
    assert Solution().repeatedSubstringPattern("aabaaba") == False
