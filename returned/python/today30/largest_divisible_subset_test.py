from largest_divisible_subset import Solution

def test1():
    assert Solution().largestDivisibleSubset([1,2,3]) == [3, 1]

def test2():
    assert Solution().largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]) == [720, 360, 180, 90, 18, 9]