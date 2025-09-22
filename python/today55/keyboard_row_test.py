from keyboard_row import Solution


def test1():
    input = ["Hello", "Alaska", "Dad", "Peace"]
    assert Solution().findWords(input) == ["Alaska", "Dad"]


def test2():
    input = ["omk"]
    assert Solution().findWords(input) == []


def test3():
    input = ["adsdf", "sfd"]
    assert Solution().findWords(input) == ["adsdf", "sfd"]
