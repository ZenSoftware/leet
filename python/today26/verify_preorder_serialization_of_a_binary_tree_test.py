from verify_preorder_serialization_of_a_binary_tree import Solution

def test1():
    assert Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#") == True

def test2():
    assert Solution().isValidSerialization("1,#") == False

def tes3():
    assert Solution().isValidSerialization("9,#,#,1") == False