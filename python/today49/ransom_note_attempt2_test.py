from ransom_note_attempt2 import Solution


def test1():
    assert Solution().canConstruct("a", "b") == False


def test2():
    assert Solution().canConstruct("aa", "ab") == False


def test3():
    assert Solution().canConstruct("aa", "aab") == True
