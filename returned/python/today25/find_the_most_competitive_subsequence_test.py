from find_the_most_competitive_subsequence import Solution

def test1():
    assert Solution().mostCompetitive([3,5,2,6], 2) == [2,6]

def test2():
    assert Solution().mostCompetitive([2,4,3,3,5,4,9,6], 4) == [2,3,3,4]