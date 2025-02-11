from sum_root_to_leaf_numbers import Solution, TreeNode

def test1():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    assert Solution().sumNumbers(a) == 25
