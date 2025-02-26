from serialize_and_deserialize_binary_tree import TreeNode, Codec

def test1():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5
    
    ser = Codec()
    serialized = ser.serialize(n1)

    deser = Codec()
    ans = deser.deserialize(serialized)
    None