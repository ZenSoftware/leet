from detect_capital import Solution


def test1():
    assert Solution().detectCapitalUse("USA") == True


def test2():
    assert Solution().detectCapitalUse("FlaG") == False
