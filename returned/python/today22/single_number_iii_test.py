from single_number_iii import Solution

def test1():
    result = Solution().singleNumber([1,2,1,3,2,5])
    result.sort()
    assert result == [3,5]