from path_sum_iii import Solution, TreeNode


def test1():
    n10 = TreeNode(10)
    n5 = TreeNode(5)
    nm3 = TreeNode(-3)
    n3 = TreeNode(3)
    n2 = TreeNode(2)
    n11 = TreeNode(11)
    n3a = TreeNode(3)
    nm2 = TreeNode(-2)
    n1 = TreeNode(1)
    n10.left = n5
    n10.right = nm3
    n5.left = n3
    n5.right = n2
    nm3.right = n11
    n3.left = n3a
    n3.right = nm2
    n2.right = n1
    assert Solution().pathSum(n10, 8) == 3


def test2():
    n0 = TreeNode(0)
    n1a = TreeNode(1)
    n1b = TreeNode(1)
    n0.left = n1a
    n0.right = n1b
    assert Solution().pathSum(n0, 1) == 4
