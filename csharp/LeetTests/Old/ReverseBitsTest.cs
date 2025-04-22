using Old.ReverseBits;

namespace LeetTests.Old
{
    internal class ReverseBitsTest
    {
        [Test]
        public void TestsReverseBits()
        {
            var solution = new Solution();
            Assert.That(
                solution.reverseBits(0b00000010100101000001111010011100),
                Is.EqualTo(0b00111001011110000010100101000000)
            );
            Assert.That(
                solution.reverseBits(0b11111111111111111111111111111101),
                Is.EqualTo(0b10111111111111111111111111111111)
            );
        }
    }
}
