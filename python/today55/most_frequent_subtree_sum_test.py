from most_frequent_subtree_sum import Solution, TreeNode


def test1():
    t5 = TreeNode(5)
    t2 = TreeNode(2)
    tn3 = TreeNode(-3)

    t5.left = t2
    t5.right = tn3

    result = Solution().findFrequentTreeSum(t5)
    result.sort()
    assert result == [-3, 2, 4]
