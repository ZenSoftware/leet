from convert_a_number_to_hexadecimal import Solution

def test1():
    assert Solution().toHex(26) == '1a'
    assert Solution().toHex(-1) == 'ffffffff'