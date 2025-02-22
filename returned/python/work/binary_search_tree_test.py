from binary_search_tree import BinarySearchTree

def test_constructor():
    bst = BinarySearchTree([1,2,3,4,5,6,7])
    assert bst.root.value == 4

def test_delete():
    bst = BinarySearchTree([1,2,3,4,5,5,6,7])
    assert bst.get_inorder() == [1,2,3,4,5,5,6,7]
    bst.delete(4)
    assert bst.get_inorder() == [1,2,3,5,5,6,7]
    assert bst.root.value == 5
    bst.delete(5)
    assert bst.root.count == 1
    bst.delete(5)
    assert bst.get_inorder() == [1,2,3,6,7]
    bst.delete(99)
    assert bst.get_inorder() == [1,2,3,6,7]

def test_get_max():
    bst = BinarySearchTree([1,2,3,4,5,6,7,8,9,10])
    assert bst.get_max() == 10
    bst = BinarySearchTree()
    assert bst.get_max() == None

def test_get_min():
    bst = BinarySearchTree([1,2,3,4,5,6,7,8,9,10])
    assert bst.get_min() == 1
    bst = BinarySearchTree()
    assert bst.get_min() == None