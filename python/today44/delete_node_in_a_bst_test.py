from delete_node_in_a_bst import Solution, TreeNode


def test1():
    n5 = TreeNode(5)
    n3 = TreeNode(3)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n7 = TreeNode(7)
    n5.left = n3
    n5.right = n6
    n3.left = n2
    n3.right = n4
    n6.right = n7
    result = Solution().deleteNode(n5, 3)
    assert result.left.val == 4
    assert result.left.left.val == 2
    assert result.left.right == None
    assert result.right.val == 6
    assert result.right.right.val == 7
