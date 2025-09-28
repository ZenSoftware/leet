from find_mode_in_binary_search_tree import Solution, TreeNode


def test1():
    t1 = TreeNode(1)
    t2a = TreeNode(2)
    t2b = TreeNode(2)
    t1.right = t2a
    t2a.left = t2b
    assert Solution().findMode(t1) == [2]
