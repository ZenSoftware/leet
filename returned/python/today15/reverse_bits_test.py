from reverse_bits import Solution

def test1():
    assert Solution().reverseBits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000

def test2():
    assert Solution().reverseBits(0b11111111111111111111111111111101) == 0b10111111111111111111111111111111