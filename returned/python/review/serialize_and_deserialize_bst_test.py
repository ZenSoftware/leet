from serialize_and_deserialize_bst import Codec, TreeNode


def test1():
    #        1
    #      /   \
    #     2     3
    #          /
    #         4
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    serialized = Codec().serialize(n1)
    assert serialized == "1,2,n,n,3,4,n,n,n"

    deserialized = Codec().deserialize(serialized)
    assert deserialized.val == 1
    assert deserialized.left.val == 2
    assert deserialized.right.val == 3
    assert deserialized.right.left.val == 4
