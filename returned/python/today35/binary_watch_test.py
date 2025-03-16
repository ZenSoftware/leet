from binary_watch import Solution

def test1():
    result = Solution().readBinaryWatch(1)
    result.sort()
    assert result == ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]