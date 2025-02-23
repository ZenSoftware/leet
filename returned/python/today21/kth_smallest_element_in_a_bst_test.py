from kth_smallest_element_in_a_bst import Solution, TreeNode

def test1():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n3.left = n1
    n3.right = n4
    n1.right = n2
    assert Solution().kthSmallest(n3, 1) == 1