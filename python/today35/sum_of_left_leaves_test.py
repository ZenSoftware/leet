from sum_of_left_leaves import Solution, TreeNode

def test1():
    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)
    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7
    assert Solution().sumOfLeftLeaves(n3) == 24