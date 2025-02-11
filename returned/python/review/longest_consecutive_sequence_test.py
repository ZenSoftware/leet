from longest_consecutive_sequence import Solution

def test1():
    assert Solution().longestConsecutive([100,4,200,1,3,2]) == 4

def test2():
    assert Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9