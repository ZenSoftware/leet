from summary_ranges import Solution

def test1():
    assert Solution().summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]

def test2():
    assert Solution().summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]

def test3():
    assert Solution().summaryRanges([]) == []

def test4():
    assert Solution().summaryRanges([1]) == ['1']