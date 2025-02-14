from binary_search_tree_iterator import BSTIterator, TreeNode

def test1():
    n7 = TreeNode(7)
    n3 = TreeNode(3)
    n15 = TreeNode(15)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n7.left = n3
    n7.right = n15
    n15.left = n9
    n15.right = n20

    bst_iter = BSTIterator(n7)
    
    assert bst_iter.next() == 3
    assert bst_iter.next() == 7
    assert bst_iter.hasNext() == True
    assert bst_iter.next() == 9
    assert bst_iter.hasNext() == True
    assert bst_iter.next() == 15
    assert bst_iter.hasNext() == True
    assert bst_iter.next() == 20
    assert bst_iter.hasNext() == False
