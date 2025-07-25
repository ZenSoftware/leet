from partition_equal_subset_sum import Solution

def test1():
    assert Solution().canPartition([1,5,11,5]) == True

def test2():
    assert Solution().canPartition([1,2,3,5]) == False