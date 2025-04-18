from russian_doll_envelopes import Solution

def test1():
    assert Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3

def test2():
    assert Solution().maxEnvelopes([[1,1],[1,1],[1,1]]) == 1

def test3():
    assert Solution().maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]) == 5