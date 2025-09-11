from predict_the_winner import Solution


def test1():
    assert Solution().predictTheWinner([1, 5, 2]) == False


def test2():
    assert Solution().predictTheWinner([1, 5, 233, 7]) == True
