from find_largest_value_in_each_tree_row import Solution, TreeNode


def test1():
    n1 = TreeNode(1)
    n3a = TreeNode(3)
    n2 = TreeNode(2)
    n5 = TreeNode(5)
    n3b = TreeNode(3)
    n9 = TreeNode(9)
    n1.left = n3a
    n1.right = n2
    n3a.left = n5
    n3a.right = n3b
    n2.right = n9

    assert Solution().largestValues(n1) == [1, 3, 9]
