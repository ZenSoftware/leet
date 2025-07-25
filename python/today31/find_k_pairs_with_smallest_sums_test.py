from find_k_pairs_with_smallest_sums import Solution

def test1():
    assert Solution().kSmallestPairs([1,7,11], [2,4,6], 3) == [[1,2],[1,4],[1,6]]
    
def test2():
    assert Solution().kSmallestPairs([1,1,2], [1,2,3], 2) == [[1,1],[1,1]]
